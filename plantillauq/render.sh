#!/usr/bin/env bash
# Renderiza una presentación Marp del curso con el tema `uq` usando las imágenes locales de tema/img
# (no depende de la red, a diferencia de renderizar con el tema publicado en GitHub).
#
# Uso:  tema/render.sh <presentacion.md> [pdf|pptx|html]     (por defecto: pdf)
# Ej.:  tema/render.sh fds2/sesion04/MLOps_I_reproducibilidad_versionado.md
#
# Requiere Marp CLI (https://github.com/marp-team/marp-cli) y, si la presentación tiene diagramas,
# Mermaid CLI (`mmdc`, o la variable MMDC). El PDF queda junto al .md.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Uso: $0 <presentacion.md> [pdf|pptx|html]" >&2
  exit 1
fi

TEMA_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REMOTO="https://raw.githubusercontent.com/christiancandela/plantillas/main/plantillauq/"
ENTRADA="$1"
FORMATO="${2:-pdf}"
DIR="$(cd "$(dirname "$ENTRADA")" && pwd)"
BASE="$(basename "$ENTRADA" .md)"
TMP="$(mktemp -d)"
TEMPORAL="$DIR/.${BASE}.render.md"
trap 'rm -rf "$TMP" "$TEMPORAL"' EXIT

# Tema y presentación con las URL del repositorio de plantillas reemplazadas por las imágenes locales.
sed "s#${REMOTO}#${TEMA_DIR}/img/#g" "$TEMA_DIR/uq.css" > "$TMP/uq.css"
sed "s#${REMOTO}#${TEMA_DIR}/img/#g" "$ENTRADA" > "$TMP/$BASE.md"

# Los diagramas Mermaid se dibujan antes de llamar a Marp (Marp no los conoce) y el SVG queda
# incrustado en la copia temporal: así salen iguales en pdf, pptx y html. El .md original no se toca.
if grep -q -e '<div class="mermaid"' -e '^```mermaid' "$TMP/$BASE.md"; then
  python3 "$TEMA_DIR/mermaid.py" "$TMP/$BASE.md" "$TEMPORAL" "$TMP"
else
  cp "$TMP/$BASE.md" "$TEMPORAL"
fi

# --no-stdin evita que Marp se quede esperando entrada estándar cuando se ejecuta desde scripts.
marp --no-stdin --no-config-file --theme-set "$TMP/uq.css" --html --allow-local-files \
  "$TEMPORAL" -o "$DIR/$BASE.$FORMATO"
echo "✅ $DIR/$BASE.$FORMATO"
