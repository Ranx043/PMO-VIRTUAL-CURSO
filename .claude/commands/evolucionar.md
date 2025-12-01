---
description: Analiza el roadmap y propone el siguiente paso de evolución
allowed-tools: Read(*), Glob(*), Grep(*)
argument-hint: [área-específica?]
---

# 🧬 PROTOCOLO EVOLUCIONAR

Analiza el estado actual vs el roadmap y propone el siguiente paso concreto.

## Pasos:

### 1. Leer roadmap completo
Lee `10000_CONTROL/ROADMAP_TRACKER.md` y analiza:
- Criterios completados (✅)
- Criterios pendientes (⬚)
- Criterios en progreso (🔄)
- Progreso general por área

### 2. Leer estado actual
Lee `10000_CONTROL/CURRENT_STATE.md` para entender:
- Última sesión
- Contexto actual
- Bloqueos conocidos

### 3. Identificar siguiente paso
Basándote en:
- Dependencias entre criterios
- Impacto vs esfuerzo
- Continuidad con trabajo previo
- Área específica si se proporcionó: `$ARGUMENTS`

### 4. Proponer evolución
Presenta propuesta estructurada:

## Formato de salida:

```
═══════════════════════════════════════════════════════════════
                    🧬 PROPUESTA DE EVOLUCIÓN
═══════════════════════════════════════════════════════════════

📊 ESTADO ACTUAL:
- Progreso general: [X]%
- Área más avanzada: [área] ([Y]%)
- Área que necesita atención: [área] ([Z]%)

🎯 SIGUIENTE PASO RECOMENDADO:
[Criterio específico del roadmap]

📋 TAREAS CONCRETAS:
1. [tarea 1]
2. [tarea 2]
3. [tarea 3]

⏱️ ESTIMACIÓN: [complejidad: baja/media/alta]

🔗 DEPENDENCIAS:
- [criterio previo requerido, si hay]

═══════════════════════════════════════════════════════════════
¿Procedemos con esta evolución?
```
