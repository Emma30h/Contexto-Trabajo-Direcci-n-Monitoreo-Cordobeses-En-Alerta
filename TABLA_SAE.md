# Tabla de Hechos SAE (histórico): cómo leerla

Guía para leer los CSV de `Table de Hechos SAE Historico/` sin errores. Actualizada el 26/11/2026 con el histórico completo. Hay un cargador listo: **`leer_tabla_sae.py`** (en la carpeta `DMCA Claude`). Usarlo siempre en vez de leer los CSV a mano.

```python
from leer_tabla_sae import cargar_historico
df = cargar_historico(r"C:\Users\Cordobeses en Alerta\Desktop\DMCA Claude\Table de Hechos SAE Historico")
```

Carga los dos CSV, repara los textos, normaliza fechas y números, quita repetidos y agrega columnas limpias (`fecha_creacion`, `min_despacho`, `djp`, `cuadrante`, `lat`, `lon`, `tipo`, `positivo`, `fuera_de_cuadrante`). Para un solo archivo: `cargar_sae(ruta)`.

> **Datos sensibles.** La tabla trae teléfonos de denunciantes, relatos con domicilios y nombres, usuarios del sistema y un campo `Recurso` con números de 8 dígitos (parecen DNI del personal). **No copiar esas columnas a informes, placas, chats ni documentos.** Para análisis usar solo agregados.

## Advertencia principal: la base cambió con el tiempo

**No es una base estable.** Entre septiembre de 2025 y noviembre de 2026 cambiaron las columnas, el formato de los datos y qué tan completo se carga cada campo. Una serie que cruce los dos exports puede mostrar "mejoras" o "saltos" que son del registro, no de la realidad.

Lo que cambió, y qué implica:

| Cambio | Antes | Ahora | Riesgo si se ignora |
|---|---|---|---|
| `Origen`, `Zona` | no existían | desde el 23/10/2026 | No hay histórico por origen ni por zona. Cualquier serie larga por 911 vs Garden es imposible |
| `Medio de origen` | no existía | desde el 13/11/2026 | Ídem; además todavía está 94 % vacía |
| **Barrios en el programa** | ~110 | ~230 | **El programa se expandió**: un conteo por barrio o un total mensual crece en parte por esto, no solo por más hechos. Ver abajo |
| `Comuna` (DJP) vacía | 14,4 % | 1,1 % | Comparar 2025 con 2026 exagera el aumento por DJP |
| Fuera de cuadrante | 21,7 % | 5,0 % | **No es mejora de registro**: son barrios que se incorporaron y pasaron a tener cuadrante |
| Formato de `Fecha Despacho` | con segundos (75 %) | sin segundos | Un parseo con formato fijo descarta decenas de miles de filas sin avisar |
| Volumen mensual | ~5.100 | hasta 11.008 | Comparar meses sin normalizar lleva a conclusiones falsas |
| Cifras ya publicadas | — | — | Las cartas se siguen editando: los aprehendidos de un período cerrado ya no dan igual que en la exposición |

### La expansión del programa (medida sobre los datos)

Los 234 barrios no estuvieron siempre: se fueron sumando. Contando barrios distintos con hechos por mes:

| | sep 25 – mar 26 | abr 26 | jun 26 | jul 26 | **ago 26** | oct 26 |
|---|---|---|---|---|---|---|
| Barrios | ~110 | 136 | 161 | 185 | **223** | 230 |
| Hechos del mes | ~5.200 | 5.747 | 5.644 | 6.190 | **9.262** | 11.008 |
| Fuera de cuadrante (cargado) | ~21 % | 13,7 % | 13,6 % | 13,5 % | **7,6 %** | 6,5 % |
| Fuera de cuadrante (geometría) | ~5,5 % | 6,0 % | 6,4 % | 6,8 % | 7,4 % | 6,6 % |

El programa **duplicó su cobertura entre marzo y agosto de 2026**, de unos 110 barrios a 223. El salto de volumen de agosto (de 6.190 a 9.262 hechos, un 50 % más) coincide exactamente con ese mes.

Esto explica también la caída de "fuera de cuadrante" del 21 % al 5 %: **no fue que se registrara mejor**, sino que barrios que antes quedaban afuera se incorporaron y pasaron a tener cuadrante. La prueba es la última fila: medido por geometría contra los polígonos de hoy, el porcentaje de hechos realmente fuera del área se mantiene plano entre 5 % y 7 % todo el período.

**Consecuencia para los informes**: cualquier serie larga de hechos, por barrio o total, mezcla dos cosas, más actividad y más cobertura. Para comparar en serio hay que normalizar, por ejemplo midiendo hechos por barrio adherido, o restringiendo la comparación a los barrios que ya estaban en el período más viejo.

**Regla antes de comparar dos períodos**: verificar que la columna existía en los dos y que estaba igual de completa. Si no, decirlo al pie del informe o directamente no hacer esa comparación.

**Regla antes de repetir una cifra publicada**: recalcularla sobre la tabla y, si no coincide, informar la diferencia en vez de elegir la que convenga.

## Qué hay

Un registro por **hecho/carta** del SAE WEB. Dos exports que se continúan sin huecos ni superposición:

| Archivo | Período | Hechos | Suceso ID |
|---|---|---|---|
| `SAE BACKUP - SAE.csv` | 18/09/2025 al 31/05/2026 | 44.638 | 11.667 – 62.913 |
| `SAE - SAE.csv` | 01/06/2026 al 19/11/2026 | 49.974 | 62.914 – 134.809 |
| **Unidos** | **18/09/2025 al 19/11/2026** | **94.612** | sin IDs repetidos |

Ambos tienen las mismas 46 columnas.

### Volumen por mes

| 2025 | | 2026 | | 2026 | |
|---|---|---|---|---|---|
| sep (desde el 18) | 1.747 | ene | 5.133 | jun | 5.644 |
| oct | 4.458 | feb | 5.184 | jul | 6.190 |
| nov | 5.118 | mar | 5.947 | ago | 9.262 |
| dic | 5.446 | abr | 5.747 | sep | 9.849 |
| | | may | 5.858 | oct | 11.008 |
| | | | | nov (hasta el 19) | 8.021 |

De ~5.100 hechos mensuales a comienzos de 2026 se pasó a 11.008 en octubre: **el volumen se duplicó**. Nunca comparar meses sin tener en cuenta ese crecimiento.

### Cifras del histórico completo (94.612 hechos)

- **Positivos**: 3.584 (3,8 % de los hechos).
- **Aprehendidos**: 2.159 (1.879 mayores y 280 menores; 1.978 masculinos y 189 femeninas).
- **Secuestros**: 1.043 vehículos · 544 estupefacientes · 286 armas blancas · 44 armas de fuego · 4.558 otros elementos.
- **Despacho**: mediana 1,95 min; 77,2 % en 3 minutos o menos.
- **Fuera de cuadrante**: 12,4 % del total, pero baja de 17,1 % en el período viejo a 8,2 % en el nuevo.
- **Tipos más frecuentes**: Sospechoso 26.617 · Disturbios 22.460 · Solicitud de presencia policial 17.070 · Emergencia de salud 4.099 · Robo 3.845 · Incidentes viales 2.807.

## Contraste con las cifras publicadas

La exposición general informa, para el **1/10/2025 al 30/9/2026**: 74.327 alertas, 2.860 positivos, 1.687 aprehendidos, mediana de despacho 2 min y 77 % despachado en 3 minutos o menos sobre 74.288 hechos.

Con estos archivos, el mismo período da:

| Cifra | Exposición | Tabla | Diferencia |
|---|---|---|---|
| Alertas | 74.327 | **73.836** | −491 |
| Hechos con tiempo de despacho | 74.288 | **73.797** | −491 |
| Positivos | 2.860 | **2.836** | −24 |
| Aprehendidos | 1.687 | **1.773** | **+86** |
| Mediana de despacho | 2 min | **1,98 min** | coincide |
| Despachado en ≤ 3 min | 77 % | **76,6 %** | coincide |

Los tiempos reproducen exactamente lo publicado, y la diferencia de **−491 es idéntica en las dos filas de alertas**, lo que indica que el export tiene 491 hechos menos que la base usada para la exposición (0,7 %). En cambio **los aprehendidos dan 86 más en la tabla**: eso no se explica por hechos faltantes, así que probablemente las cartas se siguieron editando después de armar la exposición. Antes de repetir cualquiera de estas cifras conviene decidir cuál es la fuente válida.

## Problemas de los archivos (y cómo se resuelven)

| Problema | Detalle | Solución |
|---|---|---|
| **Acentos rotos** | Nombres de columna y textos con UTF-8 leído como Latin-1 (`CreaciÃ³n`, `vehÃ­culos`, `RIÃ'A`). Ya aparecía en las placas. | El cargador los repara. Al exportar, usar UTF-8 correcto. |
| **Fechas en formatos mezclados** | `Fecha Creacion` siempre trae segundos; `Fecha Despacho` los trae en el backup (75 % de las filas) pero no en el export nuevo; `Fecha Arribo` nunca. Día primero en todos. | El cargador usa formato mixto. **Un formato fijo descarta decenas de miles de filas en silencio.** |
| **Latitud/Longitud rotas** | Los puntos son separadores de miles: `-31.374.521.335.585.800`. Inutilizables. | Usar la columna **`lat.long`**, que está limpia. |
| **Tiempos como texto** | `0:02:44` (h:mm:ss). `Creacion-Arribo_segundos` usa coma decimal. `Tiempo de respuesta` es un entero en minutos. | El cargador convierte y agrega `min_despacho`. |
| **29 filas marcadas `!!!`** | En `total aprehendidos por genero`, 29 filas tienen masculinos + femeninas ≠ aprehendidos totales (por ejemplo, 9 femeninas con total 0). La tabla las marca sola con `!!!` en vez de `OK`. La última es del 27/09/2026. | Filtrar o corregir antes de informar cualquier apertura por género. Por menor/mayor no hay ninguna inconsistencia. |
| **Un hecho duplicado** | Suceso ID 81600 aparece dos veces en el export nuevo. | El cargador lo quita. |
| **Arribo anterior a la creación** | 14 filas en el export nuevo. | Excluirlas al calcular tiempos. |

### Columnas que no existen en todo el período

| Columna | Desde | En el backup |
|---|---|---|
| `Origen` (Garden / Derivado 911) | 23/10/2026 | 100 % vacía |
| `Zona` (ESTE, CENTRO/OESTE, SUR, NORTE) | 23/10/2026 | 100 % vacía |
| `Medio de origen` (WHATSAPP, 911, RADIO, OTROS) | 13/11/2026 | 100 % vacía |

**No se puede analizar el histórico por origen ni por zona.** Esos cortes solo existen desde fines de octubre de 2026.

La georreferenciación también mejoró con el tiempo: `Cuadricula` y `BARRIO` están vacías en 17,3 % del backup y en 8,3 % del export nuevo; `Comuna` (la DJP) pasa de 14,4 % a 1,1 % vacía. Cualquier serie por barrio o por DJP que cruce los dos períodos va a mostrar una mejora que es del registro, no de la realidad.

### Numeración de los Suceso ID

Los IDs van del 11.667 al 134.809, un rango de 123.143, pero hay 94.612 hechos: **faltan 28.531 números**. Los huecos aparecen en todo el rango (12 a 19 % por cada tramo de 10.000) y se disparan a partir del ID 110.000, donde falta más de la mitad. Ese salto coincide con la puesta en marcha del 101 en el 911. Lo más probable es que la secuencia sea compartida con hechos de otras agencias que no salen en este export, pero conviene confirmarlo antes de usar los IDs para estimar totales.

## Diccionario de columnas (resumen)

- **Identificación y ubicación**: `Suceso ID` · `Cuadricula` (barrio/cuadrícula) · `Comisaria` (en realidad es el **cuadrante**: `CUADRANTE 1` a `8`; vacío = hecho **fuera de cuadrante**) · `Comuna` (en realidad es la **UT/DJP**: `DISTRITO n`) · `BARRIO` · `lat.long`.
- **Operación**: `Usuario Operador` · `Usuario Despachador` · `Supervisor` · `Usuario Cierre` (personal: no publicar) · `Recurso` (móvil/personal; sensible).
- **Contenido**: `Relato` (texto libre con teléfono y domicilio: sensible) · `Telefono Denunciante` (sensible) · `Tipo y Subtipo` (`TIPO (SUBTIPO)`).
- **Cierre**: `Resultado` · `Cierre Despachador` · `Cierre Supervisor`. Las dos últimas son listas semilibres con cientos de valores; agrupar antes de graficar.
- **Tiempos**: `Fecha Creacion`, `Fecha Despacho`, `Fecha Arribo`, `Tiempo Creación-Despacho`, `Tiempo Despacho-Arribo`, `Tiempo de respuesta`, `Creacion-Arribo_segundos`, `solo.hora`.
- **Aprehendidos y secuestros**: números por hecho, con las columnas de control `total aprehendidos por genero` y `total aprehendidos por MENOR/MAYOR` (`OK` o `!!!`).
- **Etiquetas del tablero**: `Origen`, `Zona`.

Un **positivo** es el hecho validado como relevante por el coordinador o el jefe y revisado por Auditoría (ver `FUNCIONAMIENTO.md`).

## Cómo se construye cada cifra de las placas

Verificado contra la placa semanal del 13 al 19/11/2026:

| Cifra de la placa | Regla | Placa | Tabla |
|---|---|---|---|
| **Aprehendidos** | suma de `aprehendidos totales` | 45 | 45 ✔ |
| Mayores / menores | suma de cada columna | 41 / 4 | 41 / 4 ✔ |
| **Secuestros** | suma de cada columna | AF 1 · AB 2 · estup. 10 · vehíc. 23 · otros 97 | igual ✔ |
| **Multiagencia 911: alertas** | `Origen = "Derivado 911"` | 748 | 748 ✔ |
| **Multiagencia 911: positivos** | ídem y `Resultado = "Positivo"` | 23 | 23 ✔ |
| **Alertas por DJP** | `Comuna`, solo en hechos **con cuadrante** | igual DJP por DJP | ✔ |
| **Fuera de Cuadrante** | `Comisaria` vacía | 141 | 141 ✔ |
| **Alertas totales** | las 21 DJP con frecuencia + fuera de cuadrante | **2.983** | tabla completa: **2.995** |
| **Positivos totales** | ídem | **100** | tabla completa: **101** |

**Por qué la placa da 12 alertas y 1 positivo menos**: descarta los hechos que tienen cuadrante pero no caen en una DJP con frecuencia (5 en `DISTRITO 1`, 1 en `DISTRITO 16`, 2 en `DISTRITO 18` y 4 sin `Comuna`). Los distritos 1, 16 y 18 no pertenecen a ninguna de las 8 frecuencias. Por eso **la suma por DJP + Fuera de Cuadrante da 2.983 y no 2.995**: hay que aclarar al pie qué total se informa.

**Diferencia sin explicar**: en esa semana la tabla da 43 masculinos y 2 femeninas (95,6 % / 4,4 %) y la placa muestra 93,3 % / 6,7 %, o sea 42 y 3. Los totales coinciden (45). Ninguna de las 29 filas marcadas `!!!` cae en esa semana, así que el desvío viene del tablero, no del dato.

## Chequeos para hacer siempre

- Contar `Suceso ID` únicos antes de sumar.
- No sumar a ninguna DJP los hechos **fuera de cuadrante**.
- Para tiempos usar `min_despacho` (de la columna `Tiempo Creación-Despacho`): es más precisa y más completa que restar las fechas, y es la que reproduce las cifras publicadas.
- `Tiempo de respuesta` está redondeado a minutos (79 % da 0 y 20 % da 1): no sirve para promedios finos.
- Los informes semanales van de **viernes a jueves**: filtrar `>= viernes 00:00` y `< viernes siguiente 00:00`.
- Agrupar `Cierre Supervisor` en pocas categorías antes de mostrarlo.
- Al cruzar los dos períodos, avisar que `Origen`, `Zona` y `Medio de origen` no existen antes de octubre de 2026.

## Geolocalización: recuperar barrio, cuadrante y DJP

Hecho el 26/11/2026 con `geolocalizar_sae.py` y el KML `Mapa Cordobeses en Alerta/234 barrios LIMITES AMPLIADOS.kml`. Resultado exportado en `hechos_geolocalizados.csv`.

```python
from leer_tabla_sae import cargar_historico
from geolocalizar_sae import geolocalizar, marcar_movil, mapa_barrio_djp
df = geolocalizar(cargar_historico(CARPETA_CSV), RUTA_KML_BARRIOS, RUTA_KML_UT)
df = marcar_movil(df)
```

### Qué trae el KML

| Carpeta | Contenido | Sirve para |
|---|---|---|
| `Cobertura por Barrio` | 234 polígonos **con nombre** | asignar barrio |
| `CUADRANTE 1` a `CUADRANTE 8` | 52 polígonos agrupados en 8 áreas | asignar cuadrante y detectar fuera de cuadrante |
| `Division Distrito` | 197 líneas y puntos, **sin nombre ni atributos** | nada |

Y el segundo KML, `UNIDADES TERRITORIALES ACTUALIZADO.kml`:

| Contenido | Sirve para |
|---|---|
| **25 polígonos de UT** con nombre (UT 1 a 24, más **UT 24 BIS**), agrupados en 5 carpetas por Subdirección General de Seguridad (CENTRO, ESTE, NORTE, OESTE, SUR) | asignar DJP/UT y **zona** |

Las carpetas del KML dan las 5 subdirecciones; la columna `Zona` del SAE usa 4 porque **une CENTRO y OESTE**. El script devuelve las dos: `geo_subdireccion` con las 5 y `geo_zona_sae` con las 4 del SAE. Queda además disponible `mapa_barrio_djp`, que deduce la DJP del barrio a partir de los propios datos, como control cruzado.

### Qué tan confiable es

Comparando contra lo que ya estaba cargado:

| Campo | Casos comparables | Coincidencia |
|---|---|---|
| Zona | 10.505 | **98,7 %** |
| Cuadrante | 82.444 | **99,6 %** |
| DJP vía barrio (mapa aprendido) | 72.590 | **98,8 %** |
| DJP vía polígonos de UT | 81.767 | **94,8 %** |
| Barrio (nombre exacto) | 74.383 | **91,4 %** |

El cuadrante y la zona se pueden usar con confianza.

**La DJP tiene un problema sin resolver.** Los polígonos de UT discrepan con la columna `Comuna` en el 5,2 % de los casos, y la discrepancia se concentra en unos pocos pares de distritos vecinos: 12→4 (549 hechos), 8→13 (338), 7→9 (304), 22→18 (266), 15→2 (257), 24→14 (208). Verifiqué si los límites habían cambiado en alguna fecha y **no**: la coincidencia es pareja entre 94 % y 95 % los quince meses. Es una diferencia estructural, no un cambio de límites. El caso más llamativo es el distrito 12: al principio el 87 % de sus hechos caían geográficamente en la UT 4 y hoy el 51 %.

Mientras no se defina cuál manda, **usar la geolocalización para completar la DJP donde falta, pero no para pisar la que ya está cargada**. El barrio no: el 8,6 % de desacuerdo son en parte variantes de nombre (`QUINTAS DEL ARGUELLO` contra `QUINTAS DE ARGUELLO`, `SAN FRANCISCO` contra `PARQUE SAN FRANCISCO`) y en parte barrios linderos o subdivisiones (`JARDIN` contra `SAN FERNANDO`, `ALTA CORDOBA` contra `LA FRATERNIDAD`). **Antes de usar el barrio geolocalizado hay que unificar el nomenclador** con el que usa el SAE.

### Qué se recupera

| Campo | Hechos que estaban vacíos y ahora tienen dato |
|---|---|
| Barrio | **+3.607** |
| Cuadrante | **+6.367** |
| DJP | **+6.305** (de 6.967 que faltaban) |
| **Zona** | **+77.567** |

Lo de la zona es lo más grande: la columna `Zona` existe recién desde el 23/10/2026, así que estaba vacía en el 88 % del histórico. Ahora se puede abrir **todo el período por zona**, con un 98,7 % de confiabilidad medida contra los meses en que sí estaba cargada. El reparto del histórico completo queda: Este 31.961, Centro/Oeste 22.453, Sur 17.791, Norte 15.867 y 6.540 fuera de toda UT.

### El dato más importante: "fuera de cuadrante" está sobrecontado

En la tabla hay **11.716 hechos marcados fuera de cuadrante (12,4 %)**, pero por geometría solo **5.744 caen realmente afuera (6,1 %)**. O sea, **6.367 hechos marcados como fuera de cuadrante ocurrieron dentro de un cuadrante** y se les puede asignar cuál. La cifra de fuera de cuadrante de las placas está, en los hechos, al doble de lo real.

A la inversa, hay **446 hechos con cuadrante cargado cuyo punto cae afuera**: o está mal el cuadrante o está mal la coordenada. Conviene revisarlos.

### Qué tan lejos ocurren los que sí están afuera

La columna `geo_dist_borde_m` da los metros hasta el borde del área cubierta (negativo adentro, positivo afuera). De los 5.744 que están realmente afuera:

- mediana: **179 m** del borde
- **4.302 (el 75 %) están a menos de 500 m**, o sea a unas pocas cuadras
- el 10 % está a más de 1,1 km, y el más lejano a 42 km (otra localidad)

Es decir: casi todo lo que se atiende "fuera de cuadrante" pasa pegado al límite. Sirve para discutir si conviene ampliar la cobertura en vez de tratarlos como excepción.

### Participación de móvil

`marcar_movil` agrega `hubo_movil`, que es verdadero si hay `Recurso` cargado o `Fecha Arribo`. Da **49,9 %** de los hechos.

**Ojo con esto**: los positivos tienen móvil en el **29,0 %** de los casos y los "sin novedad" en el **50,7 %**. Es al revés de lo esperable. Puede ser que en los hechos de riesgo alto intervenga el distrito policial (CAP) y no se cargue en `Recurso`, pero hay que confirmarlo antes de informar nada sobre intervención de móviles.

### `hechos_geolocalizados.csv`

94.612 filas, una por hecho, pensado para cruzar por `Suceso ID`. No incluye teléfono, relato ni usuarios. Columnas: `Suceso ID`, `fecha_creacion`, `lat`, `lon`, `barrio_cargado`, `geo_barrio`, `cuadrante_cargado`, `geo_cuadrante`, `geo_fuera`, `geo_dist_borde_m`, `djp_cargada`, `geo_ut`, `geo_djp`, `zona_cargada`, `geo_subdireccion`, `geo_zona_sae`, `hubo_movil`, `es_positivo`.

`geo_ut` conserva el **24 BIS** como etiqueta propia (3.066 hechos); `geo_djp` lo cuenta como 24, que es como aparece en `Comuna`.

## Preguntas abiertas para el usuario

1. ¿Cuál es el total oficial de alertas: con o sin los hechos de DJP sin frecuencia?
2. ¿De dónde sale el 93,3 % / 6,7 % de género en la placa numérica?
3. ¿Por qué la tabla tiene 86 aprehendidos **más** que la exposición en el mismo período? ¿Se siguieron editando las cartas?
4. ¿Los Suceso ID se comparten con hechos de otras agencias?
5. ¿Qué significa exactamente `Recurso` y por qué tiene tantos valores distintos?
6. ¿Hay datos anteriores al 18/09/2025?
7. ¿Qué nomenclador de barrios es el válido, el del KML o el del SAE?
8. ¿Por qué los positivos tienen menos móvil cargado que los "sin novedad"? ¿Interviene el CAP sin quedar en `Recurso`?
9. Los 6.367 hechos marcados fuera de cuadrante que caen adentro, ¿se corrigen en la base o se deja el dato como está?
10. Para la DJP, ¿manda el polígono del KML de UT o el campo `Comuna` del SAE? Hay un 5,2 % de desacuerdo estructural, sobre todo en los distritos 12, 8, 7, 22, 15 y 24.
11. ¿La UT 24 BIS debe informarse aparte o sumada a la 24?
