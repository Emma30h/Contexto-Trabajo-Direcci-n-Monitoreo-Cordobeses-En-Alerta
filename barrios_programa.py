"""Padrón oficial de barrios del programa y equivalencias de nombres.

Fuente: `Barrios/Nuevos barrios_ Ojos en alerta.xlsx`, hoja `BARRIOS`.
Trae por barrio el cuadrante, la UT, la población y la **fecha de
incorporación al programa**, que es el dato que permite normalizar cualquier
serie histórica.

El nombre del barrio se escribe distinto en cada fuente (padrón, SAE, KML), así
que `tabla_equivalencias` arma un puente por similitud. Las filas marcadas
`revisar` hay que validarlas a mano.

Uso:
    from barrios_programa import cargar_padron, tabla_equivalencias, normalizar
    padron = cargar_padron(RUTA_XLSX)
    equiv = tabla_equivalencias(padron, nombres_sae, nombres_kml)
"""
import difflib
import re
import unicodedata

import pandas as pd


def normalizar(s):
    """Mayúsculas, sin tildes y sin puntuación, para comparar nombres."""
    if not isinstance(s, str):
        return None
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().upper()
    s = re.sub(r"[^A-Z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip() or None


def cargar_padron(ruta_xlsx: str) -> pd.DataFrame:
    d = pd.read_excel(ruta_xlsx, sheet_name="BARRIOS", header=1)
    d.columns = [
        "_", "nro", "cuadrante_txt", "ut", "barrio",
        "poblacion", "superficie_km2", "fecha_incorporacion", "__",
    ][: len(d.columns)]
    d = d[["cuadrante_txt", "ut", "barrio", "poblacion", "fecha_incorporacion"]]
    # El Excel escribe el cuadrante y la UT una sola vez y deja el resto en blanco.
    d[["cuadrante_txt", "ut"]] = d[["cuadrante_txt", "ut"]].ffill()
    d = d[d.barrio.notna()]
    d = d[d.barrio.str.strip().str.lower() != "total"].copy()

    d["cuadrante"] = pd.to_numeric(
        d.cuadrante_txt.astype(str).str.extract(r"^(\d+)")[0], errors="coerce"
    ).astype("Int64")
    d["cuadrante_nombre"] = d.cuadrante_txt.astype(str).str.split("-").str[-1].str.strip()
    d["ut"] = pd.to_numeric(
        d.ut.astype(str).str.extract(r"(\d+)")[0], errors="coerce"
    ).astype("Int64")
    d["poblacion"] = pd.to_numeric(d.poblacion, errors="coerce")
    d["fecha_incorporacion"] = pd.to_datetime(d.fecha_incorporacion, errors="coerce")
    d["clave"] = d.barrio.map(normalizar)
    return d[
        ["barrio", "clave", "cuadrante", "cuadrante_nombre", "ut",
         "poblacion", "fecha_incorporacion"]
    ].reset_index(drop=True)


def tabla_equivalencias(padron: pd.DataFrame, *listas_de_nombres) -> pd.DataFrame:
    """Cruza nombres sueltos contra el padrón por similitud.

    Devuelve una fila por nombre distinto con el barrio oficial propuesto y una
    columna `confianza`: `exacto`, `alto` (>= 0,86) o `revisar`.
    """
    claves = padron.clave.tolist()
    por_clave = dict(zip(padron.clave, padron.barrio))
    vistos, filas = set(), []

    for lista in listas_de_nombres:
        for crudo in lista:
            k = normalizar(crudo)
            if not k or (crudo, k) in vistos:
                continue
            vistos.add((crudo, k))
            if k in por_clave:
                filas.append((crudo, por_clave[k], 1.0, "exacto"))
                continue
            cerca = difflib.get_close_matches(k, claves, n=1, cutoff=0.70)
            if cerca:
                r = difflib.SequenceMatcher(None, k, cerca[0]).ratio()
                filas.append(
                    (crudo, por_clave[cerca[0]], round(r, 3),
                     "alto" if r >= 0.86 else "revisar")
                )
            else:
                filas.append((crudo, None, 0.0, "revisar"))

    return pd.DataFrame(
        filas, columns=["nombre_origen", "barrio_oficial", "similitud", "confianza"]
    ).sort_values(["confianza", "similitud"], ascending=[True, False]).reset_index(drop=True)
