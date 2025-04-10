#!/bin/bash
# e2e_test.sh
# Prueba end-to-end para el agente RPA Drawio.

set -e

echo "Ejecutando pruebas de extremo a extremo..."

# Preparar el entorno: crear el directorio y copiar una plantilla de prueba.
mkdir -p diagrams
cp templates/base.drawio diagrams/test.drawio 2>/dev/null || echo "No se encontró la plantilla base; asegúrate de tener templates/base.drawio."

# Ejecutar el contenedor con pseudo-TTY para exportar el diagrama.
# Se utiliza 'script' para simular un TTY y mantener la opción -i.
script -qfc 'docker run --rm -i -v "$(pwd)/diagrams:/home/drawio/diagrams" atlantyde/drawio-agent export_all.sh' /dev/null

# Verificar que se hayan generado archivos PDF en el directorio "diagrams".
pdf_files=( diagrams/*.pdf )
if [ ! -f "${pdf_files[0]}" ]; then
  echo "Error: No se generaron archivos PDF en el directorio diagrams." >&2
  exit 1
else
  echo "Prueba E2E completada: archivos PDF generados correctamente."
fi

exit 0
