# Presentaciones DMCA: cómo se diseñan y cómo se cuentan

Complemento de `EXPOSICION.md` (datos técnicos y variables). Este archivo explica **cómo se ve y cómo se presenta** la exposición general, para repetir el mismo criterio en cualquier presentación nueva. Referencia: las 30 láminas de `exposicion-general-cordobeses-en-alerta-para-choferes` (capturas en `print/laminas/` del repo).

## Principios de diseño

1. **Una idea por lámina**, y el título la dice completa como frase afirmativa ("Un equipo civil y policial bajo una misma dirección", "Dos puertas de entrada, un mismo circuito de trabajo"). Nunca títulos genéricos del tipo "Introducción".
2. **Tema oscuro, mucho aire y pocos colores**: fondo azul noche, paneles apenas más claros con borde fino, celeste como color de marca y **ámbar solo para lo que hay que notar** (avisos, excepciones, el paso final, el radio operador). El verde solo para "ok/positivo/personal policial".
3. **Las cifras son las protagonistas**: números enormes en Barlow Condensed celeste, con una etiqueta corta debajo en gris. El texto explicativo es chico y de apoyo.
4. **Capas de lectura**: kicker (tema) → título (mensaje) → contenido (tarjetas/pasos/cifras) → recuadro de aviso (excepción o aclaración) → fuente al pie. El público puede leer solo el título y entender.
5. **Todo se ve en pantalla grande y desde lejos**, pero los detalles finos (mono, 12–14 px) están reservados para metadatos: kicker, etiqueta de sección y fuentes.
6. **Honestidad de datos**: cada lámina con cifras lleva su **fuente y período** al pie en mono gris; los ejemplos de capacitación se rotulan "caso ficticio"; las pantallas con datos personales se difuminan.

## Grilla y medidas (lámina de 1600 × 900)

- Márgenes de la lámina: **96 px arriba, 88 px a los costados, 84 px abajo**.
- Kicker: JetBrains Mono 15 px, mayúsculas, espaciado `.14em`, celeste. Título `h2`: Barlow Condensed 700, **58 px** (44–52 px en láminas densas), ancho máximo 1300 px.
- Etiqueta de sección arriba a la derecha (`01 · Quiénes somos`), mono 12,5 px, gris tenue.
- Fuente al pie izquierdo, mono 12,5 px, gris tenue. Barra de progreso de 3 px celeste en el borde superior.
- Paneles: fondo `--panel`, borde 1 px `--line`, radio 10 px. Separaciones habituales de 16 a 24 px; columnas con gap de 56 a 60 px.
- Texto de apoyo: Barlow 17–22 px, gris `--muted`, interlineado ~1,45. Énfasis con `<b>` en blanco semibold.

## Catálogo de láminas (qué usar para cada tipo de contenido)

| Necesito mostrar… | Patrón | Ejemplo |
|---|---|---|
| Portada | Foto de la sala oscurecida a la izquierda con velo degradado; logo, leyenda mono celeste, título gigante en 2 líneas (blanco + celeste), bajada, fecha y un **QR** en un recuadro | Lámina 1 |
| Estructura u organigrama | Tarjeta raíz arriba, ramas en tarjetas, y a la derecha un **número grande** (188) con barra apilada y leyenda de colores | Lámina 2 |
| 4 a 5 cifras clave | Fila de tarjetas de cifra + una fila de 3 definiciones con **borde izquierdo de color** | Lámina 3 |
| Mapa + referencias | Mapa vectorial a la izquierda; a la derecha tabla agrupada por zona (cuadradito de color, nombre, UT) y un aviso ámbar | Lámina 4 |
| Dos caminos que se unen | Dos tarjetas lado a lado con etiqueta ("Vía principal" / "Se suma"), cadena de píldoras con flechas y una **franja ancha abajo** con la conclusión | Lámina 5 |
| Proceso de 5 a 7 pasos | Círculos con ícono unidos por línea punteada; número mono, título, descripción y **rol responsable** al pie; barra de roles debajo; recuadro con excepciones | Lámina 6 |
| Roles con foto | Foto de 620 × 500 con pie, y lista de tarjetas con título + etiqueta mono + descripción | Lámina 7 |
| Comparar sistemas/herramientas | 4 tarjetas iguales con ícono, nombre grande en display, subtítulo mono y descripción | Lámina 8 |
| Pantalla de un dispositivo | Imagen del equipo (RugGear) a la derecha y 3 tarjetas explicativas a la izquierda | Lámina 9 |
| Funciones de un puesto | **Video de fondo** (cabina o radio) con velo oscuro y lista vertical de 4 pasos con círculos numerados unidos por una línea; el paso actual se rellena | Láminas 10 y 13 |
| Réplica de un sistema | Mock fiel de la pantalla (SAE WEB) con píldoras de pasos arriba, una línea de descripción que cambia y los campos que se "llenan" de a uno; rótulo "caso ficticio" | Láminas 11 y 12 |
| Línea de tiempo | Barra segmentada (celeste → ámbar → gris) con hitos `0 / 1 min / 1 a 3 min`, y debajo quién actúa en cada tramo; un mensaje de WhatsApp de ejemplo arriba | Lámina 14 |
| Guía paso a paso | Número gigante (`01`, `02`…) + kicker + título + 3 pasos numerados en ámbar, y el equipo a la derecha animado; tecla R repite | Láminas 16 a 21 |
| Comparación en barras | Tarjetas con barra de proporción horizontal; la principal resaltada con borde celeste | Lámina 22 |
| Muchas categorías | Tarjeta de cifra grande + grilla de "chips" `categoría · n` | Lámina 23 |
| Flujo en dos sistemas | Pasos `01 02 03` a la izquierda y panel ámbar "Si ocurre" a la derecha; una cita en mono al pie | Lámina 24 |
| Cadena de valor | 4 tarjetas con flechas `→` (Registro → Control → Análisis → Decisión) y fuentes como píldoras | Lámina 27 |
| Resultados | 4 tarjetas altas con cifra enorme; la unidad chica en ámbar (`2 min`) | Lámina 28 |
| Equipo/turnos | Tabla chica + número grande + barras horizontales por función + foto | Lámina 29 |
| Cierre | "¡MUCHAS GRACIAS!" en display, 4 cifras, botón de descarga y el mapa de frecuencias de fondo | Lámina 30 |

## Animación y manera de presentar

- **Transición entre láminas**: fundido de 0,45 s. La lámina activa recibe la clase `.on`.
- **Entrada**: cada bloque (`data-a`) "sube" 20 px mientras aparece (0,7 s) con retraso escalonado de 70 ms entre bloques.
- **Revelado por pasos**: los bloques con `data-f="n"` aparecen de a uno con cada → o toque; los pendientes quedan **atenuados** (opacidad 16 %, sin saturación) en vez de ocultos, así el público ve el mapa completo y el orador lo recorre. En las réplicas de sistema, lo no cargado queda vacío.
- **Énfasis activo**: el paso en curso se rellena con el color de marca y un halo (`box-shadow` de 7 px translúcido); el resto, tenue.
- **Mapa vivo**: los polígonos de las UT se pintan con su color de frecuencia con retraso y brillo en el enfocado; las etiquetas aparecen al final.
- **Video**: clips cortos en bucle que se alternan con fundido de 1,2 s detrás de las láminas de roles; un rótulo con punto rojo parpadeante (`OPERADOR DE CABINA · CARGA EN EL SAE WEB`).
- **Controles**: ← → (también Espacio, Enter, PageDown) avanzan; **F** pantalla completa; **R** repite la animación; **G** abre la guía en vivo. Respeta `prefers-reduced-motion`.
- **Guía en vivo para el público**: el QR de la portada lleva a una guía que avanza en los celulares junto con las láminas.
- **Entrega impresa**: PDF de una lámina por página y afiche A4 en blanco y negro con el QR.

## Voz y redacción de las láminas

- Público: personas que van a trabajar en la calle. Frases cortas, directas, verbos en presente; en las guías, **imperativo voseante** ("Entrá", "Tocá", "Elegí", "Constatá").
- Aclarar lo que **no** hay que tocar o lo que pasa si falla ("Si no ves el aviso, el registro no se envió: repetí la carga").
- Un recuadro por lámina como máximo para la excepción importante.
- Términos del glosario siempre iguales (ver `FUNCIONAMIENTO.md`). Horas con "Hs". Cifras con punto de miles.

## Checklist para una presentación nueva

1. Definir el mensaje de cada lámina y escribirlo como título afirmativo.
2. Elegir el patrón del catálogo; no inventar diseños nuevos si hay uno que sirve.
3. Usar las variables de color y las tres tipografías; ámbar solo para lo que hay que notar.
4. Cada cifra con su fuente y período al pie; ejemplos rotulados como ficticios; difuminar datos personales.
5. Agregar revelado por pasos (`data-f`) en las láminas con 3 o más bloques.
6. Revisar lámina por lámina a 1600 × 900 y probar la navegación con teclado antes de publicar.
7. No hacer `git push` (publica la presentación) sin confirmación del usuario.
