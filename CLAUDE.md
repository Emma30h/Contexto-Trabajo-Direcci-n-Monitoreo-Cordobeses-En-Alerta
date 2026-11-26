# Espacio de trabajo DMCA

Contexto para Claude. Leer esto al empezar cualquier tarea en esta carpeta.

## Quién y para qué

- **DMCA** = Dirección Monitoreo Cordobeses en Alerta (Policía de Córdoba, Argentina).
- Esta carpeta reúne el material de trabajo del usuario: informes, mapas, datos de frecuencias y apoyo para las apps que mantiene.
- Idioma de trabajo: **español rioplatense**. Zona horaria: America/Argentina/Buenos_Aires (UTC-3).

## Carpetas

| Carpeta | Contenido |
|---|---|
| `Informes/` | Informes en PDF (hechos reiterados, operativos de control de motocicletas, etc.). Sirven de modelo de formato y estilo para informes nuevos. |
| `Mapa Cordobeses en Alerta/` | `234 barrios LIMITES AMPLIADOS.kml`: límites de los 234 barrios de Córdoba. Base para mapas y cruces por barrio. |
| `Exposiciones DMCA/` | URL de la exposición general (en GitHub Pages) que cuenta cómo funciona la Dirección. Contexto en `FUNCIONAMIENTO.md`; diseño y armado en `EXPOSICION.md`. |
| `Table de Hechos SAE Historico/` | Dos CSV contiguos con el histórico del SAE: 94.612 hechos del 18/09/2025 al 19/11/2026. **Leer `TABLA_SAE.md` y cargarlos con `cargar_historico()` de `leer_tabla_sae.py`.** Tienen datos sensibles. |
| `Trabajos de Estadistica/` | Ejemplos de los trabajos estadísticos del SAE (informe semanal de 24 págs, placas 911 y numérica, placa de adherentes). Hay que reproducirlos **tal cual**: ver `ESTADISTICA.md`. |
| `Barrios/` | `Nuevos barrios_ Ojos en alerta.xlsx`: padrón oficial de los 234 barrios con cuadrante, UT, población y **fecha de incorporación**. Se lee con `barrios_programa.py`. |
| `Logos/` | Logos oficiales. Hoy: `iso_blanco.png` (isotipo del ojo con contorno blanco, para fondos oscuros). Usar siempre estos archivos. |
| `Frecuencia RugGear/` | Imagen con la configuración de frecuencias del equipo RugGear. |

Nuevas tareas: crear una subcarpeta por tema y no mezclar archivos originales con resultados.

## Apps y repositorios (GitHub: Emma30h)

- **Perfiles Garden** → repo `Emma30h/Profile-DMCA`. App de gestión de personal policial (legajos, licencias, asistencia). Next.js + Prisma + Supabase (schema `gestion_personal`), mails con Brevo. Rama principal: `master`.
  - Mails de avisos médicos a RR.HH.: `src/lib/carpetaMedica.ts`, `src/app/actions/carpetaMedica.ts`, `src/app/(dashboard)/personal/[id]/EnviarCarpetaMedicaModal.tsx`. Solo para Civil Becario; cubre Carpeta Médica, Licencia Médica y licencias extraordinarias.
  - Ojo: el `AGENTS.md` del repo avisa que esta versión de Next.js tiene cambios incompatibles; leer `node_modules/next/dist/docs/` antes de escribir código.
- **Calendario Garden** → repo `Emma30h/calendario-garden`. Calendario de cumpleaños y efemérides. Desplegado en Railway con dos tareas programadas (`cron-cumpleanos`, `cron-notificaciones`). Lee la base de Perfiles Garden en modo solo lectura.
- Otros repos de presentaciones y estadísticas: `agenda-moviles`, `estadisticas-ojos-en-alerta`, `contador-moviles`, `exposicion-*`, `Cordobeses-en-Alerta-Exposici-n*`.

## Diseño (importante)

Todo trabajo nuevo (informes, mapas, infografías) tiene que respetar el estilo de los ya hechos. **Leer `DISENO.md` en esta carpeta antes de producir cualquier informe o gráfico.** Resumen: logo `Logos/iso_blanco.png` (solo sobre fondo oscuro), Georgia para títulos y Segoe UI para el resto, celeste `#1590cf`/`#22a6e4`, informes A4 en variante clara (con fotos, para imprimir) u oscura (operativos y estadísticas), y mapas oscuros con leyenda de referencias.

Para informes o placas **estadísticas del SAE** leer además `ESTADISTICA.md`: allí está la estructura página por página y el estilo exacto de los tableros oscuros.

Para entender **cómo funciona la dependencia** (estructura, glosario, recorrido de un hecho, cifras) leer `FUNCIONAMIENTO.md`. Para hacer **presentaciones o exposiciones** con el mismo estilo, leer `EXPOSICION.md` (datos técnicos) y `PRESENTACIONES.md` (cómo se diseñan y se cuentan: grilla, catálogo de láminas, animaciones, voz).

Para leer la **tabla de hechos del SAE** (problemas del archivo, diccionario, cómo se reconstruyen las cifras de las placas) y para **geolocalizar hechos** (barrio, cuadrante, fuera de cuadrante, DJP, móvil): leer `TABLA_SAE.md` y usar los scripts `leer_tabla_sae.py`, `geolocalizar_sae.py` y `barrios_programa.py`.

## Respaldo (dónde vive cada cosa)

- **Guías y scripts** (los `.md` y los `.py`): repo de GitHub `Emma30h/Contexto-Trabajo-Direcci-n-Monitoreo-Cordobeses-En-Alerta`. Es la versión que manda. Al terminar un cambio en estos archivos, commitear y pushear.
- **Datos de origen** (CSV, PDF, KML, logos, imágenes): carpeta `DMCA Claude` en Google Drive. No van al repo: pesan mucho y tienen datos personales.
- **Para restaurar en una máquina nueva**: clonar el repo en una carpeta llamada `DMCA Claude`, bajar las subcarpetas de datos desde Drive y ponerlas adentro, y en Claude escritorio usar + → Add folder.

## Reglas de trabajo

0. **Mantener el repo al día.** Esta carpeta está versionada en GitHub (`Emma30h/Contexto-Trabajo-Direcci-n-Monitoreo-Cordobeses-En-Alerta`, rama `main`). Cada vez que se cree o se cambie una guía `.md` o un script `.py` de esta carpeta, **commitear y pushear en la misma sesión**, sin esperar a que el usuario lo pida. Es un repo de contexto, no de producción: acá no hace falta rama aparte ni confirmación previa (la regla 2 es para los repos de las aplicaciones). Lo que sí: nunca commitear datos (CSV, PDF, KML, imágenes); el `.gitignore` ya los excluye, no tocarlo. Si al terminar una tarea quedaron cambios sin pushear, avisarlo.
1. Los archivos originales de esta carpeta no se modifican: se trabaja sobre copias y los resultados van en una subcarpeta nueva.
2. Antes de subir cambios a `master` de cualquier repo, confirmar con el usuario. Por defecto: rama aparte y aviso.
3. Datos de personal policial (nombres, DNI, legajos) son sensibles: no copiarlos a otros lados ni publicarlos.
4. Informes: mantener el estilo de los PDF de `Informes/`. Si falta un dato, marcarlo como pendiente en vez de inventarlo.
5. Respuestas breves y directas; el resultado primero, sin recap de pasos.

## Pendiente de completar por el usuario

- Formato exacto y destinatarios de los informes habituales.
- Tareas recurrentes que suelen pedirle (para armar plantillas).
- Cualquier dato de frecuencias, móviles o turnos que convenga tener a mano.
