#!/usr/bin/env python3
"""
PAIDEIA - Sistema de Guardado de Sesiones
=========================================

Este script permite guardar un resumen de lo trabajado en cada sesión
de desarrollo. Los resúmenes se almacenan en dos formatos:

1. JSON (CONTEXT_MEMORY.json): Para consumo programático
2. Markdown (SESSION_LOG.md): Para lectura humana

Propósito:
    - Mantener historial de trabajo realizado
    - Facilitar continuidad entre sesiones
    - Documentar automáticamente progreso
    - Capturar archivos modificados desde git

Arquitectura:
    ┌──────────────────┐     ┌─────────────────┐
    │  save_session.py │     │   Git Diff      │
    └────────┬─────────┘     └────────┬────────┘
             │                        │
             │ Guarda resumen         │ Archivos modificados
             │                        │
    ┌────────┴────────────────────────┴────────┐
    │                                          │
    ▼                                          ▼
┌──────────────────┐              ┌──────────────────┐
│ CONTEXT_MEMORY   │              │ SESSION_LOG.md   │
│    .json         │              │ (Historial)      │
│                  │              │                  │
│ {                │              │ ## Sesión        │
│   "sesiones": [  │              │ ### Resumen      │
│     {...}        │              │ ### Archivos     │
│   ]              │              │                  │
│ }                │              │                  │
└──────────────────┘              └──────────────────┘

Datos capturados:
    - Fecha y hora exacta (ISO 8601)
    - Resumen proporcionado por el usuario
    - Archivos modificados (desde git diff)

Retención de datos:
    - JSON: Últimas 20 sesiones (para no crecer indefinidamente)
    - Markdown: Historial completo (append-only)

Comando:
    python scripts/save_session.py "Descripción de lo trabajado"

Ejemplo:
    $ python scripts/save_session.py "Implementé el sistema de auth con Supabase"
    🔄 PAIDEIA: Guardando contexto de sesión...
    ✅ Sesión guardada: Implementé el sistema de auth con...
    📄 Log: 10000_CONTROL/SESSION_LOG.md
    📄 Context: 10000_CONTROL/CONTEXT_MEMORY.json

Integración con otros scripts:
    - sync_context.py: Lee sesiones para generar AI_CONTEXT.md

Autor: Sistema PAIDEIA
Versión: 1.0.0
"""

import sys
import json
import datetime
import subprocess
from pathlib import Path

# Configuración de rutas
ROOT_DIR = Path(__file__).parent.parent
SESSION_LOG = ROOT_DIR / "10000_CONTROL" / "SESSION_LOG.md"
CONTEXT_FILE = ROOT_DIR / "10000_CONTROL" / "CONTEXT_MEMORY.json"


def load_context() -> dict:
    """
    Carga el contexto existente o crea estructura inicial.

    Returns:
        dict: Contexto con estructura completa incluyendo:
            - proyecto: Nombre del proyecto
            - sesiones: Lista de sesiones registradas
            - decisiones_clave: Lista de decisiones
            - pendientes: Lista de tareas pendientes
            - archivos_importantes: Referencias a archivos clave
            - stack_actual: Stack tecnológico actual

    Note:
        Si el archivo no existe, retorna estructura default
        con valores iniciales para PAIDEIA.
    """
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
    """
    Guarda el contexto actualizado en el archivo JSON.

    Args:
        context: Diccionario con la estructura completa del contexto.

    Note:
        Crea el directorio padre si no existe.
        Usa UTF-8 para soportar caracteres especiales (español).
    """
    CONTEXT_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONTEXT_FILE.write_text(
        json.dumps(context, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


def get_modified_files() -> str:
    """
    Obtiene la lista de archivos modificados desde el último commit.

    Returns:
        str: Lista de archivos separados por newline, o mensaje
             indicando que no hay cambios o que no está disponible.

    Note:
        Usa `git diff --name-only HEAD~1` para comparar
        con el commit anterior. Maneja errores silenciosamente.

    Example:
        >>> print(get_modified_files())
        scripts/save_session.py
        PROTOCOLOS/STACK.md
    """
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~1'],
            capture_output=True, text=True, cwd=ROOT_DIR
        )
        return result.stdout.strip() or "(sin cambios)"
    except:
        return "(no disponible)"


def append_session_log(resumen: str):
    """
    Agrega una nueva entrada al archivo de log de sesiones.

    Args:
        resumen: Descripción del trabajo realizado en la sesión.

    Proceso:
        1. Genera entrada con timestamp y resumen
        2. Obtiene archivos modificados de git
        3. Crea archivo si no existe (con header)
        4. Append de la nueva entrada

    Format:
        ## 📅 Sesión YYYY-MM-DD HH:MM
        ### Resumen
        [resumen proporcionado]
        ### Archivos Modificados
        [lista de git diff]

    Note:
        El archivo SESSION_LOG.md es append-only,
        mantiene historial completo.
    """
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


def main() -> int:
    """
    Punto de entrada principal del script.

    Procesa el resumen de la sesión y lo guarda en ambos formatos.

    Returns:
        int: Código de salida (0 = éxito, 1 = error/ayuda).

    Proceso:
        1. Valida argumentos de línea de comandos
        2. Actualiza CONTEXT_MEMORY.json con nueva sesión
        3. Mantiene solo las últimas 20 sesiones
        4. Append al SESSION_LOG.md

    Usage:
        python scripts/save_session.py "Lo que hice hoy"
    """
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
