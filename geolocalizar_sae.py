"""Geolocaliza los hechos del SAE contra el KML de barrios y cuadrantes.

Agrega a cada hecho, a partir de su coordenada:
  - `geo_barrio`      : barrio según los 234 polígonos de "Cobertura por Barrio"
  - `geo_cuadrante`   : cuadrante (1 a 8) según los polígonos de las carpetas CUADRANTE n
  - `geo_fuera`       : True si el punto no cae en ningún cuadrante
  - `geo_dist_borde_m`: metros hasta el borde del cuadrante (negativo = adentro)
  - `geo_ut`          : unidad territorial del KML de UT ("7", "24 BIS", ...)
  - `geo_djp`         : la misma UT como número (24 BIS cuenta como 24)
  - `geo_subdireccion`: CENTRO / ESTE / NORTE / OESTE / SUR, según el KML de UT
  - `geo_zona_sae`    : igual, pero uniendo CENTRO y OESTE como lo hace la columna `Zona`
  - `hubo_movil`      : si intervino un móvil (ver `marcar_movil`)

Uso:
    from leer_tabla_sae import cargar_historico
    from geolocalizar_sae import geolocalizar, marcar_movil
    df = cargar_historico(CARPETA_CSV)
    df = geolocalizar(df, RUTA_KML_BARRIOS, RUTA_KML_UT)
    df = marcar_movil(df)
"""
import re
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely.strtree import STRtree

NS = {"k": "http://www.opengis.net/kml/2.2"}
# Córdoba capital está en ~31,4° S: un grado de longitud mide menos que uno de
# latitud. Con estos factores las distancias en grados pasan a metros.
M_POR_GRADO_LAT = 111_132.0
M_POR_GRADO_LON = 94_900.0


def _nombre(elem):
    n = elem.find("k:name", NS)
    return n.text.strip() if n is not None and n.text else None


def _poligonos(placemark):
    """Devuelve los Polygon de un Placemark (ignora agujeros interiores)."""
    salida = []
    for poly in placemark.findall(".//k:Polygon", NS):
        anillo = poly.find(".//k:outerBoundaryIs//k:coordinates", NS)
        if anillo is None or not anillo.text:
            continue
        pts = []
        for trozo in anillo.text.split():
            partes = trozo.split(",")
            if len(partes) >= 2:
                pts.append((float(partes[0]), float(partes[1])))  # (lon, lat)
        if len(pts) >= 4:
            g = Polygon(pts)
            if not g.is_valid:
                g = g.buffer(0)
            if not g.is_empty:
                salida.append(g)
    return salida


def leer_kml(ruta_kml: str):
    """Lee el KML y devuelve (barrios, cuadrantes) como dicts nombre -> geometría."""
    raiz = ET.parse(ruta_kml).getroot()
    barrios, cuadrantes = {}, {}

    for carpeta in raiz.findall(".//k:Folder", NS):
        nombre_carpeta = _nombre(carpeta) or ""

        if nombre_carpeta == "Cobertura por Barrio":
            for pm in carpeta.findall("k:Placemark", NS):
                geos = _poligonos(pm)
                nombre = _nombre(pm)
                if geos and nombre:
                    barrios[nombre] = unary_union(geos)

        elif nombre_carpeta.startswith("CUADRANTE"):
            geos = []
            for pm in carpeta.findall("k:Placemark", NS):
                geos += _poligonos(pm)
            if geos:
                cuadrantes[nombre_carpeta] = unary_union(geos)

    return barrios, cuadrantes


def leer_kml_ut(ruta_kml: str):
    """Lee el KML de unidades territoriales.

    Devuelve dict `UT -> (geometría, subdirección)`. Las UT están agrupadas en
    carpetas por Subdirección General de Seguridad (CENTRO, ESTE, NORTE, OESTE,
    SUR). Los placemarks que no son polígonos (puntos de referencia) se ignoran.
    """
    raiz = ET.parse(ruta_kml).getroot()
    uts = {}
    for carpeta in raiz.findall(".//k:Folder", NS):
        nombre_carpeta = _nombre(carpeta) or ""
        if "SUBDIR" not in nombre_carpeta.upper():
            continue
        subdir = nombre_carpeta.upper().replace("SUBDIR. GRAL. DE SEG.", "").strip()
        for pm in carpeta.findall("k:Placemark", NS):
            geos = _poligonos(pm)
            nombre = _nombre(pm)
            if not geos or not nombre:
                continue
            m = re.match(r"UT\s*(\d+)\s*(BIS)?", nombre.upper())
            if not m:
                continue
            etiqueta = m.group(1) + (" BIS" if m.group(2) else "")
            uts[etiqueta] = (unary_union(geos), subdir)
    return uts


def _asignar(lon, lat, nombres, arbol, geos):
    """Punto en polígono vectorizado: devuelve el nombre o None."""
    from shapely import points

    pts = points(lon, lat)
    salida = np.full(len(lon), None, dtype=object)
    idx_pt, idx_geo = arbol.query(pts, predicate="within")
    # Si un punto cae en más de un polígono (bordes compartidos), gana el primero.
    vistos = set()
    for p, g in zip(idx_pt, idx_geo):
        if p not in vistos:
            salida[p] = nombres[g]
            vistos.add(p)
    return salida


def geolocalizar(
    df: pd.DataFrame, ruta_kml: str, ruta_kml_ut: str | None = None
) -> pd.DataFrame:
    barrios, cuadrantes = leer_kml(ruta_kml)
    df = df.copy()
    tiene = df.lat.notna() & df.lon.notna()
    lon = df.loc[tiene, "lon"].to_numpy(float)
    lat = df.loc[tiene, "lat"].to_numpy(float)

    nb = list(barrios); gb = [barrios[k] for k in nb]
    nc = list(cuadrantes); gc = [cuadrantes[k] for k in nc]

    df["geo_barrio"] = None
    df.loc[tiene, "geo_barrio"] = _asignar(lon, lat, nb, STRtree(gb), gb)
    df["geo_cuadrante"] = None
    cuad = _asignar(lon, lat, nc, STRtree(gc), gc)
    df.loc[tiene, "geo_cuadrante"] = pd.Series(cuad, index=df.index[tiene]).str.extract(
        r"(\d+)", expand=False
    )
    df["geo_cuadrante"] = pd.to_numeric(df["geo_cuadrante"], errors="coerce")
    df["geo_fuera"] = tiene & df["geo_cuadrante"].isna()

    # Distancia al borde del área cubierta: negativa adentro, positiva afuera.
    from shapely import points, distance

    cobertura = unary_union(gc)
    borde = cobertura.boundary
    pts = points(lon, lat)
    d = distance(pts, borde) * M_POR_GRADO_LAT
    adentro = np.array([cobertura.contains(p) for p in pts])
    df["geo_dist_borde_m"] = np.nan
    df.loc[tiene, "geo_dist_borde_m"] = np.where(adentro, -d, d).round(0)

    if ruta_kml_ut:
        uts = leer_kml_ut(ruta_kml_ut)
        nu = list(uts)
        gu = [uts[k][0] for k in nu]
        df["geo_ut"] = None
        df.loc[tiene, "geo_ut"] = _asignar(lon, lat, nu, STRtree(gu), gu)
        # "24 BIS" se cuenta como distrito 24, que es como aparece en `Comuna`.
        df["geo_djp"] = pd.to_numeric(
            df["geo_ut"].astype("string").str.extract(r"(\d+)", expand=False), errors="coerce"
        )
        subdir = {k: v[1] for k, v in uts.items()}
        df["geo_subdireccion"] = df["geo_ut"].map(subdir)
        df["geo_zona_sae"] = df["geo_subdireccion"].replace(
            {"CENTRO": "CENTRO/OESTE", "OESTE": "CENTRO/OESTE"}
        )
    return df


def mapa_barrio_djp(df: pd.DataFrame, minimo: int = 5, pureza: float = 0.8) -> dict:
    """Aprende barrio -> DJP de los hechos que ya tienen las dos cosas.

    Solo acepta el barrio cuando hay al menos `minimo` hechos y una DJP
    concentra al menos `pureza` de ellos.
    """
    base = df[df.geo_barrio.notna() & df.djp.notna()]
    salida = {}
    for barrio, g in base.groupby("geo_barrio"):
        vc = g.djp.value_counts()
        if vc.iloc[0] >= minimo and vc.iloc[0] / len(g) >= pureza:
            salida[barrio] = int(vc.index[0])
    return salida


def marcar_movil(df: pd.DataFrame) -> pd.DataFrame:
    """Marca si intervino un móvil.

    `Recurso` identifica el móvil o el personal asignado y `Fecha Arribo` queda
    cargada cuando el móvil llegó al lugar. Se toma como intervención si hay
    cualquiera de las dos.
    """
    df = df.copy()
    df["tiene_recurso"] = df["Recurso"].notna()
    df["tiene_arribo"] = df["fecha_arribo"].notna()
    df["hubo_movil"] = df["tiene_recurso"] | df["tiene_arribo"]
    return df
