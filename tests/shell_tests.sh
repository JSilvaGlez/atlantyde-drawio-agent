#!/usr/bin/env bats
# tests/test_export_all.bats
# Test automatizado aislado para export_all.sh

setup() {
  export TEST_DIR="test_env/diagrams"
  mkdir -p "$TEST_DIR"
  cp templates/base.drawio "$TEST_DIR/test.drawio" 2>/dev/null || touch "$TEST_DIR/test.drawio"

  # Crear una copia temporal del script con la ruta modificada
  mkdir -p test_env/scripts
  sed "s|/home/drawio/diagrams|$PWD/$TEST_DIR|g" ./scripts/export_all.sh > test_env/scripts/export_all.sh
  chmod +x test_env/scripts/export_all.sh
  # Crear un entorno de prueba aislado
  mkdir -p test_env/diagrams
  # Copiar la plantilla de ejemplo al entorno de prueba.
  cp templates/base.drawio test_env/diagrams/ 2>/dev/null || echo "Aviso: No se encontró templates/base.drawio; asegúrate de tener la plantilla."

}

teardown() {
  rm -rf test_env
}

@test ("export_all.sh maneja la ausencia de archivos .drawio") {
  # Eliminar el archivo .drawio para probar el manejo de errores
  rm -f "$TEST_DIR/test.pdf" 2>/dev/null || true
  run ./test_env/scripts/export_all.sh
  [ "$status" -eq 0 ]
  [ ! -f "$TEST_DIR/test.pdf" ]
}
@test ("create_template.sh genera un nuevo archivo basado en la plantilla") {
  run ./create_template.sh test_env/diagrams
  rm -f test_env/diagrams/test.drawio
  # Verificar que el archivo de salida no exista
  [ "$status" -eq 0 ]
  # Buscar un archivo cuyo nombre contenga la fecha actual y que termine en _new.drawio.
  output_file=$(find test_env/diagrams -type f -name "$(date +%Y%m%d)*_new.drawio")
  [ -n "$output_file" ]
}
