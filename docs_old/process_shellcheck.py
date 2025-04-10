#!/usr/bin/env python3
import json
import sys
import datetime
from jinja2 import Template

def process_shellcheck(shellcheck_json_file, output_html_file):
    # Cargar datos de ShellCheck
    with open(shellcheck_json_file, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        comments = data
    else:
        comments = data.get("comments", [])
    
    # Calcular resumen por nivel (error, warning, info, etc.)
    summary = {}
    for comment in comments:
        level = comment.get("level", "unknown")
        summary[level] = summary.get(level, 0) + 1

    # Plantilla HTML simple (puedes personalizarla a tu gusto)
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte de Análisis ShellCheck</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            h1, h2 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Reporte de Análisis ShellCheck</h1>
        <p>Fecha de generación: {{ date }}</p>
        <h2>Resumen de incidencias por nivel</h2>
        <ul>
        {% for level, count in summary.items() %}
            <li><strong>{{ level }}</strong>: {{ count }}</li>
        {% endfor %}
        </ul>
        <h2>Detalles de incidencias</h2>
        <table>
            <tr>
                <th>Archivo</th>
                <th>Línea</th>
                <th>Nivel</th>
                <th>Código</th>
                <th>Mensaje</th>
            </tr>
            {% for item in comments %}
            <tr>
                <td>{{ item.file }}</td>
                <td>{{ item.line }}</td>
                <td>{{ item.level }}</td>
                <td>{{ item.code }}</td>
                <td>{{ item.message }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    template = Template(html_template)
    rendered_html = template.render(
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        summary=summary,
        comments=comments
    )

    with open(output_html_file, 'w') as f:
        f.write(rendered_html)
    print(f"Reporte HTML generado correctamente en {output_html_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 process_shellcheck.py <input_shellcheck.json> <output.html>")
        sys.exit(1)
    process_shellcheck(sys.argv[1], sys.argv[2])
