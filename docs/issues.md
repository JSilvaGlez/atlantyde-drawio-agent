# 🐛 Issues Técnicos y de Mejora (Generados Dinámicamente)

_Última actualización: 2025-04-11 01:00:33 UTC_

| ID | Título | Tipo | Estado |
|----|--------|------|--------|
| 1 | Integrar verificación automática de cambios en 'mkdocs.yml' y carpeta 'docs/' | Mejora CI/CD | Abierto |
| 2 | Corregir warnings ShellCheck en scripts de exportación | Calidad Código / Scripting | En progreso |
| 3 | Unificar instalación de dependencias con `setup-python-cached` | Optimización CI | Pendiente |
| 4 | Problemas con descarga de artefactos: flag `--output` inválido | Fix técnico / GH CLI | Urgente |
| 5 | Mejorar validación QA/UAT en workflows para extracción dinámica | QA/UAT Automation | En progreso |
| 6 | Renderizar visualmente los reportes de ZAP DAST en MkDocs | Seguridad / Visualización | Pendiente |
| 7 | Crear sección dinámica 'Colabora' en documentación MkDocs | Comunidad / Docs | Abierto |
| 8 | Refactorizar README.md para añadir resumen gamificado y visual | UX / Documentación | En progreso |

---

## Detalles

### 1. Integrar verificación automática de cambios en 'mkdocs.yml' y carpeta 'docs/'
**Tipo:** _Mejora CI/CD_  
**Estado:** _Abierto_  

El flujo de despliegue actual se basa en una variable de entorno 'deploy_required', que a veces genera advertencias. Se sugiere extraer esta lógica a un script Python externo para mayor robustez y trazabilidad.

### 2. Corregir warnings ShellCheck en scripts de exportación
**Tipo:** _Calidad Código / Scripting_  
**Estado:** _En progreso_  

El script `export_all.sh` debe refactorizar la comprobación de salida con `if ! comando; then` en lugar de `if [ $? -ne 0 ];` para cumplir con buenas prácticas.

### 3. Unificar instalación de dependencias con `setup-python-cached`
**Tipo:** _Optimización CI_  
**Estado:** _Pendiente_  

Varios workflows instalan dependencias de forma redundante. Consolidar la instalación usando el action `setup-python-cached` y `requirements.txt` para ahorro energético.

### 4. Problemas con descarga de artefactos: flag `--output` inválido
**Tipo:** _Fix técnico / GH CLI_  
**Estado:** _Urgente_  

El uso de `gh api ... --output` no es compatible en runners actuales. Sustituir por redirección con `> archivo.zip` o usar `gh release download` si aplica.

### 5. Mejorar validación QA/UAT en workflows para extracción dinámica
**Tipo:** _QA/UAT Automation_  
**Estado:** _En progreso_  

Asegurar que todos los tests de contenido y accesibilidad QA/UAT usen navegadores headless vía Playwright correctamente configurado y con fallback en errores de instalación.

### 6. Renderizar visualmente los reportes de ZAP DAST en MkDocs
**Tipo:** _Seguridad / Visualización_  
**Estado:** _Pendiente_  

Mover `report_md.md` a `docs/security/zap-report.md` y añadir sección permanente en el menú de navegación MkDocs para visualizarlo.

### 7. Crear sección dinámica 'Colabora' en documentación MkDocs
**Tipo:** _Comunidad / Docs_  
**Estado:** _Abierto_  

Agregar contenido desde `CONTRIBUTING.md` y permitir que esta crezca automáticamente con nuevas contribuciones mediante PRs.

### 8. Refactorizar README.md para añadir resumen gamificado y visual
**Tipo:** _UX / Documentación_  
**Estado:** _En progreso_  

Incluir nuevas secciones con navegación rápida, integración visual y enlaces a reportes de calidad y documentación automatizada.

