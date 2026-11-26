"""Carga limpia de la Tabla de Hechos SAE (CSV exportado del tablero).

Uso normal (histórico completo: backup + export actual):
    from leer_tabla_sae import cargar_historico
    df = cargar_historico(r"C:\\Users\\...\\Table de Hechos SAE Historico")

Un solo archivo:
    from leer_tabla_sae import cargar_sae
    df = cargar_sae(r"C:\\...\\SAE - SAE.csv")
    sem = df[(df.fecha_creacion >= "2026-11-13") & (df.fecha_creacion < "2026-11-20")]

Qué corrige (ver TABLA_SAE.md):
  - textos y nombres de columna con acentos rotos (UTF-8 leído como Latin-1)
  - fila duplicada exacta
  - fechas dd/mm/aaaa, tiempos h:mm:ss, decimales con coma
  - latitud/longitud (las columnas Latitud/Longitud vienen rotas: se usa lat.long)
No imprime ni exporta datos personales (teléfono, relato, usuarios, recurso).
"""
import glob
import os

import pandas as pd


def _fecha(serie):
    """Las fechas vienen en formatos mezclados entre exports y entre columnas:
    `18/09/2025 0:01:00` y `1/6/2026 0:03` conviven. Siempre día primero."""
    return pd.to_datetime(serie, dayfirst=True, format="mixed", errors="coerce")


def _fix(s):
    if not isinstance(s, str):
        return s
    for _ in range(3):
        try:
            t = s.encode("latin-1").decode("utf-8")
        except Exception:
            break
        if t == s:
            break
        s = t
    return s


# DJP (UT) que forman parte de las 8 frecuencias. Los Distritos 1, 16 y 18
# aparecen en la tabla pero no tienen frecuencia: la placa semanal los descarta.
DJP_CON_FRECUENCIA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 24]

NUM = [
    "menores aprehendidos", "mayores aprehendidos", "aprehendidos totales",
    "masculinos aprehendidos", "femeninas aprehendidas", "vehículos secuestrados",
    "estupefacientes secuestrados", "armas de fuego secuestradas",
    "armas blancas secuestradas", "otros elementos secuestrados",
]


def cargar_sae(ruta: str) -> pd.DataFrame:
    df = pd.read_csv(ruta, dtype=str, keep_default_na=False, na_values=[""])
    df.columns = [_fix(c).replace("\xa0", " ") for c in df.columns]
    for c in df.columns:
        df[c] = df[c].map(_fix)
    df = df.drop_duplicates().reset_index(drop=True)

    df["fecha_creacion"] = _fecha(df["Fecha Creacion"])
    df["fecha_despacho"] = _fecha(df["Fecha Despacho"])
    df["fecha_arribo"] = _fecha(df["Fecha Arribo"])
    # Duración creación -> despacho, en minutos. Más completa y precisa que
    # restar las fechas: es la que usan las cifras publicadas.
    df["min_despacho"] = (
        pd.to_timedelta(df["Tiempo Creación-Despacho"], errors="coerce").dt.total_seconds() / 60
    )
    for c in NUM:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

    # DJP como número ("DISTRITO 15" -> 15) y cuadrante como número ("CUADRANTE 3" -> 3)
    df["djp"] = pd.to_numeric(df["Comuna"].str.extract(r"(\d+)")[0], errors="coerce")
    df["cuadrante"] = pd.to_numeric(df["Comisaria"].str.extract(r"CUADRANTE\s+(\d+)")[0], errors="coerce")
    df["fuera_de_cuadrante"] = df["Comisaria"].isna()

    ll = df["lat.long"].str.split(",", expand=True)
    df["lat"] = pd.to_numeric(ll[0], errors="coerce")
    df["lon"] = pd.to_numeric(ll[1], errors="coerce")
    df["seg_creacion_arribo"] = pd.to_numeric(
        df["Creacion-Arribo_segundos"].str.replace(",", ".", regex=False), errors="coerce"
    )
    df["tipo"] = df["Tipo y Subtipo"].str.extract(r"^(.*?)\s*\(")[0]
    df["positivo"] = df["Resultado"].eq("Positivo")
    return df


def cargar_historico(carpeta: str) -> pd.DataFrame:
    """Carga y une todos los CSV del SAE de una carpeta (backup + export actual).

    Quita Suceso ID repetidos y ordena por fecha. Los exports son contiguos por
    ID, así que no debería haber solapamiento.
    """
    rutas = sorted(glob.glob(os.path.join(carpeta, "*.csv")))
    if not rutas:
        raise FileNotFoundError(f"No hay CSV en {carpeta}")

    partes = [cargar_sae(r) for r in rutas]
    df = pd.concat(partes, ignore_index=True)
    antes = len(df)
    df = df.drop_duplicates(subset="Suceso ID").sort_values("fecha_creacion")
    df.attrs["archivos"] = [os.path.basename(r) for r in rutas]
    df.attrs["duplicados_quitados"] = antes - len(df)
    return df.reset_index(drop=True)


def resumen_semanal(df: pd.DataFrame, desde: str, hasta_exclusivo: str) -> dict:
    """Cifras con las reglas de la placa semanal (ver TABLA_SAE.md)."""
    w = df[(df.fecha_creacion >= desde) & (df.fecha_creacion < hasta_exclusivo)]
    valido = w.fuera_de_cuadrante | w.djp.isin(DJP_CON_FRECUENCIA)
    placa = w[valido]
    return {
        "alertas_tabla": len(w),
        "alertas_placa": len(placa),
        "excluidas_de_placa": len(w) - len(placa),
        "positivos_tabla": int(w.positivo.sum()),
        "positivos_placa": int(placa.positivo.sum()),
        "aprehendidos": int(w["aprehendidos totales"].sum()),
        "masculinos": int(w["masculinos aprehendidos"].sum()),
        "femeninas": int(w["femeninas aprehendidas"].sum()),
        "mayores": int(w["mayores aprehendidos"].sum()),
        "menores": int(w["menores aprehendidos"].sum()),
        "vehiculos": int(w["vehículos secuestrados"].sum()),
        "estupefacientes": int(w["estupefacientes secuestrados"].sum()),
        "armas_fuego": int(w["armas de fuego secuestradas"].sum()),
        "armas_blancas": int(w["armas blancas secuestradas"].sum()),
        "otros": int(w["otros elementos secuestrados"].sum()),
    }
