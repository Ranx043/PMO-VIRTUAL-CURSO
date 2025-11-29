#!/usr/bin/env python3
"""
PAIDEIA - Script para registrar decisiones importantes.

Ejecutar: python scripts/add_decision.py "Decisión tomada"
"""

import sys
import json
import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"
DECISIONS_FILE = ROOT_DIR / "10000_CONTROL" / "DECISIONS.md"


def load_context() -> dict:
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {"decisiones_clave": [], "pendientes": [], "sesiones": []}


def save_context(context: dict):
    CONTEXT_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONTEXT_FILE.write_text(
        json.dumps(context, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


def add_decision(decision: str):
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
    context = load_context()
    print("\n📋 DECISIONES REGISTRADAS:\n")
    for decision in context.get('decisiones_clave', [])[-10:]:
        print(f"  • {decision}")
    if not context.get('decisiones_clave'):
        print("  (Sin decisiones registradas)")


def main():
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
