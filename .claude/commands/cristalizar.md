---
description: Crea una nueva NEURONA con aprendizaje importante para memoria permanente
allowed-tools: Read(*), Write(*), Glob(*), Bash(git *)
argument-hint: [título-del-aprendizaje]
---

# 💎 PROTOCOLO CRISTALIZAR

Convierte un aprendizaje importante en una NEURONA de memoria permanente.

## Pasos:

### 1. Identificar siguiente número
Busca en `00000_GENESIS/` el último número de NEURONA usado:
```bash
ls 00000_GENESIS/NEURONA_*.md | sort | tail -1
```

### 2. Crear nueva NEURONA
Genera archivo `00000_GENESIS/NEURONA_[XXXXX]_[TITULO].md` con estructura:

```markdown
# NEURONA_[XXXXX]: $ARGUMENTS

## Fecha de Cristalización
[fecha actual]

## Contexto
[Qué problema o situación llevó a este aprendizaje]

## Aprendizaje Central
[La lección principal en 1-3 oraciones]

## Detalles Técnicos
[Código, configuración, o pasos específicos si aplica]

## Aplicación Futura
[Cuándo y cómo usar este conocimiento]

## Conexiones
[Otras NEURONAs relacionadas]

---
*Cristalizado por PAIDEIA*
*Sesión: [número de sesión si se conoce]*
```

### 3. Actualizar índice
Añadir la nueva NEURONA al `INDICES/INDICE_MAESTRO.md`

### 4. Commit automático
```bash
git add 00000_GENESIS/NEURONA_*.md INDICES/INDICE_MAESTRO.md
git commit -m "💎 NEURONA: $ARGUMENTS"
```

## Formato de salida:

```
═══════════════════════════════════════════════════════════════
                    💎 MEMORIA CRISTALIZADA
═══════════════════════════════════════════════════════════════

📄 Archivo: NEURONA_[XXXXX]_[TITULO].md
📍 Ubicación: 00000_GENESIS/
🔗 Commit: [hash]

Aprendizaje preservado para la eternidad.
═══════════════════════════════════════════════════════════════
```
