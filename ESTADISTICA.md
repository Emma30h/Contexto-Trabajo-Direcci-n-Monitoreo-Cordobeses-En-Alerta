# Trabajos de Estadística DMCA (SAE)

Guía para reproducir **tal cual** los trabajos de la carpeta `Trabajos de Estadistica/`. Todos salen del **Sistema de Atención de Emergencias (SAE)**, llevan al pie `* FUENTE DE INFORMACION: SAE` y comparten un estilo de tablero oscuro. Los colores marcados con (m) están medidos de los archivos; el resto son aproximados a ojo.

Los originales parecen exportados de un tablero tipo Looker Studio (mapa de Google, selector de "Periodo" con flecha, íconos Material). Esto es una inferencia: confirmar con el usuario de dónde salen los datos y con qué herramienta los arman.

## Los 4 trabajos de ejemplo

| Archivo | Formato | Qué es |
|---|---|---|
| `INFORME SEMANAL(SAE) 13-11 AL 19-11.pdf` | PDF 24 págs, 930 × 1315 pt (vertical) | Informe semanal completo: portada + General + una página por DJP + Fuera de cuadrante |
| `INFORME 911 (SAE) 13-11 AL 19-11.pdf` | PDF 1 pág, 930 × 600 pt (apaisado) | Placa "Multiagencia 911" |
| `Placa semanal numerica (SAE) 13-11 al 19-11.pdf` | PDF 1 pág, 930 × 600 pt (apaisado) | Placa "Resumen Numérico" semanal |
| `WhatsApp Image ... 9.57.43 AM.jpeg` | Imagen 1240 × 800 aprox. | Placa "Evolución de adherentes" (para WhatsApp) |

El período de los trabajos es semanal, **de viernes a jueves** (13/11 al 19/11/2026). Los nombres de archivo siguen el patrón `TIPO (SAE) dd-mm AL dd-mm`.

## Estilo común (todos)

- **Fondo** casi negro `#141a1e` (m) con degradé sutil; **paneles** en tarjetas oscuras `#1a232e` / `#29333d` (m) con esquinas redondeadas y borde fino. Las tarjetas destacadas llevan **borde con brillo (glow)**: aqua/turquesa para Alertas, **verde** para Positivos.
- **Encabezado** en una tarjeta ancha: logo del ojo (`Logos/iso_blanco.png`) a un lado, título `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA` en blanco, mayúsculas y negrita, y el **escudo de la Policía de la Provincia de Córdoba** (insignia dorada) al otro lado. El logo del ojo y el escudo se alternan de lado entre placas, pero siempre van los dos.
- **Selector de período**: etiqueta `Periodo:` en dorado `#e8c15a` aprox. y una caja con borde dorado que dice `13 nov 2026 - 19 nov 2026` (mes abreviado en minúscula).
- **Marca de agua** `D.M.C.A.` en gris tenue, grande y repetida en los paneles.
- **Pie** a la derecha: `* FUENTE DE INFORMACION: SAE`, letra chica.
- **Colores de datos**: Alertas = azul `#1899de` (m); **Positivos = verde lima** `#39f516` (m); aqua `#00ffd0` aprox. en las placas 911; barras multicolor por categoría en la placa de adherentes.
- **Tipografías**: títulos en una sans geométrica redondeada tipo Quicksand/Lexend, números grandes en la misma; texto de tablas y etiquetas en Arial; la portada del informe semanal usa Open Sans en negrita. Los números grandes se muestran con **punto de miles** (`2.983`, `199.225`).
- **Listas con barra**: cada fila con fondo alternado gris, texto en mayúsculas, número a la derecha y una barrita (azul para alertas, verde para positivos).
- Etiquetas de los tipos de hecho **tal cual salen del SAE**, en mayúsculas, ej. `EMERGENCIA DE SALUD (107) (INDIVIDUO DESCOMPENSADO)`, `DISTURBIOS (RUIDOS MOLESTOS)`.

### Ojo con los acentos
En la placa 911 y en la numérica aparecen letras rotas (`RIÃ‘A`, `ALTERACIÃ"N`, `PÃºBLICO`) por un problema de codificación de la fuente. **En trabajos nuevos hay que corregirlo** (`RIÑA`, `ALTERACIÓN`, `PÚBLICO`), usando UTF-8.

## 1) Informe semanal (PDF largo)

Orden de páginas:

1. **Portada**: fondo oscuro con foto desenfocada de la sala de monitoreo; arriba a la derecha el escudo; `DIRECCION MONITOREO CORDOBESES EN ALERTA` centrado en gris claro; el logo del ojo grande en el centro; abajo en blanco y negrita `INFORME SEMANAL` / `DESDE 13/11/2026 HASTA 19/11/2026`.
2. **General** (etiqueta `GENERAL` bajo el título). Distribución de paneles de arriba hacia abajo:
   - **Resumen de secuestros** (columna izquierda): Armas de Fuego, Armas Blancas, Estupefacientes, Vehículos, Otros, cada uno con su ícono y número.
   - **Barra apilada** azul/verde con **Alertas totales** y **Positivos**, con íconos de alerta y de tilde; y la tarjeta **Aprehendidos** con ícono de esposas.
   - **Gráfico de barras de Alerta por DJP / Positivo por DJP**: una pareja azul/verde por DJP (10, 11, 12, 13, 14, 15, 17, 19, 2, 20, 21, 22, 23, 24, 3, 4, 5, 6, 7, 8, 9 y "Fuera de Cuadrante"), con la cifra encima de cada barra.
   - **Día crítico** (barras horizontales domingo a sábado) y **Hora crítica** (columnas 0 a 23), ambos con alertas en azul y positivos en verde.
   - **Tipología de positivos** (lista con barras verdes) y **Concentración de positivos** (mapa oscuro de Google de toda la ciudad con puntos verdes).
3. **Una página por DJP**, en este orden: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 24 (no hay 1, 16 ni 18). Misma plantilla que General, pero el título lleva a la derecha `DJP n` y el mapa se acerca al cuadrante. Esta página trae además **Hora crítica** como barras horizontales y la **Tipología** dividida en `ALERTAS` (celeste) y `POSITIVOS` (verde).
4. **Fuera de cuadrante** (última página): misma plantilla, con el título `FUERA DE CUADRANTE`.

Cuando una DJP no tiene positivos, el panel de positivos dice `No hay datos`.

## 2) Placa Multiagencia 911 (apaisada)

- Título grande `Multiagencia 911`, `Periodo 13 nov 2026 - 19 nov 2026`, y al centro `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA`. Escudo a la izquierda y ojo a la derecha.
- Fila superior: tarjeta **ALERTAS** (748), barras por zona **ESTE / CENTRO-OESTE / NORTE / SUR** (más una zona chica) y tarjeta **POSITIVOS** (23) con brillo verde.
- Fila inferior, 4 paneles: **Tipología de Alertas** (lista), **DJP** (barras horizontales aqua ordenadas, el mayor resaltado), **Día Crítico** y **Horario Crítico** (0 a 23), y **Tipología de Positivos** (lista).
- Todas las barras de esta placa son **aqua**.

## 3) Placa Resumen Numérico (apaisada)

- Título `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA` y `Periodo:` a la izquierda, `Resumen Numérico` al centro, ojo y escudo a la derecha.
- Dos tarjetas grandes: **ALERTAS** (2.983, borde aqua) y **POSITIVOS** (100, borde verde).
- Panel **APREHENDIDOS**: dona **Masculino** (azul violeta `#2500c9` (m)) y **Femenino** (magenta), con el porcentaje de cada uno, **TOTAL** al centro (45) y dos tarjetas chicas **MAYORES** (41) / **MENORES** (4).
- Lista **POSITIVOS** por tipo, con barritas verdes.
- Panel **RESUMEN DE SECUESTROS**: Armas de Fuego, Armas Blancas, Vehículos, Estupefacientes y Otros, cada uno con su ícono y número grande.

## 4) Evolución de adherentes (imagen)

- Encabezado con escudo a la izquierda, ojo a la derecha, `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA`, título enorme `EVOLUCION DE ADHERENTES` en una sans geométrica gruesa y la fecha debajo: `20 / 11 / 2026`.
- Tarjeta ancha con borde aqua: `ADHERIDOS TOTALES` y el número grande (`199.225`).
- Abajo, dos paneles: **gráfico de barras horizontales por cuadrante** (cada cuadrante con su color: rosa, naranja, amarillo, turquesa, azul, violeta, gris, coral, verde para "Sin cuadrante") y **tabla** `CUADRANTE` / `ADHERIDOS` con bordes gris claro, ordenada de mayor a menor.
- Pensada para enviar por WhatsApp (imagen).

## Cómo producirlo (para Claude)

- Los tableros se arman en HTML/CSS (o canvas) con gráficos vectoriales y se exportan: **PDF** con Chrome (A4 no: usar el tamaño exacto de cada pieza: 930 × 600 pt apaisado, 930 × 1315 pt el informe) o **PNG** para las placas.
- Los mapas de concentración son mapa base **oscuro** con puntos verdes; si no hay acceso a Google Maps, usar otro mapa oscuro equivalente (por ejemplo, el KML de barrios de `Mapa Cordobeses en Alerta/`) y avisar.
- Hay que pedirle al usuario el **export de datos del SAE** (alertas, positivos, DJP, tipología, hora, día, aprehendidos, secuestros) antes de armar nada. No inventar cifras.
- Antes de entregar: cuadrar que la suma por DJP, por día y por hora coincida con el total de Alertas, y que los Positivos cierren con la tipología.
- Comparar visualmente con los ejemplos página por página.
