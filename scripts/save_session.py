#!/usr/bin/env python3
"""
PAIDEIA - Script para guardar contexto de sesión.
Guarda un resumen de lo trabajado para referencia futura.

Ejecutar: python scripts/save_session.py "Descripción de lo hecho"
"""

import sys
import json
import datetime
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
SESSION_LOG = ROOT_DIR / "10000_CONTROL" / "SESSION_LOG.md"
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"


def load_context() -> dict:
    """Carga contexto existente o crea uno nuevo."""
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {
        "proyecto": "PAIDEIA",
        "sesiones": [],
        "decisiones_clave": [],
        "pendientes": [],
        "archivos_importantes": [],
        "stack_actual": "Next.js + Supabase + Vercel"
    }


def save_context(context: dict):
    """Guarda el contexto actualizado."""
    CONTEXT_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONTEXT_FILE.write_text(
        json.dumps(context, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


def get_modified_files() -> str:
    """Obtiene archivos modificados desde último commit."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~1'],
            capture_output=True, text=True, cwd=ROOT_DIR
        )
        return result.stdout.strip() or "(sin cambios)"
    except:
        return "(no disponible)"


def append_session_log(resumen: str):
    """Agrega entrada al log de sesiones."""
    now = datetime.datetime.now()
    entry = f"""
## 📅 Sesión {now.strftime('%Y-%m-%d %H:%M')}

### Resumen
{resumen}

### Archivos Modificados
```
{get_modified_files()}
```

---
"""

    SESSION_LOG.parent.mkdir(parents=True, exist_ok=True)

    if SESSION_LOG.exists():
        content = SESSION_LOG.read_text(encoding='utf-8')
    else:
        content = "# 📋 LOG DE SESIONES - PAIDEIA\n\n"

    content += entry
    SESSION_LOG.write_text(content, encoding='utf-8')


def main():
    if len(sys.argv) < 2:
        print("Uso: python save_session.py 'Descripción de lo trabajado'")
        print("Ejemplo: python save_session.py 'Documenté el stack Next.js + Supabase'")
        return 1

    resumen = ' '.join(sys.argv[1:])

    print("🔄 PAIDEIA: Guardando contexto de sesión...")

    # Actualizar contexto JSON
    context = load_context()
    context['sesiones'].append({
        'fecha': datetime.datetime.now().isoformat(),
        'resumen': resumen
    })
    # Mantener solo últimas 20 sesiones
    context['sesiones'] = context['sesiones'][-20:]
    save_context(context)

    # Actualizar log markdown
    append_session_log(resumen)

    print(f"✅ Sesión guardada: {resumen[:50]}...")
    print(f"📄 Log: {SESSION_LOG}")
    print(f"📄 Context: {CONTEXT_FILE}")

    return 0


if __name__ == '__main__':
    exit(main())
