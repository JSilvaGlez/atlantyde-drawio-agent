#!/usr/bin/env python3
import json
import sys

def convert_to_sarif(shellcheck_json_file, output_file):
    with open(shellcheck_json_file, 'r') as f:
        data = json.load(f)

    # La salida de ShellCheck puede ser una lista o un objeto con clave "comments"
    if isinstance(data, list):
        comments = data
    else:
        comments = data.get("comments", [])

    results = []
    for comment in comments:
        file_path = comment.get("file", "")
        line = comment.get("line", 1)
        column = comment.get("column", 1)
        message = comment.get("message", "")
        rule_id = str(comment.get("code", ""))
        level = comment.get("level", "warning")

        # Mapeo de niveles a los estándares SARIF:
        # error -> error, warning -> warning, info -> note (o cualquier otro valor se puede considerar "note")
        if level.lower() == "error":
            severity = "error"
        elif level.lower() == "warning":
            severity = "warning"
        else:
            severity = "note"

        result_obj = {
            "ruleId": rule_id,
            "level": severity,
            "message": {
                "text": message
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": file_path
                        },
                        "region": {
                            "startLine": line,
                            "startColumn": column
                        }
                    }
                }
            ]
        }
        results.append(result_obj)

    # Construcción del objeto SARIF
    sarif_output = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "ShellCheck",
                        "informationUri": "https://www.shellcheck.net/",
                        "rules": []  # Opcional: se pueden agregar reglas únicas detectadas
                    }
                },
                "results": results
            }
        ]
    }

    with open(output_file, 'w') as f:
        json.dump(sarif_output, f, indent=2)
    print(f"SARIF generado correctamente en {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 convert_to_sarif.py <input_shellcheck.json> <output.sarif>")
        sys.exit(1)
    convert_to_sarif(sys.argv[1], sys.argv[2])
