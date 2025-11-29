#!/usr/bin/env python3
"""
PAIDEIA - Generador de Contexto para IA
=======================================

Este script genera un archivo Markdown optimizado para que Claude pueda
entender rápidamente el estado actual del proyecto al iniciar una nueva sesión.

Propósito:
    - Crear un "resumen ejecutivo" del proyecto para Claude
    - Combinar información de múltiples fuentes en un solo archivo
    - Facilitar la continuidad entre sesiones de trabajo

Arquitectura:
    ┌──────────────────┐     ┌─────────────────┐
    │ CONTEXT_MEMORY   │     │   Git History   │
    │     .json        │     │   (commits)     │
    └────────┬─────────┘     └────────┬────────┘
             │                        │
             └───────────┬────────────┘
                         │
                         ▼
               ┌─────────────────┐
               │ sync_context.py │
               └────────┬────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ AI_CONTEXT.md   │
               │ (Para Claude)   │
               └─────────────────┘

Fuentes de datos:
    1. CONTEXT_MEMORY.json:
       - Sesiones recientes
       - Decisiones clave
       - Pendientes activos
       - Stack actual

    2. Git:
       - Últimos commits
       - Hash, mensaje, fecha

Contenido generado (AI_CONTEXT.md):
    - Estado actual del proyecto
    - Últimas 5 sesiones
    - Últimos 7 commits
    - Decisiones clave recientes
    - Pendientes actuales
    - Mapa de archivos importantes

Uso recomendado:
    - Ejecutar antes de iniciar sesión con Claude
    - Ejecutar después de cambios importantes
    - Incluir en workflow de CI/CD (opcional)

Comando:
    python scripts/sync_context.py

Ejemplo de salida:
    🔄 PAIDEIA: Sincronizando contexto para IA...
    ✅ Contexto IA generado: 00000_GENESIS/AI_CONTEXT.md

Autor: Sistema PAIDEIA
Versión: 1.0.0
"""

import json
import datetime
import subprocess
from pathlib import Path

# Configuración de rutas
ROOT_DIR = Path(__file__).parent.parent
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"
AI_CONTEXT = ROOT_DIR / "00000_GENESIS" / "AI_CONTEXT.md"


def load_context() -> dict:
    """
    Carga el contexto desde el archivo JSON.

    Returns:
        dict: Contexto completo o diccionario vacío si no existe.

    Note:
        Retorna {} en lugar de estructura default para permitir
        que generate_ai_context() maneje los casos de datos faltantes.
    """
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {}


def get_recent_commits(n: int = 10) -> list:
    """
    Obtiene los últimos N commits del repositorio git.

    Args:
        n: Número de commits a obtener (default: 10).

    Returns:
        list: Lista de diccionarios con {hash, mensaje, cuando}.
              Lista vacía si hay error o no hay commits.

    Example:
        >>> commits = get_recent_commits(5)
        >>> print(commits[0])
        {'hash': 'abc123', 'mensaje': 'feat: Add login', 'cuando': '2 hours ago'}

    Note:
        Usa formato personalizado de git log para parsear fácilmente.
        Maneja errores silenciosamente retornando lista vacía.
    """
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
    """
    Genera el archivo AI_CONTEXT.md con información consolidada.

    Este es el método principal que:
    1. Carga contexto desde JSON
    2. Obtiene commits recientes de git
    3. Genera markdown formateado
    4. Escribe el archivo de salida

    Secciones generadas:
        - Estado actual del proyecto
        - Últimas 5 sesiones
        - Últimos 7 commits
        - Decisiones clave (últimas 5)
        - Pendientes activos (últimos 10)
        - Mapa de archivos importantes

    Output:
        Archivo: 00000_GENESIS/AI_CONTEXT.md
    """
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


def main() -> int:
    """
    Punto de entrada principal del script.

    Ejecuta la generación del contexto para IA y muestra feedback.

    Returns:
        int: Código de salida (siempre 0, no hay casos de error manejados).

    Usage:
        python scripts/sync_context.py
    """
    print("🔄 PAIDEIA: Sincronizando contexto para IA...")
    generate_ai_context()
    return 0


if __name__ == '__main__':
    exit(main())
