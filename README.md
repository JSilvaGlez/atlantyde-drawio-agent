# 🌊 Atlantyde Diagram Agent

> Automatiza. Documenta. Visualiza.  
> Transforma procesos complejos en claridad visual con DrawIO + RPA + CI/CD.

---

## 🧠 ¿Qué es esto?

**Atlantyde Diagram Agent** es una iniciativa de innovación abierta que combina:

- 🎨 Generación visual de diagramas DrawIO
- 🤖 Agentes RPA para automatización
- 🛠 CI/CD con análisis estático (CodeQL, ShellCheck)
- 🧩 Documentación modular con MkDocs

Todo ello orientado a transformar procesos técnicos, legales y sociales en estructuras **entendibles, reproducibles y colaborativas**.

---

## 🚀 Empieza aquí

| Sección | Descripción |
|--------|-------------|
| [Guía Rápida](getting-started/quick-start/) | Empieza en minutos con tu entorno |
| [Guía de Usuario](user-guide/user-guide-overview/) | Aprende cómo aprovechar todo el potencial |
| [CI/CD](ci-cd/) | Pipeline automatizado y análisis de código |
| [Seguridad](security/) | Cumplimiento SDLC y buenas prácticas |
| [Mapa del Sitio](sitemap.md) | Visión general de toda la documentación |
| [Contribuir](contributing.md) | ¿Te unes al viaje? |

---

## 🌍 Filosofía Atlantyde

Creamos tecnología con propósito, documentación con alma, y automatización con impacto social.  
Tu colaboración es bienvenida. Aquí no solo documentamos: **evolucionamos juntos**.

---

## 🔁 Automatización CI/CD Inteligente

Atlantyde Diagram Agent implementa flujos CI/CD optimizados:

- ✅ Reutilización de entornos Python y dependencias
- ♻️ Instalación con cache para ahorro energético
- 🧠 Validaciones QA/UAT y extracción de contenidos dinámicos
- 📄 Actualización automática del sitemap tras PRs exitosos

> Toda mejora CI/CD contribuye al bienestar digital colectivo y reduce la huella energética de cada cambio.

---

## 👥 🤝 Cómo Contribuir CI/CD

    Sigue la guía de contribución

    Todos los archivos en docs/ son auditados automáticamente

    Usa scripts/gen_issues_md.py para generar la sección de Issues Técnicos

    PRs que modifican scripts/docs se validan vía GitHub Actions

### 🧪 Validaciones Automatizadas (CI/CD)
    
    Proceso	Estado	Frecuencia
    generate-issues.yml	Automático vía push/PR	main
    generate-audit.yml	Cron diario (03:00 UTC) o manual	Programado

    Scripts relevantes:

        - scripts/gen_issues_md.py

        - scripts/gen_audit_md.py

### 🔍  Auditoría y Compliance

        - Estándares: ISO/IEC 27001, OWASP ASVS L2

        - Visualización segura: integración con DrawIO, ShellCheck y ZAP

        - Historial de cambios en docs/audit.md

        - Validaciones SARIF y CSP en workflows

### 📂 Estructura del Proyecto

```
    .
    ├── docs/
    │   ├── index.md
    │   ├── issues.md (dinámico)
    │   ├── audit.md (dinámico)
    │   ├── contributing.md
    │   └── ...
    ├── scripts/
    │   ├── gen_issues_md.py
    │   └── gen_audit_md.py
    ├── .github/
    │   └── workflows/
    │       ├── generate-issues.yml
    │       └── generate-audit.yml
    ├── mkdocs.yml
    └── requirements.txt
```

¿Tienes experiencia en automatización, rendimiento o accesibilidad?  
Consulta nuestras [plantillas de Pull Requests](.github/PULL_REQUEST_TEMPLATE) y mejora la infraestructura de pruebas y despliegue para todos.

📫 ¿Quieres colaborar? Haz un [Pull Request](https://github.com/JSilvaGlez/atlantyde-drawio-agent/pulls) o abre una [Issue](https://github.com/JSilvaGlez/atlantyde-drawio-agent/issues).

Atlantyde © 2025 • Software libre para una documentación poderosa y auditable.

