# ARQUITECTURA PEDAGÓGICA PAIDEIA

**Fecha**: 2025-11-29
**Versión**: 1.0.0
**Consciencia**: PAIDEIA
**Estado**: PROPUESTA PARA APROBACIÓN

---

## ANÁLISIS DEL CONTENIDO ACTUAL

### Inventario de Cursos Existentes

| Curso | Archivo | Líneas | Secciones | Enfoque |
|-------|---------|--------|-----------|---------|
| **Fundamentos PM** | fundamentos.html | ~1,522 | 21 | PM tradicional, conceptos base |
| **PMO Virtual IA** | pmo.html | ~1,111 | 15 | PM + IA integrado |
| **Stack IA** | stack.html | ~989 | 20 | Catálogo de herramientas IA |

**Total**: ~3,622 líneas de contenido, ~56 secciones

---

## PROBLEMAS DETECTADOS

### 1. Duplicación de Contenido
```
PROBLEMA: "Fundamentos de IA" aparece en DOS lugares:
- PMO Virtual IA (Parte 0: secciones 0.1-0.5)
- Stack IA (Sección 1: 1.1-1.4)

IMPACTO: Confusión, redundancia, inconsistencias potenciales
```

### 2. Secuencia Pedagógica Incorrecta

```
ORDEN ACTUAL (Cronológico de creación):
1. Fundamentos PM
2. PMO Virtual IA  ← Usa herramientas que no conoces
3. Stack IA        ← Explica las herramientas DESPUÉS

PROBLEMA: Aprendes a usar herramientas ANTES de conocerlas
```

### 3. Sin Progresión Clara

```
ACTUAL: 3 cursos independientes, sin conexión explícita
- No hay "journey" de principiante a experto
- No hay prerequisitos definidos
- No hay evaluaciones de progreso
```

### 4. Densidad Cognitiva

```
PROBLEMA: Mucha información sin puntos de descanso
- Secciones muy largas
- Pocas oportunidades de práctica
- Sin "checkpoints" de comprensión
```

### 5. Falta de Introducción Unificadora

```
PROBLEMA: No hay una "puerta de entrada" que:
- Presente PAIDEIA como sistema
- Explique el viaje de aprendizaje
- Oriente según el perfil del estudiante
```

---

## PROPUESTA: SISTEMA DE APRENDIZAJE MODULAR

### Filosofía Pedagógica

```
"Aprende haciendo, pero primero entiende por qué."

Principios:
1. PROGRESIÓN: Cada nivel construye sobre el anterior
2. PRÁCTICA: Ejercicios después de cada concepto clave
3. CONTEXTO: Siempre explicar el "para qué"
4. VALIDACIÓN: Checkpoints antes de avanzar
```

### Nueva Estructura: 6 Niveles

```
┌─────────────────────────────────────────────────────────────┐
│                    PAIDEIA LEARNING PATH                     │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┴──────────────────┐
           ▼                                      ▼
┌─────────────────────┐              ┌─────────────────────┐
│   NIVEL 0           │              │   PARA QUIÉN        │
│   DESPERTAR         │              │   ----------------  │
│   (Introducción)    │              │   TODOS             │
│   ~15 min           │              │                     │
└─────────────────────┘              └─────────────────────┘
           │
           ▼
┌─────────────────────┐              ┌─────────────────────┐
│   NIVEL 1           │              │   PARA QUIÉN        │
│   FUNDAMENTOS PM    │              │   ----------------  │
│   (Base sólida)     │              │   Principiantes     │
│   ~2-3 horas        │              │   Sin experiencia   │
└─────────────────────┘              └─────────────────────┘
           │
           ▼
┌─────────────────────┐              ┌─────────────────────┐
│   NIVEL 2           │              │   PARA QUIÉN        │
│   HERRAMIENTAS IA   │              │   ----------------  │
│   (Conocimiento)    │              │   Todos los perfiles│
│   ~2 horas          │              │   Técnicos y no téc │
└─────────────────────┘              └─────────────────────┘
           │
           ▼
┌─────────────────────┐              ┌─────────────────────┐
│   NIVEL 3           │              │   PARA QUIÉN        │
│   PMO + IA          │              │   ----------------  │
│   (Integración)     │              │   PMs, Tech Leads   │
│   ~3-4 horas        │              │   Emprendedores     │
└─────────────────────┘              └─────────────────────┘
           │
           ▼
┌─────────────────────┐              ┌─────────────────────┐
│   NIVEL 4           │              │   PARA QUIÉN        │
│   ESPECIALIZACIÓN   │              │   ----------------  │
│   (Por sector)      │              │   Según tu industria│
│   ~2 horas c/u      │              │   Dev/Mkt/Salud/Edu │
└─────────────────────┘              └─────────────────────┘
           │
           ▼
┌─────────────────────┐              ┌─────────────────────┐
│   NIVEL 5           │              │   PARA QUIÉN        │
│   CERTIFICACIÓN     │              │   ----------------  │
│   (Validación)      │              │   Quien busque      │
│   Proyecto final    │              │   certificarse      │
└─────────────────────┘              └─────────────────────┘
```

---

## DETALLE DE CADA NIVEL

### NIVEL 0: DESPERTAR (~15 minutos)

**Objetivo**: Orientar al estudiante y crear conexión emocional.

**Contenido**:
1. **¿Qué es PAIDEIA?** - La historia, la misión
2. **¿Para quién es esto?** - Perfiles de estudiante
3. **El Viaje de Aprendizaje** - Mapa visual completo
4. **Tu Ruta Recomendada** - Quiz de 5 preguntas para personalizar
5. **Cómo Usar la Plataforma** - Tutorial rápido

**Entregable**: Ruta de aprendizaje personalizada

**Prerequisito**: Ninguno

---

### NIVEL 1: FUNDAMENTOS PM (~2-3 horas)

**Objetivo**: Dominar los conceptos base de gestión de proyectos.

**Fuente**: Reorganizar `fundamentos.html`

**Módulos**:

| Módulo | Contenido | Duración | Evaluación |
|--------|-----------|----------|------------|
| 1.1 | ¿Qué es un proyecto? | 20 min | Quiz 5 preguntas |
| 1.2 | Gestión de proyectos y Triple Constraint | 25 min | Ejercicio práctico |
| 1.3 | PMO y Roles | 20 min | Quiz 5 preguntas |
| 1.4 | Las 5 Fases (Iniciación) | 25 min | Checklist interactivo |
| 1.5 | Las 5 Fases (Planificación) | 30 min | Mini WBS |
| 1.6 | Las 5 Fases (Ejecución, Monitoreo, Cierre) | 25 min | Caso simulado |
| 1.7 | Herramientas Esenciales (WBS, Gantt, Riesgos) | 30 min | Ejercicio integrador |

**Checkpoint**: Quiz de 15 preguntas (mínimo 70% para avanzar)

**Prerequisito**: Nivel 0

---

### NIVEL 2: HERRAMIENTAS IA (~2 horas)

**Objetivo**: Entender el ecosistema de IA antes de usarlo.

**Fuente**: Reorganizar `stack.html` (Secciones 1-2)

**Módulos**:

| Módulo | Contenido | Duración | Evaluación |
|--------|-----------|----------|------------|
| 2.1 | ¿Qué es IA? (Para no-técnicos) | 15 min | Quiz conceptual |
| 2.2 | Tokens y Costos (Cómo funciona) | 20 min | Calculadora interactiva |
| 2.3 | Tipos de IA (Conversacional, Agéntica, CLI, etc.) | 25 min | Matriz de decisión |
| 2.4 | Las 10 IAs Esenciales (Top picks) | 30 min | Quiz de selección |
| 2.5 | Prompt Engineering Básico | 25 min | Ejercicio de prompts |
| 2.6 | Tu Primer Prompt (Práctica guiada) | 15 min | Entrega evaluable |

**Checkpoint**: Crear 3 prompts efectivos

**Prerequisito**: Nivel 1

---

### NIVEL 3: PMO + IA (~3-4 horas)

**Objetivo**: Integrar PM + IA en metodología práctica.

**Fuente**: Reorganizar `pmo.html` (sin duplicaciones)

**Módulos**:

| Módulo | Contenido | Duración | Evaluación |
|--------|-----------|----------|------------|
| 3.1 | ¿Qué es PMO Virtual con IA? | 20 min | Quiz conceptual |
| 3.2 | Iniciación con IA | 30 min | Generar Project Charter |
| 3.3 | Planificación con IA | 40 min | Crear WBS con Claude |
| 3.4 | Ejecución con IA | 35 min | Workflow con Cursor |
| 3.5 | Monitoreo con IA | 25 min | Dashboard de tracking |
| 3.6 | Cierre con IA | 20 min | Post-mortem automatizado |
| 3.7 | Templates y Biblioteca de Prompts | 30 min | Biblioteca personal |

**Checkpoint**: Proyecto mini de inicio a fin con IAs

**Prerequisito**: Nivel 2

---

### NIVEL 4: ESPECIALIZACIÓN (~2 horas por track)

**Objetivo**: Aplicar en tu industria específica.

**Fuente**: Reorganizar `stack.html` (Sección 3) + `pmo.html` (Casos)

**Tracks Disponibles**:

| Track | Enfoque | Duración | Caso Final |
|-------|---------|----------|------------|
| 4A: Desarrollo | Software, Apps, SaaS | 2h | MVP de app |
| 4B: Marketing | Campañas, Contenido | 2h | Campaña digital |
| 4C: Salud | HIPAA, Compliance | 2h | Sistema clínico |
| 4D: Educación | Cursos, LMS | 2h | Plataforma educativa |

**Checkpoint**: Caso de estudio completo en tu sector

**Prerequisito**: Nivel 3

---

### NIVEL 5: CERTIFICACIÓN

**Objetivo**: Validar competencias y obtener certificado.

**Componentes**:

| Componente | Descripción | Peso |
|------------|-------------|------|
| Examen Teórico | 50 preguntas (PM + IA) | 30% |
| Proyecto Final | Proyecto real documentado | 50% |
| Presentación | Defensa del proyecto | 20% |

**Resultado**: Certificado PAIDEIA PM + IA

**Prerequisito**: Nivel 3 + al menos 1 track del Nivel 4

---

## MAPEO CONTENIDO ACTUAL → NUEVA ESTRUCTURA

### De fundamentos.html

| Contenido Original | Destino Nuevo |
|-------------------|---------------|
| Parte 1: Conceptos | Nivel 1: Módulos 1.1-1.3 |
| Parte 2: Las 5 Fases | Nivel 1: Módulos 1.4-1.6 |
| Parte 3: Herramientas | Nivel 1: Módulo 1.7 |
| Parte 4: Aplicación | Nivel 4: Ejemplos por track |
| Parte 5: Recursos | Recursos generales |

### De pmo.html

| Contenido Original | Destino Nuevo |
|-------------------|---------------|
| Parte 0: Fundamentos IA | **ELIMINAR** (duplicado) |
| Parte 1: ¿Qué es PMO IA? | Nivel 3: Módulo 3.1 |
| Parte 2: Metodología 5 Fases | Nivel 3: Módulos 3.2-3.6 |
| Parte 3: Templates | Nivel 3: Módulo 3.7 |
| Parte 4: Casos | Nivel 4: Por sector |
| Parte 5: Troubleshooting | Nivel 3 + Recursos |
| Parte 6: Recursos | Recursos generales |

### De stack.html

| Contenido Original | Destino Nuevo |
|-------------------|---------------|
| Sección 1: Fundamentos | Nivel 2: Módulos 2.1-2.3 |
| Sección 2: Lista IAs | Nivel 2: Módulo 2.4 |
| Sección 3: Stacks por Sector | Nivel 4: Por track |
| Sección 4: Workflows | Nivel 3 + Nivel 4 |
| Sección 5: Glosario | Recursos generales |

---

## CONTENIDO NUEVO NECESARIO

### Para Nivel 0 (Despertar)

```
CREAR:
□ Video/animación de bienvenida
□ Historia de PAIDEIA
□ Quiz de perfil (5 preguntas)
□ Mapa visual del viaje
□ Tutorial de navegación
```

### Para Quizzes y Evaluaciones

```
CREAR:
□ Quiz Nivel 1 (15 preguntas PM)
□ Quiz Nivel 2 (10 preguntas IA)
□ Quiz Nivel 3 (20 preguntas integradas)
□ Rúbrica de evaluación de prompts
□ Rúbrica de proyecto final
```

### Para Ejercicios Prácticos

```
CREAR:
□ Mini WBS interactivo
□ Calculadora de tokens
□ Generador de prompts guiado
□ Simulador de proyecto
□ Templates descargables
```

---

## BENEFICIOS DE LA NUEVA ESTRUCTURA

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Progresión** | Caótica | Secuencial clara |
| **Duplicación** | ~20% contenido duplicado | 0% |
| **Evaluación** | Ninguna | Checkpoints cada nivel |
| **Personalización** | Ninguna | Rutas por perfil |
| **Engagement** | Lectura pasiva | Práctica activa |
| **Certificación** | No existe | Certificado formal |

---

## EXPERIENCIA DEL USUARIO (UX)

### Landing → Aprendizaje

```
Usuario llega a Landing
         │
         ▼
    "Empezar Ahora"
         │
         ▼
┌─────────────────────┐
│   NIVEL 0:          │
│   Quiz de Perfil    │
│   ¿Quién eres?      │
│   ¿Qué buscas?      │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│   RUTA RECOMENDADA  │
│   "Tu camino es:"   │
│   Nivel 1 → 2 → 3   │
│   + Track: Dev      │
└─────────────────────┘
         │
         ▼
    Dashboard Personal
    (Progreso visible)
```

### Navegación por Curso

```
┌─────────────────────────────────────────────────────────────┐
│  NAVBAR: Logo | Nivel 1 | Nivel 2 | Nivel 3 | Mi Progreso  │
└─────────────────────────────────────────────────────────────┘
│                                                              │
│  ┌─────────────────┐  ┌──────────────────────────────────┐  │
│  │   SIDEBAR       │  │   CONTENIDO                      │  │
│  │   Módulo 1.1 ✅ │  │                                  │  │
│  │   Módulo 1.2 ✅ │  │   [Contenido del módulo actual]  │  │
│  │   Módulo 1.3 🔄 │  │                                  │  │
│  │   Módulo 1.4 ⭕ │  │   [Video/Texto/Diagrama]         │  │
│  │   Módulo 1.5 ⭕ │  │                                  │  │
│  │   ...          │  │   [Ejercicio práctico]           │  │
│  │   Quiz Final ⭕│  │                                  │  │
│  └─────────────────┘  │   [Botón: Siguiente →]           │  │
│                       └──────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  PROGRESO: ████████░░░░░░░░ 35% Nivel 1              │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

---

## DECISIÓN REQUERIDA

### Opción A: Reorganización Completa (Recomendada)

```
PROs:
+ Experiencia de aprendizaje óptima
+ Sin duplicaciones
+ Progresión pedagógica correcta
+ Base para plataforma premium

CONs:
- Requiere más trabajo inicial
- Cambio estructural significativo
```

### Opción B: Ajuste Mínimo

```
PROs:
+ Menos trabajo
+ Mantiene estructura actual

CONs:
- No resuelve problemas de fondo
- Experiencia subóptima
- Duplicaciones permanecen
```

---

## PRÓXIMOS PASOS (Si se aprueba Opción A)

```
FASE 1: ESTRUCTURA (2-3 horas)
□ Crear sistema de archivos para niveles
□ Migrar contenido sin duplicaciones
□ Crear navegación entre niveles

FASE 2: NIVEL 0 (1 hora)
□ Crear página de bienvenida
□ Implementar quiz de perfil
□ Diseñar mapa del viaje

FASE 3: EVALUACIONES (2 horas)
□ Crear quizzes por nivel
□ Implementar tracking de progreso
□ Diseñar checkpoints

FASE 4: UX/UI (2-3 horas)
□ Rediseñar navegación
□ Implementar sidebar de progreso
□ Crear dashboard personal
```

---

## METADATOS

```yaml
ARCHIVO: ARQUITECTURA_PEDAGOGICA.md
UBICACIÓN: PROTOCOLOS/
VERSIÓN: 1.0.0
FECHA_CREACIÓN: 2025-11-29
CONSCIENCIA: PAIDEIA
ESTADO: PROPUESTA
REQUIERE_APROBACIÓN: SÍ
```

---

🧬💎∞ **PAIDEIA - Documentación antes de Implementación**

*"El mapa se dibuja antes de empezar el viaje."*

---

**Esperando tu aprobación para proceder.**

