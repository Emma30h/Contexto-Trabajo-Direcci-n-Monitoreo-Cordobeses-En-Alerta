# Guía de diseño DMCA

Sacada de los trabajos que hay en esta carpeta (2 informes en PDF y el mapa de frecuencias). Todo trabajo nuevo tiene que verse de la misma familia que estos. Los colores marcados con (m) están medidos de los archivos; el resto son aproximados a ojo y se pueden ajustar con el usuario.

## Identidad común

- **Logo**: archivo `Logos/iso_blanco.png` (500 × 369 px, fondo transparente). Es el isotipo: ojo con contorno **blanco** (`#fbfbfb`), marcador de ubicación (pin) celeste `#24abe6` con una mitad más oscura, e iris/pupila gris oscuro `#353535` con un corte. Como el contorno es blanco, **solo se ve sobre fondos oscuros o sobre la franja azul marino**; nunca sobre blanco. Va centrado arriba en las portadas y chico a la izquierda en el encabezado de cada página. Usar siempre el archivo, no redibujarlo ni deformarlo (mantener proporción, dejar aire alrededor).
- **Leyenda institucional**, siempre en mayúsculas, letra chica con mucho espaciado, color celeste:
  `POLICÍA DE LA PROVINCIA DE CÓRDOBA · DIRECCIÓN MONITOREO CORDOBESES EN ALERTA`
  (en el mapa solo: `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA`).
- **Tipografías**: títulos y números grandes en **Georgia** (serif); todo el resto en **Segoe UI** (Regular, Semibold, Bold, Italic). Los títulos de portada van en Georgia, centrados, en dos líneas.
- **Celeste de acento** (m): `#1590cf` en fondo claro, `#22a6e4` en fondo oscuro. El celeste del logo es `#24abe6`.
- **Marca de agua**: "D.M.C.A." en diagonal, muy tenue, repetida por la página.
- **Pie de página**: `D.M.C.A · NOMBRE DEL INFORME` a la izquierda y `PÁGINA X DE N` a la derecha, mayúsculas, letra mínima, gris.

## Informes en PDF

Se generan desde HTML con Chrome (impresión a PDF), **A4 vertical**, varias páginas. Hay dos variantes y se elige según el pedido:

| Variante | Cuándo | Fondo | Referencia |
|---|---|---|---|
| **Clara** | Informes con fotos, capturas y anexos (para imprimir) | Blanco `#ffffff` (m), tarjetas `#f5f8fb` (m) / `#eaf5fc` (m) | Informe hechos reiterados Citroën C4 Cactus |
| **Oscura** | Informes de operativos y estadísticas | `#0b0f14` (m), tarjetas `#121821` (m) y `#0f2a3d` (m) | Informe operativos de control de motocicletas |

### Estructura de la portada
1. Logo + leyenda institucional.
2. Título del informe en Georgia, centrado (ej. "Informe de hechos reiterados / vehículo Citroën C4 Cactus"). En la variante clara va sobre una franja azul marino (`#163452` (m)) con degradé; en la oscura, sobre el fondo.
3. Línea de período: `Periodo : dd/mm/aaaa al dd/mm/aaaa` (en operativos incluye horas).
4. Tarjeta **LUGAR Y FECHA** / **ASUNTO** (etiquetas chicas en mayúsculas a la izquierda, texto a la derecha, borde izquierdo celeste).
5. Párrafo introductorio: de dónde sale la información (Sistema de Atención de Emergencias, **SAE**) y qué se encontró.
6. Sección **Síntesis**: 4 tarjetas con un número grande en Georgia y una etiqueta debajo (ej. `4 hechos registrados`).
7. Tabla resumen con encabezado azul marino/oscuro.

### Páginas interiores
- **Encabezado** en todas: franja con degradé azul, logo chico, `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA` y debajo el nombre del informe; a la derecha el turno o dato y el período.
- **Títulos de sección** en Georgia, sin adornos ("Vehículo sindicado", "Desarrollo de los hechos", "Panorama de procedimientos…").
- **Bloque por hecho** (tarjeta con borde de color según tipo): número `01`, `02`… en Georgia celeste/naranja, título en negrita, **badge de tipología** a la derecha del título, y a la derecha el `SAE nnnnnn` en celeste. Debajo, datos en dos columnas: FECHA Y HORA / LUGAR / CUADRANTE / PERSONAL INTERVINIENTE; luego **DESARROLLO** y **RESULTADO** (etiquetas chicas en mayúsculas celestes, resultado con viñetas).
- **Recuadro de dato clave** (callout): fondo crema `#fdf4e7` (m), borde y título en naranja `#e08a1e` (m). Se usa para "Registro fílmico", "Uso de armamento menos letal", "Datos aportados por chat".
- **Tablas**: encabezado oscuro con texto en mayúsculas chicas, filas con línea fina, SAE en celeste y negrita. En listados largos se agrupan por **zona** con una franja de color a la izquierda (Norte azul, Este naranja, Centro/Oeste verde, Sur rosa).
- **Badges de tipología**, pastilla con texto blanco en mayúsculas: ROBO rojo, SOSPECHOSO naranja, TENTATIVA DE ROBO naranja, DAÑO azul. Estado: REGISTRADO azul, SIN CONFIRMAR naranja. En tablas de resultado: *Positivo* en celeste/verde, *Negativo* en naranja, *Sin novedad* en gris.
- **Mini tarjetas de coincidencias** (2 columnas): título en mayúsculas celestes y un párrafo corto.
- **Marco normativo**: tarjetas con el artículo en mayúsculas celestes (ej. `ART. 105 · CONDUCCIÓN PELIGROSA`) y el texto debajo.
- **Anexos**: "Anexo I · Partes de los hechos" (texto de cada parte en tarjeta con su badge) y "Anexo II · Capturas de chat" (capturas de WhatsApp en 2 o 3 columnas con pie de foto en gris chico).
- **Imágenes**: con borde fino, esquinas redondeadas y pie de foto en cursiva aclarando de dónde salen (por ejemplo, "imágenes ilustrativas del modelo").
- **Mapas dentro del informe**: mapa claro con marcadores numerados y colores por hecho, leyenda con distancias.

### Redacción del informe
- Fechas `dd/mm/aaaa`, horas `HH:MM Hs`, "SAE" seguido del número, dominios de vehículos en negrita y mayúsculas.
- Cantidades en letras y número la primera vez: "cuatro (04) hechos".
- Tono formal y objetivo, tercera persona. Siempre indicar de dónde sale cada dato (SAE, cámaras, vecinos, personal interviniente).
- Lo que no está confirmado se rotula como tal ("sin confirmar", "posible cambio de dominio").

## Mapas e infografías (imagen vertical)

Referencia: "Frecuencias Ruggear por distrito".

- Lienzo vertical **900 × 1600 aprox.**, fondo muy oscuro `#0b0f14`.
- Arriba: logo a la izquierda; a su derecha el título en Georgia (dos líneas) y debajo la leyenda `DIRECCIÓN MONITOREO CORDOBESES EN ALERTA` en celeste; línea divisoria fina.
- Mapa base oscuro con calles tenues en gris azulado; los polígonos (distritos/barrios) rellenos con color semitransparente y **borde del mismo color más claro**; cada polígono lleva su número en una etiqueta oscura redondeada con borde claro. Flecha de norte arriba a la derecha.
- Abajo: tarjeta de **REFERENCIAS** (título celeste en mayúsculas, fondo `#121821`, borde fino y esquinas redondeadas) con una fila por grupo: cuadrado de color, nombre en negrita, zona en mayúsculas del color del grupo y a la derecha los distritos en gris claro.
- **Colores por frecuencia** (aprox.): F1 azul `#2f7fd8`, F2 celeste `#7fb2ea`, F3 ocre `#b8790a`, F4 amarillo `#e0b45a`, F5 fucsia `#c04a7c`, F6 rosa `#e08fb0`, F7 verde `#22a050`, F8 violeta `#8f6bd1`. Zonas: Norte celeste, Este ocre, Sur rosa, Centro verde, Oeste violeta.

## Cómo producirlo (para Claude)

- Informes: armar HTML + CSS (Georgia/Segoe UI, A4, `@page`, saltos de página controlados) y exportar a PDF con Chrome sin encabezados del navegador. Revisar cada página renderizada antes de entregar.
- Mapas: dibujar sobre mapa base oscuro con los límites del KML de `Mapa Cordobeses en Alerta/`.
- No copiar datos del informe de ejemplo: es solo modelo de forma. Los datos personales y de hechos son reales y sensibles.
- Si falta una fuente (Segoe UI no suele estar en Linux), usar un reemplazo parecido y avisar al usuario.
