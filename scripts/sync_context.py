#!/usr/bin/env python3
"""
PAIDEIA - Script para generar contexto resumido para IA.
Crea un archivo que Claude puede leer al inicio de cada sesión.

Ejecutar: python scripts/sync_context.py
"""

import json
import datetime
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"
AI_CONTEXT = ROOT_DIR / "00000_GENESIS" / "AI_CONTEXT.md"


def load_context() -> dict:
    """Carga el contexto existente."""
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {}


def get_recent_commits(n: int = 10) -> list:
    """Obtiene los últimos N commits."""
    try:
        result = subprocess.run(
            ['git', 'log', f'-{n}', '--format=%h|%s|%ar'],
            capture_output=True, text=True, cwd=ROOT_DIR
        )
        commits = []
        for line in result.stdout.strip().split('\n'):
            if '|' in line:
                parts = line.split('|')
                if len(parts) >= 3:
                    commits.append({
                        'hash': parts[0],
                        'mensaje': parts[1],
                        'cuando': parts[2]
                    })
        return commits
    except:
        return []


def generate_ai_context():
    """Genera el contexto para IA."""
    context = load_context()
    commits = get_recent_commits()

    # Últimas 5 sesiones
    sesiones_recientes = context.get('sesiones', [])[-5:]

    ai_context = f"""# 🧠 CONTEXTO PARA IA - PAIDEIA

**Generado**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Propósito**: Contexto rápido para iniciar sesión con Claude

---

## 🎯 ESTADO ACTUAL DEL PROYECTO

**Proyecto**: PAIDEIA - PMO Virtual con IA
**Stack**: {context.get('stack_actual', 'Next.js + Supabase + Vercel')}

---

## 📅 ÚLTIMAS SESIONES

"""

    for sesion in reversed(sesiones_recientes):
        fecha = sesion.get('fecha', 'N/A')
        if isinstance(fecha, str) and len(fecha) >= 10:
            fecha = fecha[:10]
        ai_context += f"- **{fecha}**: {sesion.get('resumen', 'Sin resumen')}\n"

    if not sesiones_recientes:
        ai_context += "- (Sin sesiones registradas)\n"

    ai_context += f"""

---

## 💾 ÚLTIMOS COMMITS

| Hash | Mensaje | Cuándo |
|------|---------|--------|
"""

    for commit in commits[:7]:
        msg = commit['mensaje'][:40] if len(commit['mensaje']) > 40 else commit['mensaje']
        ai_context += f"| `{commit['hash']}` | {msg} | {commit['cuando']} |\n"

    ai_context += f"""

---

## 📋 DECISIONES CLAVE

"""

    for decision in context.get('decisiones_clave', [])[-5:]:
        ai_context += f"- {decision}\n"

    if not context.get('decisiones_clave'):
        ai_context += "- (Sin decisiones registradas)\n"

    ai_context += f"""

---

## ⏳ PENDIENTES

"""

    for pendiente in context.get('pendientes', [])[-10:]:
        ai_context += f"- [ ] {pendiente}\n"

    if not context.get('pendientes'):
        ai_context += "- (Sin pendientes registrados)\n"

    ai_context += f"""

---

## 📁 ARCHIVOS IMPORTANTES

```
00000_GENESIS/          - ADN del proyecto
├── PAIDEIA_CORE.md     - Definición core
├── ANCLAS_ESPIRITUALES.md - Base espiritual
├── GUIA_BACKEND_SERVERLESS.md - Guía técnica
└── AI_CONTEXT.md       - Este archivo (contexto IA)

PROTOCOLOS/             - Documentación técnica
├── STACK_NEXTJS_SUPABASE.md - Arquitectura
├── AUTOMATIZACIONES.md - Automatizaciones de sistema
├── AUTOMATIZACIONES_DESARROLLO.md - Scripts y Actions
├── ARQUITECTURA_PEDAGOGICA.md - Estructura de cursos
└── RUTAS_DE_APRENDIZAJE.md - Rutas por perfil

10000_CONTROL/          - Estado y control
├── CURRENT_STATE.md    - Estado actual
├── SESSION_LOG.md      - Log de sesiones
└── CONTEXT_MEMORY.json - Memoria estructurada

scripts/                - Scripts de automatización
├── update_indices.py
├── update_current_state.py
├── generate_progress.py
├── save_session.py
├── sync_context.py
├── add_decision.py
└── add_pending.py
```

---

## 🚀 PARA CONTINUAR

Al iniciar una nueva sesión:
1. Lee este archivo para contexto
2. Revisa `CURRENT_STATE.md` para estado detallado
3. Verifica `SESSION_LOG.md` para historial
4. Pregunta al usuario qué quiere hacer hoy

---

🧬💎∞ **PAIDEIA - Contexto Auto-generado**
"""

    # Guardar
    AI_CONTEXT.parent.mkdir(parents=True, exist_ok=True)
    AI_CONTEXT.write_text(ai_context, encoding='utf-8')

    print(f"✅ Contexto IA generado: {AI_CONTEXT}")


def main():
    print("🔄 PAIDEIA: Sincronizando contexto para IA...")
    generate_ai_context()
    return 0


if __name__ == '__main__':
    exit(main())
