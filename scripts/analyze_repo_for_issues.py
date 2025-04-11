#!/usr/bin/env python3
"""
Analiza el repositorio y genera un listado preliminar de posibles issues técnicas y de documentación
basadas en palabras clave dentro de los archivos fuente y Markdown.

Resultado: docs/issues.md (listado dinámico de tareas sugeridas).
"""

import os
import re
from pathlib import Path

KEYWORDS = [
    r"#\s?TODO\b", r"#\s?FIXME\b", r"//\s?TODO\b", r"//\s?FIXME\b",
    r"<!--\s?TODO\b", r"<!--\s?FIXME\b", r"\bWIP\b", r"\bREVIEW\b", r"\bPENDING\b"
]
EXCLUDED_DIRS = {'.git', 'venv', '__pycache__', 'node_modules', '.github'}
OUTPUT_FILE = Path("docs/issues.md")

def find_matches_in_file(filepath, keywords):
    matches = []
    try:
        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            for kw in keywords:
                if re.search(kw, line, re.IGNORECASE):
                    matches.append((i, line.strip()))
    except Exception as e:
        print(f"⚠️ Error leyendo {filepath}: {e}")
    return matches

def scan_repo():
    issues = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for file in files:
            if file.endswith(('.py', '.sh', '.md', '.yml', '.yaml')):
                full_path = Path(root) / file
                matches = find_matches_in_file(full_path, KEYWORDS)
                if matches:
                    issues.append((str(full_path), matches))
    return issues

def generate_issue_md(issues):
    lines = [
        "# 📋 Issues detectadas automáticamente",
        "",
        "Este archivo enumera posibles mejoras detectadas de forma automática en el repositorio, a partir de comentarios y palabras clave comunes.",
        "",
        "---"
    ]

    for filepath, occurrences in issues:
        lines.append(f"## 📁 {filepath}")
        for lineno, content in occurrences:
            lines.append(f"- [ ] L{lineno}: `{content}`")
        lines.append("")

    if not issues:
        lines.append("✅ ¡No se detectaron tareas pendientes mediante análisis estático!")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding='utf-8')
    print(f"✅ Archivo generado: {OUTPUT_FILE}")

if __name__ == "__main__":
    issues = scan_repo()
    generate_issue_md(issues)
