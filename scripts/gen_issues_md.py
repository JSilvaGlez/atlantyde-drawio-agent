#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Atlantyde Diagram Agent — Generador dinámico de documentación de issues
# © 2025 Atlantyde Org — Licencia GPLv3
# Cumple con prácticas recomendadas para trazabilidad CI/CD y documentación viva
# Contacto: compliance@atlantyde.org | Contribuciones: CONTRIBUTING.md

from datetime import datetime

issues = [
    {
        "id": 1,
        "title": "Integrar verificación automática de cambios en 'mkdocs.yml' y carpeta 'docs/'",
        "type": "Mejora CI/CD",
        "status": "Abierto"
    },
    {
        "id": 2,
        "title": "Corregir warnings ShellCheck en scripts de exportación",
        "type": "Calidad Código / Scripting",
        "status": "En progreso"
    },
    # ... más issues desde fuentes externas, PR o IA
]

print("# 🐛 Issues Técnicos y de Mejora (Generados Dinámicamente)\n")

for i in issues:
    print(f"## {i['id']}. {i['title']}\n")
    print(f"**Tipo:** _{i['type']}_  ")
    print(f"**Estado:** _{i['status']}_\n")

print("---")
print(f"**Última actualización:** {datetime.utcnow().isoformat()} UTC\n")
print("**Generado automáticamente por el script `gen_issues_md.py`**")
print("**Atlantyde Org**")
print("**Contribuciones y mejoras son bienvenidas**")