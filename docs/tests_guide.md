# Guía de Tests para el Agente RPA Drawio

Esta guía paso a paso te permitirá validar de forma local todo el ciclo de pruebas de tu agente RPA Drawio, facilitando la depuración y asegurando la calidad antes de integrar cambios en el repositorio.

---

## 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas en tu entorno local:

- **Docker:** Para construir y ejecutar la imagen del agente.
- **Python y Pytest:** Para ejecutar los tests unitarios de Python.
- **Bats:** Para ejecutar los tests unitarios en Bash.  
  Revisa la [documentación de Bats](https://github.com/bats-core/bats-core) para su instalación.

---

## 2. Estructura de la Batería de Tests y Archivos Adicionales

El proyecto incorpora tests en tres niveles:

### A. Pruebas Unitarias en Bash (Bats)

- **Archivo:** `tests/shell_tests.bats`  
  Este archivo contiene tests que verifican el correcto funcionamiento de scripts clave (por ejemplo, `create_template.sh`), comprobando que se genere un nuevo archivo basado en la plantilla.

### B. Pruebas Unitarias en Python (Pytest)

- **Archivo:** `tests/test_python.py`  
  Aquí se prueban funcionalidades de los scripts en Python, como:
  - **`convert_to_sarif.py`**: Convierte una salida JSON de ShellCheck a un archivo SARIF válido.
  - **`process_shellcheck.py`**: Genera un reporte HTML a partir del JSON de ShellCheck.

### C. Prueba End-to-End (E2E)

- **Archivo:** `e2e_test.sh`  
  Este script simula el flujo completo del agente:
  1. Prepara el entorno creando el directorio `diagrams` y copiando la plantilla `templates/base.drawio` a `diagrams/test.drawio`.
  2. Ejecuta el contenedor Docker utilizando un pseudo-TTY (con `script` para mantener la opción `-i`) para ejecutar `export_all.sh`.
  3. Verifica que al menos se haya generado un archivo PDF en el directorio `diagrams`.

---

## 3. Pasos para Ejecutar los Tests en Local

### Paso 1: Clonar el Repositorio

Si aún no lo has hecho, clona el repositorio y cambia al directorio del proyecto:

```bash
git clone https://github.com/JSilvaGlez/atlantyde-drawio-agent.git
cd atlantyde-drawio-agent
```

### Paso 2: Ejecutar Pruebas Unitarias en Bash

Utiliza Bats para ejecutar los tests en Bash:

bats tests/shell_tests.bats

Esto ejecutará los tests definidos en tests/shell_tests.bats y mostrará un resumen con el resultado.

### Paso 3: Ejecutar Pruebas Unitarias en Python

Instala Pytest (si aún no lo tienes) y ejecuta los tests de Python:

```bash
pip install pytest
pytest tests/test_python.py
```

Verifica que todas las aserciones pasen correctamente.

### Paso 4: Ejecutar la Prueba End-to-End (E2E)

Dale permisos de ejecución al script y ejecútalo:

```bash
chmod +x e2e_test.sh
./e2e_test.sh
```

El script realizará las siguientes acciones:

    Creará el directorio diagrams y copiará la plantilla templates/base.drawio a diagrams/test.drawio.

    Ejecutará el contenedor Docker con un pseudo-TTY para exportar el diagrama a PDF.

    Verificará la generación de al menos un archivo PDF en el directorio diagrams.

### Paso 5: Verificar Resultados

Para confirmar la salida, revisa el contenido del directorio diagrams:

ls -la diagrams

Asegúrate de que se hayan generado archivos PDF válidos.
## 4. Consejos Adicionales
### Logs y Depuración

    Si algún test falla, revisa la salida de la terminal para identificar qué parte del proceso tuvo problemas.

    Puedes agregar comandos echo adicionales en los scripts para obtener mayor trazabilidad.

### Pruebas en Contenedor y en Local

    Asegúrate de que la ejecución local de los tests y la integración en el pipeline CI (por ejemplo, en GitHub Actions) sean consistentes.

    Ejecuta los pasos localmente antes de integrarlos en el CI para minimizar sorpresas.

### Actualizaciones de Dependencias

    Si algún test falla por versiones de herramientas (Bats, Pytest, etc.), revisa la versión instalada y actualízala según sea necesario.

## 5. Resumen Final

Para validar el ciclo de pruebas del agente RPA Drawio, sigue estos pasos:

    Clona el repositorio y asegúrate de tener Docker, Python, Pytest y Bats instalados.

    Ejecuta los tests unitarios en Bash:

bats tests/shell_tests.bats

Ejecuta los tests unitarios en Python:

pytest tests/test_python.py

Construye la imagen Docker:

docker build -t atlantyde/drawio-agent .

Ejecuta la prueba E2E:

    chmod +x e2e_test.sh
    ./e2e_test.sh

Esta guía te permitirá validar de forma local la integridad y el funcionamiento del agente RPA Drawio, facilitando la depuración y asegurando la calidad del proyecto antes de integrar cambios en el repositorio.
## 6. Documentación y Colaboración

    Documentación Adicional:
    Puedes complementar esta guía utilizando Sphinx o MkDocs para generar documentación web con GitHub Pages.

    Colaboración:
    Antes de enviar Pull Requests, verifica la ejecución local de todos los tests y utiliza esta guía para entender el flujo de pruebas. ¡Contribuye con mejoras y comparte tus resultados!

¡Sigue estos pasos y mantén la robustez del proyecto mientras colaboras en su mejora continua!


---

Con estos dos archivos, dispondrás de una guía completa para MkDocs compatible con GitHub Pages. Una vez que los añadas a tu repositorio, podrás generar la documentación web (por ejemplo, ejecutando `mkdocs build` o `mkdocs serve`) y tener una referencia actualizada y ordenada para la ejecución de tests en el proyecto *atlantyde-drawio-agent*.
