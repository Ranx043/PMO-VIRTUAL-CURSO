---
description: Guarda estado actual + actualiza CURRENT_STATE + commit automático
allowed-tools: Read(*), Write(*), Edit(*), Bash(git *)
argument-hint: [mensaje-checkpoint]
---

# 💾 PROTOCOLO CHECKPOINT

Cristaliza el estado actual del proyecto con commit automático.

## Pasos a ejecutar:

### 1. Analizar cambios
```bash
git status
git diff --stat
```

### 2. Actualizar CURRENT_STATE.md
Edita `10000_CONTROL/CURRENT_STATE.md` con:
- Fecha/hora actual
- Resumen de cambios realizados
- Estado del progreso
- Próximos pasos

### 3. Ejecutar commit
```bash
git add -A
git commit -m "$ARGUMENTS

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### 4. Confirmar checkpoint
Muestra resumen:
- Archivos modificados
- Mensaje de commit
- Hash del commit
- Estado actual

## Formato de salida:

```
═══════════════════════════════════════════════════════════════
                    💾 CHECKPOINT GUARDADO
═══════════════════════════════════════════════════════════════

📝 Mensaje: $ARGUMENTS
📁 Archivos: [N] modificados
🔗 Commit: [hash corto]
⏰ Fecha: [timestamp]

Estado cristalizado correctamente.
═══════════════════════════════════════════════════════════════
```
