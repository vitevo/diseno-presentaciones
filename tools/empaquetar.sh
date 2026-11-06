#!/usr/bin/env bash
# Genera dist/diseno-presentaciones.skill (zip con la carpeta del skill en la raíz)
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/diseno-presentaciones.skill
(cd skills && zip -rq ../dist/diseno-presentaciones.skill diseno-presentaciones -x '*/__pycache__/*' '*.pyc' '*.DS_Store')
echo "Creado: dist/diseno-presentaciones.skill"
