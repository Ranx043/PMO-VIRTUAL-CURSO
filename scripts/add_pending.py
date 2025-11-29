#!/usr/bin/env python3
"""
PAIDEIA - Script para agregar tareas pendientes.

Ejecutar: python scripts/add_pending.py "Tarea pendiente"
"""

import sys
import json
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"


def load_context() -> dict:
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {"pendientes": [], "decisiones_clave": [], "sesiones": []}


def save_context(context: dict):
    CONTEXT_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONTEXT_FILE.write_text(
        json.dumps(context, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


def add_pending(task: str):
    context = load_context()
    if 'pendientes' not in context:
        context['pendientes'] = []
    context['pendientes'].append(task)
    save_context(context)
    print(f"✅ Pendiente agregado: {task}")
    print(f"📋 Total pendientes: {len(context['pendientes'])}")


def list_pending():
    context = load_context()
    print("\n📋 PENDIENTES ACTUALES:\n")
    pendientes = context.get('pendientes', [])
    for i, task in enumerate(pendientes, 1):
        print(f"  {i}. [ ] {task}")
    if not pendientes:
        print("  (Sin pendientes)")
    print(f"\nTotal: {len(pendientes)}")


def complete_pending(index: int):
    context = load_context()
    pendientes = context.get('pendientes', [])
    if 0 < index <= len(pendientes):
        removed = pendientes.pop(index - 1)
        context['pendientes'] = pendientes
        save_context(context)
        print(f"✅ Completado: {removed}")
        print(f"📋 Pendientes restantes: {len(pendientes)}")
    else:
        print(f"❌ Índice inválido: {index}")
        print(f"   Rango válido: 1-{len(pendientes)}")


def clear_all():
    context = load_context()
    count = len(context.get('pendientes', []))
    context['pendientes'] = []
    save_context(context)
    print(f"🗑️ Eliminados {count} pendientes")


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python add_pending.py 'Nueva tarea'     - Agregar pendiente")
        print("  python add_pending.py --list            - Ver pendientes")
        print("  python add_pending.py --done 1          - Marcar #1 como completado")
        print("  python add_pending.py --clear           - Eliminar todos")
        print("")
        print("Ejemplo: python add_pending.py 'Actualizar sprints para nuevo stack'")
        return 1

    if sys.argv[1] == '--list':
        list_pending()
    elif sys.argv[1] == '--done' and len(sys.argv) > 2:
        try:
            complete_pending(int(sys.argv[2]))
        except ValueError:
            print(f"❌ '{sys.argv[2]}' no es un número válido")
    elif sys.argv[1] == '--clear':
        clear_all()
    else:
        task = ' '.join(sys.argv[1:])
        add_pending(task)

    return 0


if __name__ == '__main__':
    exit(main())
