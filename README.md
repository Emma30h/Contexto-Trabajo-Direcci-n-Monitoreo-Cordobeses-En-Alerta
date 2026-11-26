# Contexto de trabajo · Dirección Monitoreo Cordobeses en Alerta

Guías y herramientas para trabajar con Claude en los proyectos de la **Dirección Monitoreo Cordobeses en Alerta** (Policía de la Provincia de Córdoba, Argentina).

Este repo existe para que el contexto no se pierda si cambia la computadora. Clonarlo en la máquina nueva y conectarlo a Claude alcanza para seguir trabajando.

## Cómo usarlo en una máquina nueva

```bash
git clone https://github.com/Emma30h/Contexto-Trabajo-Direcci-n-Monitoreo-Cordobeses-En-Alerta.git "DMCA Claude"
```

Después, en la aplicación de escritorio de Claude: **+ → Add folder** y elegir esa carpeta. Claude lee `CLAUDE.md` y arranca con todo el contexto cargado.

## Qué hay acá

| Archivo | Para qué |
|---|---|
| `CLAUDE.md` | Índice y reglas de trabajo. Es lo primero que lee Claude |
| `FUNCIONAMIENTO.md` | Cómo funciona la Dirección: estructura, glosario, recorrido de un hecho, cifras |
| `TABLA_SAE.md` | Cómo leer la tabla de hechos del SAE: trampas del archivo, diccionario de columnas, cómo se arman las cifras de las placas, geolocalización |
| `DISENO.md` | Identidad visual: logo, tipografías, colores, estructura de los informes |
| `ESTADISTICA.md` | Estructura y estilo de los trabajos estadísticos semanales |
| `PRESENTACIONES.md` | Cómo se diseñan y se cuentan las exposiciones: grilla, catálogo de láminas, animaciones |
| `EXPOSICION.md` | Datos técnicos de la exposición general y cómo armar una nueva |
| `leer_tabla_sae.py` | Carga limpia de los CSV del SAE (acentos, fechas mezcladas, duplicados) |
| `geolocalizar_sae.py` | Asigna barrio, cuadrante, UT/DJP y zona por punto en polígono, contra los KML |

## Qué NO está acá

Los **datos de origen** no se versionan: pesan más de 150 MB y tienen datos personales (teléfonos de denunciantes, relatos con domicilios, legajos del personal). Están en la carpeta local y respaldados en Google Drive:

- `Table de Hechos SAE Historico/` — los CSV del SAE
- `Informes/`, `Trabajos de Estadistica/` — los PDF de referencia
- `Mapa Cordobeses en Alerta/` — los KML de barrios y unidades territoriales
- `Logos/`, `Frecuencia RugGear/`, `Exposiciones DMCA/`

Los scripts esperan encontrar esas carpetas al lado de los `.md`.

## Dependencias de los scripts

```bash
pip install pandas shapely
```
