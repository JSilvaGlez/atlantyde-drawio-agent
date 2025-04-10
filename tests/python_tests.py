import json
import os
import tempfile
import subprocess
import pytest

def test_convert_to_sarif():
    # Crear un dummy de salida JSON de ShellCheck.
    dummy_json = {
        "comments": [
            {
                "file": "test.sh",
                "line": 1,
                "column": 1,
                "message": "Dummy error",
                "code": "SC1001",
                "level": "error"
            }
        ]
    }
    with tempfile.NamedTemporaryFile("w+", delete=False) as temp_json, \
         tempfile.NamedTemporaryFile("w+", delete=False) as temp_sarif:
        json.dump(dummy_json, temp_json)
        temp_json.close()
        # Ejecutar el script de conversión.
        ret = subprocess.run(["python3", "./convert_to_sarif.py", temp_json.name, temp_sarif.name])
        assert ret.returncode == 0
        # Verificar que el archivo SARIF es un JSON válido y contiene la clave "runs".
        with open(temp_sarif.name, "r") as f:
            sarif_data = json.load(f)
        assert "runs" in sarif_data
    os.unlink(temp_json.name)
    os.unlink(temp_sarif.name)

def test_process_shellcheck():
    # Dummy JSON similar al de ShellCheck.
    dummy_json = {
        "comments": [
            {
                "file": "test.sh",
                "line": 1,
                "column": 1,
                "message": "Dummy warning",
                "code": "SC2001",
                "level": "warning"
            }
        ]
    }
    with tempfile.NamedTemporaryFile("w+", delete=False) as temp_json, \
         tempfile.NamedTemporaryFile("w+", suffix=".html", delete=False) as temp_html:
        json.dump(dummy_json, temp_json)
        temp_json.close()
        # Ejecutar el script de generación del reporte HTML.
        ret = subprocess.run(["python3", "./process_shellcheck.py", temp_json.name, temp_html.name])
        assert ret.returncode == 0
        # Comprobar que el HTML generado contiene etiquetas <html>.
        with open(temp_html.name, "r") as f:
            content = f.read()
        assert "<html" in content.lower()
    os.unlink(temp_json.name)
    os.unlink(temp_html.name)
