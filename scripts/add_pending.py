#!/usr/bin/env python3
"""
PAIDEIA - Sistema de Gestión de Tareas Pendientes
=================================================

Este script permite gestionar una lista de tareas pendientes que persiste
entre sesiones de trabajo. Los pendientes se almacenan en CONTEXT_MEMORY.json
y están disponibles para que Claude los lea al iniciar nuevas sesiones.

Arquitectura:
    ┌─────────────────┐      ┌──────────────────────┐
    │  add_pending.py │ ──── │  CONTEXT_MEMORY.json │
    └─────────────────┘      └──────────────────────┘
           │                          │
           │  Operaciones:            │  Estructura:
           │  - Agregar               │  {
           │  - Listar                │    "pendientes": [...]
           │  - Completar             │  }
           │  - Limpiar               │
           └──────────────────────────┘

Comandos disponibles:
    python scripts/add_pending.py "Nueva tarea"     # Agregar pendiente
    python scripts/add_pending.py --list            # Ver todos los pendientes
    python scripts/add_pending.py --done 1          # Marcar #1 como completado
    python scripts/add_pending.py --clear           # Eliminar todos

Ejemplos de uso:
    $ python scripts/add_pending.py "Implementar login con Supabase"
    ✅ Pendiente agregado: Implementar login con Supabase
    📋 Total pendientes: 5

    $ python scripts/add_pending.py --list
    📋 PENDIENTES ACTUALES:
      1. [ ] Implementar login con Supabase
      2. [ ] Crear componente de quiz
    Total: 2

    $ python scripts/add_pending.py --done 1
    ✅ Completado: Implementar login con Supabase
    📋 Pendientes restantes: 1

Integración con otros scripts:
    - sync_context.py: Lee los pendientes para generar AI_CONTEXT.md
    - save_session.py: Puede referenciar pendientes en el resumen

Autor: Sistema PAIDEIA
Versión: 1.0.0
"""

import sys
import json
from pathlib import Path

# Configuración de rutas
ROOT_DIR = Path(__file__).parent.parent
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"


def load_context() -> dict:
    """
    Carga el contexto desde el archivo JSON.

    Returns:
        dict: Contexto con estructura {pendientes, decisiones_clave, sesiones}
              Si el archivo no existe, retorna estructura vacía.

    Example:
        >>> context = load_context()
        >>> print(context['pendientes'])
        ['Tarea 1', 'Tarea 2']
    """
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {"pendientes": [], "decisiones_clave": [], "sesiones": []}


def save_context(context: dict):
    """
    Guarda el contexto actualizado en el archivo JSON.

    Args:
        context: Diccionario con la estructura del contexto.

    Note:
        Crea el directorio padre si no existe.
        Usa UTF-8 para soportar caracteres especiales.
    """
    CONTEXT_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONTEXT_FILE.write_text(
        json.dumps(context, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


def add_pending(task: str):
    """
    Agrega una nueva tarea a la lista de pendientes.

    Args:
        task: Descripción de la tarea pendiente.

    Example:
        >>> add_pending("Crear componente de navegación")
        ✅ Pendiente agregado: Crear componente de navegación
        📋 Total pendientes: 3
    """
    context = load_context()
    if 'pendientes' not in context:
        context['pendientes'] = []
    context['pendientes'].append(task)
    save_context(context)
    print(f"✅ Pendiente agregado: {task}")
    print(f"📋 Total pendientes: {len(context['pendientes'])}")


def list_pending():
    """
    Muestra todos los pendientes actuales con formato numerado.

    Output:
        Lista numerada de pendientes con checkbox [ ] y total.

    Example:
        >>> list_pending()
        📋 PENDIENTES ACTUALES:
          1. [ ] Implementar auth
          2. [ ] Crear componente quiz
        Total: 2
    """
    context = load_context()
    print("\n📋 PENDIENTES ACTUALES:\n")
    pendientes = context.get('pendientes', [])
    for i, task in enumerate(pendientes, 1):
        print(f"  {i}. [ ] {task}")
    if not pendientes:
        print("  (Sin pendientes)")
    print(f"\nTotal: {len(pendientes)}")


def complete_pending(index: int):
    """
    Marca un pendiente como completado y lo elimina de la lista.

    Args:
        index: Número del pendiente (1-based, como se muestra en --list).

    Note:
        El índice es 1-based para coincidir con la visualización.
        Si el índice es inválido, muestra error con el rango válido.

    Example:
        >>> complete_pending(1)
        ✅ Completado: Implementar auth
        📋 Pendientes restantes: 1
    """
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
    """
    Elimina todos los pendientes de la lista.

    Warning:
        Esta acción es irreversible. Todos los pendientes se perderán.

    Example:
        >>> clear_all()
        🗑️ Eliminados 5 pendientes
    """
    context = load_context()
    count = len(context.get('pendientes', []))
    context['pendientes'] = []
    save_context(context)
    print(f"🗑️ Eliminados {count} pendientes")


def main() -> int:
    """
    Punto de entrada principal del script.

    Procesa los argumentos de línea de comandos y ejecuta la acción correspondiente.

    Returns:
        int: Código de salida (0 = éxito, 1 = error/ayuda).

    Comandos:
        (sin args)      Muestra ayuda
        "tarea"         Agrega nuevo pendiente
        --list          Lista todos los pendientes
        --done N        Marca pendiente N como completado
        --clear         Elimina todos los pendientes
    """
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
