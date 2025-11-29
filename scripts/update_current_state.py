#!/usr/bin/env python3
"""
PAIDEIA - Script de Auto-actualización de timestamp en CURRENT_STATE.md
Actualiza la fecha de última modificación automáticamente.

Ejecutar: python scripts/update_current_state.py
"""

import re
import datetime
from pathlib import Path

# Configuración
ROOT_DIR = Path(__file__).parent.parent
CURRENT_STATE_FILE = ROOT_DIR / "10000_CONTROL" / "CURRENT_STATE.md"


def update_timestamp():
    """Actualiza el timestamp en CURRENT_STATE.md."""

    if not CURRENT_STATE_FILE.exists():
        print(f"⚠️ Archivo no encontrado: {CURRENT_STATE_FILE}")
        return 1

    # Leer contenido actual
    content = CURRENT_STATE_FILE.read_text(encoding='utf-8')

    # Nuevo timestamp
    now = datetime.datetime.now()
    new_timestamp = now.strftime('%Y-%m-%d')

    # Patrones a actualizar
    patterns = [
        (r'\*\*Última Actualización\*\*: \d{4}-\d{2}-\d{2}',
         f'**Última Actualización**: {new_timestamp}'),
        (r'\*\*Actualizado\*\*: \d{4}-\d{2}-\d{2}',
         f'**Actualizado**: {new_timestamp}'),
    ]

    updated = False
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            updated = True

    if updated:
        # Escribir contenido actualizado
        CURRENT_STATE_FILE.write_text(content, encoding='utf-8')
        print(f"✅ CURRENT_STATE.md actualizado: {new_timestamp}")
    else:
        print("ℹ️ No se encontraron timestamps para actualizar")

    return 0


def main():
    """Función principal."""
    print("🔄 PAIDEIA: Actualizando timestamp...")
    return update_timestamp()


if __name__ == '__main__':
    exit(main())
