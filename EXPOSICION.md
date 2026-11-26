# Exposiciones DMCA: diseño y armado

Guía para hacer una exposición **con el mismo estilo** que la presentación general. Contenido y cifras: ver `FUNCIONAMIENTO.md`.

## Dónde está

- Publicada: https://emma30h.github.io/exposicion-general-cordobeses-en-alerta-para-choferes/ (GitHub Pages, se actualiza con cada `git push`). La URL guardada está en `Exposiciones DMCA/URL Diapositivas - Exposicion.txt`.
- Código: repo `Emma30h/exposicion-general-cordobeses-en-alerta-para-choferes` (público). Archivos: `index.html` (las 30 láminas), `guia.html` (guía del público), `config-vivo.js`, `media/`, `print/`, `README.md`, `REUTILIZAR.md`.
- La presentación juntó cuatro anteriores (CeA, 101, Agenda Móvil, División de Frecuencia). Para una exposición nueva, **partir de este repo** (`REUTILIZAR.md` lista las piezas reutilizables).
- El repo de GitHub no tiene push configurado en esta sesión: para cambiarlo hay que adjuntarlo con permiso de escritura.

## Copia de respaldo (sin conexión)

`Exposiciones DMCA/Presentacion Cordobeses en Alerta - copia sin conexion.html`: un solo archivo HTML (≈12 MB) con las 30 láminas, imágenes, videos, tipografías, mapa e instructivo PDF **incluidos**; se abre con doble clic en cualquier navegador, sin internet. Se hizo el 26/11/2026 desde el repo publicado. Diferencia: no tiene la guía en vivo para celulares ni el QR (necesitan internet). Si la exposición se actualiza, hay que regenerar la copia.

## Formato

- Un solo `index.html` autocontenido, láminas de **1600 × 900** que escalan a la pantalla. Navegación con ← →, **F** pantalla completa, **R** repite las animaciones, **G** guía en vivo.
- **Guía en vivo**: el celular del público sigue la exposición vía Supabase Realtime (canal firmado). Hay que reactivar el proyecto de Supabase (plan gratis, se pausa tras ~7 días) antes de exponer. La contraseña está en el `README.md` del repo: no copiarla a otros lados.
- Si se cambian las láminas, subir la constante `VER` en `index.html` y `guia.html` (deben coincidir).
- **PDF**: `print/presentacion.html` junta capturas de 1600×900 de `print/laminas/` (se sacan con Chrome desde el sitio publicado) en un PDF de una lámina por página. Afiche A4 con QR: `print/afiche-qr.html`.
- Vercel quedó pausado por límite de uso hasta el 18/12/2026; la versión vigente es la de GitHub Pages.

## Estilo visual

- **Tema oscuro**. Variables CSS del archivo:
  - Fondo `--bg #0a1219`, paneles `--panel #101c26` y `--panel-2 #152330`, líneas `--line #22343f`.
  - Texto `--fg #e8eef2`, secundario `--muted #93a6b4`, tenue `--faint #5f7484`.
  - Marca (celeste) `--brand #42ade8`, señal (ámbar) `--signal #e2a23b`, ok (verde) `--ok #3fbf6a`.
  - Colores de las 8 frecuencias: F1 `#3276c7`, F2 `#79a8de`, F3 `#ac7505`, F4 `#cfa952`, F5 `#b74873`, F6 `#d087a6`, F7 `#1c9144`, F8 `#8564c3`. Los mismos del mapa `Frecuencia RugGear`.
- **Tipografías** (Google Fonts): títulos y cifras en **Barlow Condensed** (500–700), texto en **Barlow**, etiquetas y fuentes en **JetBrains Mono**, y Roboto para las réplicas de pantallas.
- **Portada**: foto de fondo de la sala (oscurecida) con título grande `DIRECCIÓN MONITOREO` en blanco y `CORDOBESES EN ALERTA` en celeste, bajada, `CÓRDOBA CAPITAL · NOVIEMBRE 2026`, y un recuadro con **QR** "Seguí la exposición en tu celular".
- **Lámina tipo**: arriba a la izquierda un **kicker** en celeste, mono y mayúsculas (ej. `ESTRUCTURA`); título grande en Barlow Condensed; arriba a la derecha la **etiqueta de sección** (`.sec-tag`, ej. `01 · QUIÉNES SOMOS`); al pie, a la izquierda, la **fuente** en mono chico (ej. `Fuente: base del SAE, sucesos del 1/10/2025 al 30/9/2026`).
- **Secciones numeradas**: 01 Quiénes somos · 02 Cómo trabajamos · 03 División de frecuencia · 04 En la calle · 05 El 101 en el 911 · 06 Control e información · 07 Resultados y equipo.
- **Componentes**:
  - Tarjetas de cifra: número grande celeste + etiqueta gris (ej. `198.613 vecinos adheridos`).
  - Pasos numerados `01 … 07` con ícono circular y rol en mono al pie.
  - Cadenas de flujo con flechas `→` entre "píldoras".
  - Tarjetas con borde izquierdo de color (celeste, ámbar) para definiciones y avisos.
  - Organigrama con tarjetas conectadas y gráfico de barra apilada por tipo de personal (civil celeste, técnico ámbar, policial verde).
  - Barras horizontales de proporción (ej. subtipos por agencia 44 / 24 / 16 / 4).
  - Tablas simples de turnos.
  - Imagen del RugGear (`media/ruggear-crop.png`) con la aplicación en modo oscuro, y réplicas de pantallas del SAE WEB marcadas "caso ficticio con fines de capacitación".
  - Videos cortos en bucle de las cabinas (`media/video/`), y animaciones paso a paso del personal tech (motor `makeDev` / `DEMOS`, tecla R).
- **Cierre**: "¡Muchas gracias!" con 4 cifras (vecinos, barrios, puertas de entrada, 24/7) y botón para descargar el instructivo.
- Redacción: tono directo y didáctico, pensado para **civiles becarios que van a ser choferes de móviles**. Frases cortas, lenguaje de calle, todo en presente, "Hs" para horas.

## Cómo hacer una exposición nueva (para Claude)

1. Partir del repo (clonar) y duplicar `index.html`; conservar `<style>`, el motor de navegación y la guía en vivo; reemplazar láminas.
2. Respetar el tema oscuro, las variables y las tipografías de arriba; usar el logo `Logos/iso_blanco.png` (o `media/logo_ojo.png` del repo).
3. Pedir al usuario los datos y la fecha de corte de cada cifra; poner siempre la **fuente** al pie. No inventar números.
4. Revisar en pantalla cada lámina (1600×900) y exportar el PDF con el procedimiento de `print/`.
5. Confirmar con el usuario antes de hacer `git push` (publica la presentación).
