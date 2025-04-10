#!/usr/bin/env bats
# tests/shell_tests.bats
# Test unitarios para scripts de shell (ejemplo: create_template.sh).

setup() {
  # Crear un entorno de prueba aislado
  mkdir -p test_env/diagrams
  # Copiar la plantilla de ejemplo al entorno de prueba.
  cp templates/base.drawio test_env/diagrams/ 2>/dev/null || echo "Aviso: No se encontró templates/base.drawio; asegúrate de tener la plantilla."
}

teardown() {
  rm -rf test_env
}

@test "create_template.sh genera un nuevo archivo basado en la plantilla" {
  run ./create_template.sh test_env/diagrams
  [ "$status" -eq 0 ]
  # Buscar un archivo cuyo nombre contenga la fecha actual y que termine en _new.drawio.
  output_file=$(find test_env/diagrams -type f -name "$(date +%Y%m%d)*_new.drawio")
  [ -n "$output_file" ]
}
