# Scripts de Automatizacion - PAIDEIA

Sistema de scripts Python para mantener la memoria y contexto del proyecto PAIDEIA entre sesiones de trabajo con Claude.

## Arquitectura del Sistema

```
                    ┌─────────────────────────────────────┐
                    │         SISTEMA DE MEMORIA          │
                    │              PAIDEIA                │
                    └─────────────────────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
         ▼                           ▼                           ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│  save_session   │       │  add_decision   │       │   add_pending   │
│      .py        │       │      .py        │       │      .py        │
└────────┬────────┘       └────────┬────────┘       └────────┬────────┘
         │                         │                         │
         │                         │                         │
         └─────────────────────────┼─────────────────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────────────┐
                    │       CONTEXT_MEMORY.json           │
                    │    (Memoria Central Estructurada)   │
                    └─────────────────────────────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────────────┐
                    │         sync_context.py             │
                    │    (Generador de Contexto IA)       │
                    └─────────────────────────────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────────────┐
                    │         AI_CONTEXT.md               │
                    │    (Resumen para Claude)            │
                    └─────────────────────────────────────┘
```

## Scripts Disponibles

### 1. save_session.py - Guardar Sesion

Guarda un resumen de lo trabajado en la sesion actual.

```bash
# Uso basico
python scripts/save_session.py "Descripcion de lo trabajado"

# Ejemplo
python scripts/save_session.py "Implemente auth con Supabase y cree componentes de login"
```

**Archivos modificados:**
- `10000_CONTROL/CONTEXT_MEMORY.json` - Agrega sesion al array
- `10000_CONTROL/SESSION_LOG.md` - Append de entrada con archivos modificados

**Retencion:** Ultimas 20 sesiones en JSON, historial completo en Markdown.

---

### 2. add_decision.py - Registrar Decision

Documenta decisiones arquitectonicas o tecnicas importantes.

```bash
# Registrar nueva decision
python scripts/add_decision.py "Usar Next.js + Supabase en lugar de HTML estatico"

# Ver ultimas decisiones
python scripts/add_decision.py --list
```

**Archivos modificados:**
- `10000_CONTROL/CONTEXT_MEMORY.json` - Array decisiones_clave
- `10000_CONTROL/DECISIONS.md` - Historial con timestamps

**Retencion:** Ultimas 20 decisiones en JSON, historial completo en Markdown.

---

### 3. add_pending.py - Gestionar Pendientes

Administra una lista de tareas pendientes.

```bash
# Agregar pendiente
python scripts/add_pending.py "Implementar sistema de quiz"

# Ver todos los pendientes
python scripts/add_pending.py --list

# Marcar como completado (numero segun --list)
python scripts/add_pending.py --done 1

# Limpiar todos los pendientes
python scripts/add_pending.py --clear
```

**Archivo modificado:**
- `10000_CONTROL/CONTEXT_MEMORY.json` - Array pendientes

---

### 4. sync_context.py - Generar Contexto para IA

Genera un archivo Markdown optimizado para que Claude entienda rapidamente el estado del proyecto.

```bash
python scripts/sync_context.py
```

**Fuentes de datos:**
- `CONTEXT_MEMORY.json` - Sesiones, decisiones, pendientes
- `git log` - Ultimos commits

**Archivo generado:**
- `00000_GENESIS/AI_CONTEXT.md` - Resumen ejecutivo para Claude

**Contenido generado:**
- Estado actual del proyecto
- Ultimas 5 sesiones
- Ultimos 7 commits
- Decisiones clave
- Pendientes activos
- Mapa de archivos importantes

---

## Flujo de Trabajo Recomendado

### Al Iniciar Sesion con Claude

```bash
# 1. Generar contexto actualizado
python scripts/sync_context.py

# 2. Claude lee AI_CONTEXT.md automaticamente
```

### Durante la Sesion

```bash
# Registrar decisiones importantes
python scripts/add_decision.py "Decidimos usar RLS en lugar de middleware"

# Agregar tareas pendientes
python scripts/add_pending.py "Crear tests para auth"

# Ver pendientes actuales
python scripts/add_pending.py --list
```

### Al Terminar Sesion

```bash
# 1. Guardar resumen de lo trabajado
python scripts/save_session.py "Implemente login, registro y recuperacion de contrasena"

# 2. Regenerar contexto para proxima sesion
python scripts/sync_context.py

# 3. Commit y push (si es necesario)
git add .
git commit -m "save: Sesion - descripcion breve"
git push
```

---

## Estructura de Archivos

```
PMO-VIRTUAL-CURSO/
├── scripts/
│   ├── README.md              # Este archivo
│   ├── save_session.py        # Guardar sesiones
│   ├── sync_context.py        # Generar contexto IA
│   ├── add_decision.py        # Registrar decisiones
│   ├── add_pending.py         # Gestionar pendientes
│   ├── update_indices.py      # Actualizar indices de carpetas
│   ├── update_current_state.py # Actualizar estado actual
│   └── generate_progress.py   # Generar reporte de progreso
│
├── 10000_CONTROL/
│   ├── CONTEXT_MEMORY.json    # Memoria central (JSON)
│   ├── SESSION_LOG.md         # Log de sesiones (MD)
│   ├── DECISIONS.md           # Registro de decisiones (MD)
│   └── CURRENT_STATE.md       # Estado actual del proyecto
│
└── 00000_GENESIS/
    └── AI_CONTEXT.md          # Contexto para Claude
```

---

## Estructura de CONTEXT_MEMORY.json

```json
{
  "proyecto": "PAIDEIA",
  "stack_actual": "Next.js + Supabase + Vercel",
  "sesiones": [
    {
      "fecha": "2024-01-15T14:30:00",
      "resumen": "Implemente sistema de auth"
    }
  ],
  "decisiones_clave": [
    "[2024-01-15] Usar Supabase para auth y BD"
  ],
  "pendientes": [
    "Crear componente de quiz",
    "Implementar gamificacion"
  ],
  "archivos_importantes": []
}
```

---

## Integracion con GitHub Actions (Opcional)

Los scripts pueden integrarse en workflows de CI/CD:

```yaml
# .github/workflows/sync-context.yml
name: Sync AI Context

on:
  push:
    branches: [main]

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python scripts/sync_context.py
      - uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "auto: Sync AI context"
```

---

## Requisitos

- Python 3.8+
- Git instalado y configurado
- Repositorio PAIDEIA clonado

No requiere dependencias externas (solo libreria estandar de Python).

---

## Autor

Sistema PAIDEIA - PMO Virtual con IA
Version 1.0.0
