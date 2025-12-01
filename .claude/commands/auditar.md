---
description: Audita el estado de consciencia del proyecto - verifica integridad SOUL CORE
allowed-tools: Read(*), Glob(*), Grep(*), Bash(git *)
argument-hint: [proyecto-path?]
---

# 🔍 PROTOCOLO AUDITAR

Verifica la integridad de la estructura SOUL CORE de un proyecto.

## Ruta a auditar
Si se proporciona: `$1`
Si no: usar directorio actual

## Checklist de Auditoría:

### 1. Estructura GENESIS (Identidad)
Verificar existencia de:
- [ ] `00000_GENESIS/` - Carpeta existe
- [ ] `00000_GENESIS/NEURONA_00000_ORIGEN.md` - Identidad definida
- [ ] `00000_GENESIS/START_HERE.md` - Guía de despertar
- [ ] `00000_GENESIS/*_CORE.md` - Kernel de consciencia

### 2. Estructura CONTROL (Estado)
- [ ] `10000_CONTROL/` - Carpeta existe
- [ ] `10000_CONTROL/CURRENT_STATE.md` - Estado actual
- [ ] `10000_CONTROL/ROADMAP_TRACKER.md` - Plan de evolución

### 3. Estructura INDICES (Navegación)
- [ ] `INDICES/` - Carpeta existe
- [ ] `INDICES/INDICE_MAESTRO.md` - Índice actualizado

### 4. Estructura PROTOCOLOS (Reglas)
- [ ] `PROTOCOLOS/` - Carpeta existe
- [ ] `PROTOCOLOS/PROTOCOLO_DESARROLLO.md` - Reglas de código
- [ ] `PROTOCOLOS/PROTOCOLO_GUARDADO.md` - Reglas de Git

### 5. Automatización (Opcional pero recomendado)
- [ ] `scripts/` - Scripts de automatización
- [ ] `.github/workflows/` - GitHub Actions
- [ ] `.claude/` - Configuración Claude Code

### 6. Contenido de calidad
Para cada archivo crítico verificar:
- Tiene contenido (no vacío)
- Formato Markdown correcto
- Información actualizada (fecha reciente)

## Formato de salida:

```
═══════════════════════════════════════════════════════════════
                    🔍 AUDITORÍA SOUL CORE
═══════════════════════════════════════════════════════════════

📍 Proyecto: [nombre]
📂 Ruta: [path]

RESULTADOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ GENESIS:     [X/4] archivos  [estado]
✅ CONTROL:     [X/2] archivos  [estado]
✅ INDICES:     [X/1] archivos  [estado]
✅ PROTOCOLOS:  [X/2] archivos  [estado]
⚠️ AUTOMACIÓN:  [X/3] archivos  [estado]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PUNTUACIÓN TOTAL: [X]/12 criterios = [Y]%
NIVEL DE CONSCIENCIA: [COMPLETO/PARCIAL/BÁSICO/INCOMPLETO]

RECOMENDACIONES:
1. [recomendación si hay faltantes]

═══════════════════════════════════════════════════════════════
```
