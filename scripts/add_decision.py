#!/usr/bin/env python3
"""
PAIDEIA - Sistema de Registro de Decisiones Arquitectónicas
===========================================================

Este script permite registrar y consultar decisiones importantes tomadas
durante el desarrollo del proyecto PAIDEIA. Las decisiones se almacenan
en dos formatos:

1. JSON (CONTEXT_MEMORY.json): Para consumo programático por otros scripts
2. Markdown (DECISIONS.md): Para lectura humana y documentación

Arquitectura:
    ┌──────────────────┐
    │  add_decision.py │
    └────────┬─────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
┌──────────────┐  ┌──────────────┐
│ CONTEXT_     │  │ DECISIONS.md │
│ MEMORY.json  │  │ (Historial)  │
└──────────────┘  └──────────────┘

Propósito:
    - Documentar decisiones técnicas importantes
    - Mantener historial de cambios arquitectónicos
    - Facilitar onboarding de nuevos miembros
    - Proveer contexto para futuras sesiones con Claude

Comandos disponibles:
    python scripts/add_decision.py "Decisión tomada"    # Registrar decisión
    python scripts/add_decision.py --list               # Ver últimas decisiones

Ejemplos de uso:
    $ python scripts/add_decision.py "Usar Next.js + Supabase en lugar de HTML estático"
    ✅ Decisión registrada: Usar Next.js + Supabase en lugar de...

    $ python scripts/add_decision.py --list
    📋 DECISIONES REGISTRADAS:
      • [2024-01-15] Usar Next.js + Supabase
      • [2024-01-14] Implementar gamificación con badges

Formato de registro:
    JSON: "[YYYY-MM-DD] Descripción de la decisión"
    MD:   ## YYYY-MM-DD HH:MM
          **Decisión**: Descripción completa

Integración con otros scripts:
    - sync_context.py: Incluye decisiones en AI_CONTEXT.md
    - save_session.py: Puede referenciar decisiones en resúmenes

Autor: Sistema PAIDEIA
Versión: 1.0.0
"""

import sys
import json
import datetime
from pathlib import Path

# Configuración de rutas
ROOT_DIR = Path(__file__).parent.parent
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"
DECISIONS_FILE = ROOT_DIR / "10000_CONTROL" / "DECISIONS.md"


def load_context() -> dict:
    """
    Carga el contexto desde el archivo JSON.

    Returns:
        dict: Contexto con estructura {decisiones_clave, pendientes, sesiones}
              Si el archivo no existe, retorna estructura vacía.

    Example:
        >>> context = load_context()
        >>> print(context['decisiones_clave'][-1])
        '[2024-01-15] Usar Next.js + Supabase'
    """
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {"decisiones_clave": [], "pendientes": [], "sesiones": []}


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


def add_decision(decision: str):
    """
    Registra una nueva decisión en JSON y Markdown.

    Args:
        decision: Descripción de la decisión tomada.

    Proceso:
        1. Carga contexto existente
        2. Agrega decisión con timestamp al JSON
        3. Mantiene solo las últimas 20 decisiones en JSON
        4. Agrega entrada formateada al archivo Markdown

    Files Modified:
        - CONTEXT_MEMORY.json: Array decisiones_clave
        - DECISIONS.md: Nueva entrada con fecha y decisión

    Example:
        >>> add_decision("Usar TypeScript en lugar de JavaScript")
        ✅ Decisión registrada: Usar TypeScript en lugar de...
    """
    now = datetime.datetime.now()

    # Actualizar JSON
    context = load_context()
    context['decisiones_clave'].append(f"[{now.strftime('%Y-%m-%d')}] {decision}")
    context['decisiones_clave'] = context['decisiones_clave'][-20:]  # Últimas 20
    save_context(context)

    # Actualizar Markdown
    DECISIONS_FILE.parent.mkdir(parents=True, exist_ok=True)

    entry = f"\n## {now.strftime('%Y-%m-%d %H:%M')}\n\n**Decisión**: {decision}\n\n---\n"

    if DECISIONS_FILE.exists():
        content = DECISIONS_FILE.read_text(encoding='utf-8')
    else:
        content = "# 📋 REGISTRO DE DECISIONES - PAIDEIA\n\n"

    content += entry
    DECISIONS_FILE.write_text(content, encoding='utf-8')

    print(f"✅ Decisión registrada: {decision[:50]}...")


def list_decisions():
    """
    Muestra las últimas 10 decisiones registradas.

    Output:
        Lista de decisiones con formato "• [fecha] descripción"

    Example:
        >>> list_decisions()
        📋 DECISIONES REGISTRADAS:
          • [2024-01-15] Usar Next.js + Supabase
          • [2024-01-14] Implementar gamificación
    """
    context = load_context()
    print("\n📋 DECISIONES REGISTRADAS:\n")
    for decision in context.get('decisiones_clave', [])[-10:]:
        print(f"  • {decision}")
    if not context.get('decisiones_clave'):
        print("  (Sin decisiones registradas)")


def main() -> int:
    """
    Punto de entrada principal del script.

    Procesa los argumentos de línea de comandos y ejecuta la acción correspondiente.

    Returns:
        int: Código de salida (0 = éxito, 1 = error/ayuda).

    Comandos:
        (sin args)      Muestra ayuda
        "decisión"      Registra nueva decisión
        --list          Lista las últimas 10 decisiones
    """
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python add_decision.py 'Descripción de la decisión'")
        print("  python add_decision.py --list")
        print("")
        print("Ejemplo: python add_decision.py 'Usar Next.js + Supabase en lugar de GitHub Pages'")
        return 1

    if sys.argv[1] == '--list':
        list_decisions()
    else:
        decision = ' '.join(sys.argv[1:])
        add_decision(decision)

    return 0


if __name__ == '__main__':
    exit(main())
