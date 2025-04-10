#!/bin/bash
# create_template.sh
# Crea un nuevo archivo de diagrama basado en la plantilla base.

set -e

# Ruta donde se encuentra la plantilla (modifícala si es necesario)
TEMPLATE_SOURCE="/home/drawio/templates/base.drawio"

# Directorio destino, se puede pasar como argumento; por defecto "diagrams"
TARGET_DIR="${1:-diagrams}"
TARGET_FILE="$TARGET_DIR/$(date +%Y%m%d_%H%M%S)_new.drawio"

# Crear el directorio destino si no existe.
if [ ! -d "$TARGET_DIR" ]; then
  echo "Creando directorio $TARGET_DIR..."
  mkdir -p "$TARGET_DIR"
fi

# Verificar que la plantilla existe.
if [ ! -f "$TEMPLATE_SOURCE" ]; then
  echo "Error: No se encontró la plantilla base en $TEMPLATE_SOURCE"
  exit 1
fi

# Copiar la plantilla al destino.
echo "Copiando plantilla a $TARGET_FILE..."
cp "$TEMPLATE_SOURCE" "$TARGET_FILE"
echo "Template creado exitosamente: $TARGET_FILE"
