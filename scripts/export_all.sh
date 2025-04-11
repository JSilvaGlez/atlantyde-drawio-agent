#!/bin/bash
# export_all.sh
# Exporta todos los archivos .drawio en el directorio /home/drawio/diagrams a formato PDF.

set -e

DIAGRAMS_DIR="/home/drawio/diagrams"

if [ ! -d "$DIAGRAMS_DIR" ]; then
  echo "El directorio $DIAGRAMS_DIR no existe. Saliendo..."
  exit 1
fi

# Obtener la lista de archivos .drawio
files=( "$DIAGRAMS_DIR"/*.drawio )
if [ ${#files[@]} -eq 0 ] || [ ! -f "${files[0]}" ]; then
  echo "No se encontraron archivos .drawio en $DIAGRAMS_DIR"
  exit 0
fi

# Recorrer todos los archivos .drawio y exportarlos a PDF.
for file in "${files[@]}"; do
  output_pdf="${file%.drawio}.pdf"
  echo "Exportando $file a $output_pdf..."

  if ! drawio --export --format pdf --output "$output_pdf" "$file"; then
    echo "❌ Error al exportar $file" >&2
  else
    echo "✅ Exportado exitosamente: $output_pdf"
  fi
done
echo "Todos los archivos .drawio han sido exportados a PDF."
echo "Exportación completa."
exit 0
# This script exports all .drawio files in the specified directory to PDF format.