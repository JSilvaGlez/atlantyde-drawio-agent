# 🛡️ Reglas OWASP ZAP para Atlantyde

Este directorio contiene las reglas de escaneo estático y dinámico utilizadas por las acciones de GitHub para validar la seguridad del sitio web generado con MkDocs.

## Archivo `rules.tsv`

Este archivo permite ignorar alertas de seguridad conocidas o no críticas durante el análisis DAST con `zaproxy/action-baseline`.

| Código | Acción  | Justificación                              |
|--------|---------|--------------------------------------------|
| 10015  | IGNORE  | Falta de cabecera Cache-Control            |
| 10020  | IGNORE  | X-Frame-Options no establecida             |
| 10035  | IGNORE  | Contenido mixto en pruebas                 |
| ...    | ...     | ...                                        |

---

## 📣 ¿Cómo colaborar?

Puedes enviar una Pull Request proponiendo reglas nuevas o actualizaciones justificadas. Asegúrate de:

- Especificar el código ZAP
- Indicar claramente la justificación
- Validar que no introduces riesgos para producción

Este archivo es parte del flujo SDLC y QA/UAT del proyecto **Atlantyde Diagram Agent**.
