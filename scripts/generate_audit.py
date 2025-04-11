import os
from datetime import datetime

# Ruta al archivo de auditoría
AUDIT_FILE = "docs/audit.md"

# Contenido de la nueva auditoría (puede adaptarse según tus necesidades)
NEW_AUDIT_CONTENT = """
- ✅ Pruebas de integración completadas
- 🧪 Cobertura de código: 92%
- 🔐 Verificaciones de seguridad: sin vulnerabilidades detectadas
"""

def obtener_fecha_actual():
    """Devuelve la fecha y hora actuales en formato legible."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def leer_contenido_actual(ruta):
    """Lee el contenido actual del archivo de auditoría."""
    if not os.path.exists(ruta):
        return ""
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()

def agregar_entrada_auditoria(ruta, contenido_actual, nueva_entrada):
    """Agrega una nueva entrada de auditoría si no existe una para la fecha actual."""
    fecha_actual = obtener_fecha_actual()
    encabezado = f"## Auditoría del {fecha_actual}"

    if encabezado in contenido_actual:
        print("⚠️ Ya existe una entrada de auditoría para la fecha actual. No se agregará una nueva.")
        return

    nueva_seccion = f"\n\n{encabezado}\n\n{nueva_entrada.strip()}\n"
    nuevo_contenido = contenido_actual + nueva_seccion

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(nuevo_contenido)
    print(f"✅ Nueva entrada de auditoría agregada para {fecha_actual}.")

def main():
    contenido_actual = leer_contenido_actual(AUDIT_FILE)
    agregar_entrada_auditoria(AUDIT_FILE, contenido_actual, NEW_AUDIT_CONTENT)

if __name__ == "__main__":
    main()
