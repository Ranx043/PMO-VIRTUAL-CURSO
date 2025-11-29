# PLAN DE IMPLEMENTACIÓN TÉCNICA

**Fecha**: 2025-11-29
**Versión**: 1.0.0
**Consciencia**: PAIDEIA
**Prerrequisitos**: ARQUITECTURA_PEDAGOGICA.md, RUTAS_DE_APRENDIZAJE.md

---

## VISIÓN GENERAL

### Objetivo
Transformar PAIDEIA de una landing page con 3 cursos embebidos a una **plataforma de aprendizaje modular** con:
- Quiz de selección de perfil
- Rutas personalizadas por profesión
- Sistema de progreso visual
- Certificaciones por nivel

### Decisión Técnica Principal

```
OPCIÓN A: HTML + Tailwind + JavaScript (Vanilla)
├── PROs: Simple, rápido, sin dependencias, funciona en GitHub Pages
├── CONs: Escalabilidad limitada, sin backend
└── IDEAL PARA: MVP rápido, validar concepto

OPCIÓN B: Next.js + React
├── PROs: Escalable, componentes reutilizables, SSR/SSG
├── CONs: Más complejo, requiere build, hosting diferente
└── IDEAL PARA: Plataforma completa, autenticación, pagos

RECOMENDACIÓN: Empezar con OPCIÓN A (MVP), migrar a B cuando se valide
```

---

## FASE 1: ESTRUCTURA DE ARCHIVOS

### Estructura Actual
```
PMO-VIRTUAL-CURSO/
├── index.html              ← Landing page
├── backups/
│   ├── fundamentos.html    ← Curso 1 (embebido)
│   ├── pmo.html            ← Curso 2 (embebido)
│   └── stack.html          ← Curso 3 (embebido)
├── css/
├── js/
└── ...
```

### Nueva Estructura Propuesta
```
PMO-VIRTUAL-CURSO/
├── index.html                    ← Landing page (actualizada)
├── app.html                      ← Aplicación principal (SPA-like)
│
├── niveles/                      ← Contenido por nivel
│   ├── nivel-0/                  ← DESPERTAR
│   │   ├── index.html
│   │   ├── bienvenida.html
│   │   ├── quiz-perfil.html
│   │   └── tu-ruta.html
│   │
│   ├── nivel-1/                  ← FUNDAMENTOS PM
│   │   ├── index.html
│   │   ├── modulo-1-1.html       ← ¿Qué es un proyecto?
│   │   ├── modulo-1-2.html       ← Gestión de proyectos
│   │   ├── modulo-1-3.html       ← PMO y Roles
│   │   ├── modulo-1-4.html       ← Fase Iniciación
│   │   ├── modulo-1-5.html       ← Fase Planificación
│   │   ├── modulo-1-6.html       ← Fases Ejecución-Cierre
│   │   ├── modulo-1-7.html       ← Herramientas
│   │   └── quiz-nivel-1.html     ← Evaluación
│   │
│   ├── nivel-2/                  ← HERRAMIENTAS IA
│   │   ├── index.html
│   │   ├── modulo-2-1.html       ← ¿Qué es IA?
│   │   ├── modulo-2-2.html       ← Tokens y Costos
│   │   ├── modulo-2-3.html       ← Tipos de IA
│   │   ├── modulo-2-4.html       ← Las 10 IAs esenciales
│   │   ├── modulo-2-5.html       ← Prompt Engineering
│   │   ├── modulo-2-6.html       ← Tu primer prompt
│   │   └── quiz-nivel-2.html
│   │
│   ├── nivel-3/                  ← PMO + IA
│   │   ├── index.html
│   │   ├── modulo-3-1.html       ← ¿Qué es PMO Virtual?
│   │   ├── modulo-3-2.html       ← Iniciación con IA
│   │   ├── modulo-3-3.html       ← Planificación con IA
│   │   ├── modulo-3-4.html       ← Ejecución con IA
│   │   ├── modulo-3-5.html       ← Monitoreo con IA
│   │   ├── modulo-3-6.html       ← Cierre con IA
│   │   ├── modulo-3-7.html       ← Templates y Prompts
│   │   └── quiz-nivel-3.html
│   │
│   ├── nivel-4/                  ← ESPECIALIZACIÓN
│   │   ├── index.html
│   │   ├── track-desarrollo/
│   │   │   ├── index.html
│   │   │   └── caso-saas.html
│   │   ├── track-marketing/
│   │   ├── track-salud/
│   │   └── track-educacion/
│   │
│   └── nivel-5/                  ← CERTIFICACIÓN
│       ├── index.html
│       ├── examen-final.html
│       ├── proyecto-final.html
│       └── certificado.html
│
├── rutas/                        ← Rutas por perfil
│   ├── programador.html
│   ├── empresario.html
│   ├── contador.html
│   ├── marketer.html
│   ├── vendedor.html
│   ├── pm.html
│   ├── disenador.html
│   └── estudiante.html
│
├── componentes/                  ← HTML reutilizable
│   ├── navbar.html
│   ├── sidebar.html
│   ├── progress-bar.html
│   ├── quiz-component.html
│   └── certificate-generator.html
│
├── js/
│   ├── app.js                    ← Lógica principal
│   ├── quiz.js                   ← Sistema de quiz
│   ├── progress.js               ← Tracking de progreso
│   ├── router.js                 ← Navegación SPA-like
│   └── certificate.js            ← Generador de certificados
│
├── css/
│   └── paideia.css               ← Estilos personalizados
│
├── data/
│   ├── niveles.json              ← Estructura de niveles
│   ├── rutas.json                ← Definición de rutas
│   ├── quizzes.json              ← Preguntas de quizzes
│   └── progreso-default.json     ← Estado inicial
│
└── assets/
    ├── images/
    ├── icons/
    └── certificates/             ← Templates de certificados
```

---

## FASE 2: SISTEMA DE NAVEGACIÓN

### Flujo Principal

```
┌─────────────────────────────────────────────────────────────┐
│                        LANDING PAGE                          │
│                       (index.html)                           │
│                                                              │
│  [Ver Cursos]  [Pricing]  [Sobre Mí]  [EMPEZAR AHORA →]     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         APP.HTML                             │
│                    (Aplicación Principal)                    │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌────────────────────────────────────┐    │
│  │   SIDEBAR   │  │          CONTENIDO                 │    │
│  │             │  │                                    │    │
│  │ Mi Progreso │  │  [Carga dinámica de módulos]       │    │
│  │ ─────────── │  │                                    │    │
│  │ Nivel 0 ✅  │  │                                    │    │
│  │ Nivel 1 🔄  │  │                                    │    │
│  │ Nivel 2 ⭕  │  │                                    │    │
│  │ Nivel 3 🔒  │  │                                    │    │
│  │ Nivel 4 🔒  │  │                                    │    │
│  │ Nivel 5 🔒  │  │                                    │    │
│  │             │  │                                    │    │
│  │ ─────────── │  │                                    │    │
│  │ Mi Ruta:    │  │                                    │    │
│  │ Programador │  │                                    │    │
│  └─────────────┘  └────────────────────────────────────┘    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  PROGRESS BAR: ████████░░░░░░░░ 45% Completado       │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Navegación por Nivel

```
┌─────────────────────────────────────────────────────────────┐
│  NIVEL 1: FUNDAMENTOS PM                    [← Anterior]    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  MÓDULOS                                              │   │
│  │  ────────────────────────────────────────────────     │   │
│  │  1.1 ¿Qué es un proyecto?          ✅ Completado     │   │
│  │  1.2 Gestión de proyectos          ✅ Completado     │   │
│  │  1.3 PMO y Roles                   🔄 En progreso    │   │
│  │  1.4 Fase: Iniciación              ⭕ Pendiente      │   │
│  │  1.5 Fase: Planificación           ⭕ Pendiente      │   │
│  │  1.6 Fases: Ejecución-Cierre       ⭕ Pendiente      │   │
│  │  1.7 Herramientas                  ⭕ Pendiente      │   │
│  │  ────────────────────────────────────────────────     │   │
│  │  📝 Quiz de Nivel                  🔒 Bloqueado      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  [Continuar donde lo dejé →]                                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## FASE 3: QUIZ DE PERFIL

### Estructura del Quiz

```javascript
// data/quiz-perfil.json
{
  "titulo": "Descubre tu Ruta de Aprendizaje",
  "preguntas": [
    {
      "id": 1,
      "pregunta": "¿Cuál describe mejor tu trabajo actual?",
      "opciones": [
        { "texto": "Escribo código / desarrollo software", "perfil": "programador", "peso": 3 },
        { "texto": "Tengo mi propio negocio / empresa", "perfil": "empresario", "peso": 3 },
        { "texto": "Trabajo con números / finanzas", "perfil": "contador", "peso": 3 },
        { "texto": "Creo contenido / campañas", "perfil": "marketer", "peso": 3 },
        { "texto": "Vendo productos / servicios", "perfil": "vendedor", "peso": 3 },
        { "texto": "Coordino proyectos / equipos", "perfil": "pm", "peso": 3 },
        { "texto": "Diseño / creo visuales", "perfil": "disenador", "peso": 3 },
        { "texto": "Estoy estudiando / cambiando de carrera", "perfil": "estudiante", "peso": 3 }
      ]
    },
    {
      "id": 2,
      "pregunta": "¿Cuánta experiencia tienes en gestión de proyectos?",
      "opciones": [
        { "texto": "Ninguna", "modificador": { "estudiante": 2 } },
        { "texto": "Básica (he participado en proyectos)", "modificador": {} },
        { "texto": "Intermedia (he liderado proyectos pequeños)", "modificador": { "pm": 1 } },
        { "texto": "Avanzada (gestiono proyectos regularmente)", "modificador": { "pm": 2 } }
      ]
    },
    {
      "id": 3,
      "pregunta": "¿Qué tanto conoces sobre Inteligencia Artificial?",
      "opciones": [
        { "texto": "Nada / muy poco", "modificador": { "estudiante": 1 } },
        { "texto": "He usado ChatGPT básicamente", "modificador": {} },
        { "texto": "Uso varias IAs en mi trabajo", "modificador": { "programador": 1, "marketer": 1 } },
        { "texto": "Soy avanzado en IA", "modificador": { "programador": 2 } }
      ]
    },
    {
      "id": 4,
      "pregunta": "¿Cuál es tu objetivo principal?",
      "opciones": [
        { "texto": "Aprender desde cero", "modificador": { "estudiante": 2 } },
        { "texto": "Ser más productivo en mi trabajo", "modificador": {} },
        { "texto": "Obtener una certificación", "modificador": { "pm": 2 } },
        { "texto": "Emprender / lanzar un proyecto", "modificador": { "empresario": 2 } }
      ]
    },
    {
      "id": 5,
      "pregunta": "¿Cuánto tiempo puedes dedicar por semana?",
      "opciones": [
        { "texto": "1-2 horas", "duracion": "corta" },
        { "texto": "3-5 horas", "duracion": "media" },
        { "texto": "6-10 horas", "duracion": "larga" },
        { "texto": "Más de 10 horas", "duracion": "intensiva" }
      ]
    }
  ]
}
```

### Algoritmo de Asignación

```javascript
// js/quiz.js
function calcularPerfil(respuestas) {
  const puntos = {
    programador: 0,
    empresario: 0,
    contador: 0,
    marketer: 0,
    vendedor: 0,
    pm: 0,
    disenador: 0,
    estudiante: 0
  };

  respuestas.forEach(respuesta => {
    // Sumar puntos base del perfil
    if (respuesta.perfil) {
      puntos[respuesta.perfil] += respuesta.peso;
    }

    // Aplicar modificadores
    if (respuesta.modificador) {
      Object.keys(respuesta.modificador).forEach(perfil => {
        puntos[perfil] += respuesta.modificador[perfil];
      });
    }
  });

  // Encontrar el perfil con más puntos
  const perfilGanador = Object.keys(puntos).reduce((a, b) =>
    puntos[a] > puntos[b] ? a : b
  );

  return {
    perfil: perfilGanador,
    puntos: puntos,
    confianza: calcularConfianza(puntos, perfilGanador)
  };
}
```

### Pantalla de Resultado

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│                    🎯 TU RUTA PAIDEIA                        │
│                                                              │
│         ┌─────────────────────────────────┐                  │
│         │      🖥️ PROGRAMADOR             │                  │
│         │      FULL STACK                 │                  │
│         └─────────────────────────────────┘                  │
│                                                              │
│    Tu ruta está optimizada para desarrolladores que          │
│    quieren multiplicar su productividad con IA.              │
│                                                              │
│    ⏱️ Duración estimada: 8-10 horas                          │
│    📚 Módulos seleccionados: 12                              │
│    🎓 Certificación: PAIDEIA Developer                       │
│                                                              │
│    ┌─────────────────────────────────────────────────┐       │
│    │  TU CAMINO:                                     │       │
│    │  N0 → N2.1 → N2.2 → N2.5 → N1.4 → N3.4 → N4.A  │       │
│    └─────────────────────────────────────────────────┘       │
│                                                              │
│         [VER MI RUTA COMPLETA]   [EMPEZAR AHORA →]          │
│                                                              │
│    ─────────────────────────────────────────────────         │
│    ¿No es tu perfil? [Cambiar perfil manualmente]            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## FASE 4: SISTEMA DE PROGRESO

### Modelo de Datos (localStorage)

```javascript
// Estructura guardada en localStorage
const progreso = {
  "usuario": {
    "perfil": "programador",
    "fechaInicio": "2025-11-29",
    "tiempoTotal": 0  // minutos
  },
  "niveles": {
    "nivel-0": {
      "completado": true,
      "modulos": {
        "bienvenida": { "completado": true, "fecha": "2025-11-29" },
        "quiz-perfil": { "completado": true, "fecha": "2025-11-29" },
        "tu-ruta": { "completado": true, "fecha": "2025-11-29" }
      }
    },
    "nivel-1": {
      "completado": false,
      "modulos": {
        "modulo-1-1": { "completado": true, "fecha": "2025-11-29" },
        "modulo-1-2": { "completado": true, "fecha": "2025-11-29" },
        "modulo-1-3": { "completado": false, "progreso": 60 },
        "modulo-1-4": { "completado": false },
        "modulo-1-5": { "completado": false },
        "modulo-1-6": { "completado": false },
        "modulo-1-7": { "completado": false }
      },
      "quiz": {
        "intentos": 0,
        "mejorPuntaje": null,
        "aprobado": false
      }
    },
    // ... más niveles
  },
  "certificaciones": {
    "nivel-1": null,
    "nivel-3": null,
    "nivel-5": null
  }
};
```

### Funciones de Progreso

```javascript
// js/progress.js

// Guardar progreso
function guardarProgreso(nivel, modulo, datos) {
  const progreso = JSON.parse(localStorage.getItem('paideia_progreso')) || {};
  progreso.niveles[nivel].modulos[modulo] = {
    ...progreso.niveles[nivel].modulos[modulo],
    ...datos,
    ultimaActualizacion: new Date().toISOString()
  };
  localStorage.setItem('paideia_progreso', JSON.stringify(progreso));
  actualizarUI();
}

// Calcular porcentaje total
function calcularProgresoTotal() {
  const progreso = JSON.parse(localStorage.getItem('paideia_progreso'));
  const totalModulos = contarTotalModulos();
  const completados = contarModulosCompletados(progreso);
  return Math.round((completados / totalModulos) * 100);
}

// Verificar si puede avanzar al siguiente nivel
function puedeAvanzar(nivel) {
  const progreso = JSON.parse(localStorage.getItem('paideia_progreso'));
  const nivelActual = progreso.niveles[nivel];

  // Todos los módulos completados
  const todosCompletados = Object.values(nivelActual.modulos)
    .every(m => m.completado);

  // Quiz aprobado (si aplica)
  const quizAprobado = nivelActual.quiz?.aprobado ?? true;

  return todosCompletados && quizAprobado;
}

// Desbloquear siguiente nivel
function desbloquearNivel(nivel) {
  const progreso = JSON.parse(localStorage.getItem('paideia_progreso'));
  progreso.niveles[nivel].bloqueado = false;
  localStorage.setItem('paideia_progreso', JSON.stringify(progreso));
}
```

### Visualización de Progreso

```html
<!-- componentes/progress-bar.html -->
<div class="progress-container">
  <div class="progress-header">
    <span class="progress-title">Tu Progreso</span>
    <span class="progress-percent" id="progress-percent">45%</span>
  </div>

  <div class="progress-bar-bg">
    <div class="progress-bar-fill" id="progress-fill" style="width: 45%"></div>
  </div>

  <div class="progress-levels">
    <div class="level-dot completed" data-level="0">N0</div>
    <div class="level-dot completed" data-level="1">N1</div>
    <div class="level-dot current" data-level="2">N2</div>
    <div class="level-dot locked" data-level="3">N3</div>
    <div class="level-dot locked" data-level="4">N4</div>
    <div class="level-dot locked" data-level="5">N5</div>
  </div>
</div>
```

---

## FASE 5: CERTIFICADOS

### Generación de Certificado (jsPDF)

```javascript
// js/certificate.js
async function generarCertificado(tipo, datos) {
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF('landscape', 'mm', 'a4');

  // Fondo
  doc.setFillColor(30, 58, 95); // paideia-primary
  doc.rect(0, 0, 297, 210, 'F');

  // Marco dorado
  doc.setDrawColor(245, 158, 11); // paideia-accent
  doc.setLineWidth(2);
  doc.rect(10, 10, 277, 190);

  // Logo PAIDEIA
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(24);
  doc.setTextColor(245, 158, 11);
  doc.text('PAIDEIA', 148.5, 35, { align: 'center' });

  // Subtítulo
  doc.setFontSize(12);
  doc.setTextColor(255, 255, 255);
  doc.text('Formación Profesional en Gestión de Proyectos + IA', 148.5, 45, { align: 'center' });

  // Certificado de
  doc.setFontSize(18);
  doc.text('CERTIFICADO DE COMPLETACIÓN', 148.5, 70, { align: 'center' });

  // Nombre
  doc.setFontSize(32);
  doc.setTextColor(245, 158, 11);
  doc.text(datos.nombre, 148.5, 95, { align: 'center' });

  // Descripción
  doc.setFontSize(14);
  doc.setTextColor(255, 255, 255);
  doc.text(`Ha completado exitosamente el programa`, 148.5, 115, { align: 'center' });

  // Nombre del programa
  doc.setFontSize(20);
  doc.setTextColor(6, 182, 212); // cyan
  doc.text(datos.programa, 148.5, 130, { align: 'center' });

  // Fecha y ID
  doc.setFontSize(10);
  doc.setTextColor(200, 200, 200);
  doc.text(`Fecha: ${datos.fecha}`, 50, 170);
  doc.text(`ID: ${datos.id}`, 50, 178);

  // Firma
  doc.text('Randhy Paul Rodriguez Santos', 247, 170, { align: 'right' });
  doc.text('Fundador, PAIDEIA', 247, 178, { align: 'right' });

  // Descargar
  doc.save(`Certificado_PAIDEIA_${datos.nombre.replace(' ', '_')}.pdf`);
}
```

---

## FASES DE DESARROLLO

### Sprint 1: Fundamentos (2-3 días)
```
□ Crear estructura de carpetas
□ Configurar app.html como SPA base
□ Implementar sistema de routing básico
□ Crear componentes navbar y sidebar
□ Implementar localStorage para progreso
```

### Sprint 2: Quiz y Rutas (2 días)
```
□ Crear quiz de perfil
□ Implementar algoritmo de asignación
□ Crear páginas de rutas personalizadas
□ Conectar quiz con sistema de progreso
```

### Sprint 3: Contenido Nivel 0-1 (3-4 días)
```
□ Migrar contenido de fundamentos.html
□ Dividir en módulos individuales
□ Crear quiz de Nivel 1
□ Implementar navegación entre módulos
```

### Sprint 4: Contenido Nivel 2-3 (3-4 días)
```
□ Migrar contenido de stack.html → Nivel 2
□ Migrar contenido de pmo.html → Nivel 3
□ Eliminar duplicaciones
□ Crear quizzes de nivel
```

### Sprint 5: Especialización y Certificados (2 días)
```
□ Crear tracks del Nivel 4
□ Implementar generador de certificados
□ Crear Nivel 5 con examen final
□ Testing completo
```

### Sprint 6: Pulido y Deploy (1-2 días)
```
□ Optimización de performance
□ Responsive design completo
□ Testing en múltiples dispositivos
□ Deploy a GitHub Pages
□ Documentación final
```

---

## ESTIMACIÓN TOTAL

| Fase | Duración | Entregable |
|------|----------|------------|
| Sprint 1 | 2-3 días | Estructura base funcional |
| Sprint 2 | 2 días | Quiz y rutas |
| Sprint 3 | 3-4 días | Niveles 0-1 completos |
| Sprint 4 | 3-4 días | Niveles 2-3 completos |
| Sprint 5 | 2 días | Niveles 4-5 + certificados |
| Sprint 6 | 1-2 días | Deploy final |
| **TOTAL** | **13-17 días** | **Plataforma completa** |

---

## TECNOLOGÍAS UTILIZADAS

```
FRONTEND:
├── HTML5 - Estructura
├── TailwindCSS - Estilos
├── JavaScript (Vanilla) - Lógica
├── Mermaid.js - Diagramas
└── jsPDF - Certificados

ALMACENAMIENTO:
├── localStorage - Progreso del usuario
└── JSON - Datos de cursos/quizzes

HOSTING:
└── GitHub Pages - Gratuito, SSL incluido

FUTURO (Migración):
├── Next.js - Framework React
├── Supabase - Base de datos + Auth
├── Stripe - Pagos
└── Vercel - Hosting
```

---

## DECISIONES PENDIENTES

### Requieren tu aprobación:

1. **¿Empezamos con HTML+JS o directamente Next.js?**
   - Recomiendo: HTML+JS para MVP rápido

2. **¿Mantenemos los 3 cursos originales como backup?**
   - Recomiendo: Sí, en carpeta `/legacy/`

3. **¿Quieres autenticación de usuarios?**
   - Sin auth: Progreso en localStorage (se pierde si cambia de navegador)
   - Con auth: Requiere backend (Supabase, Firebase)

4. **¿Certificados gratuitos o solo para plan premium?**
   - Opción A: Todos gratis
   - Opción B: Nivel 0-3 gratis, certificación de pago

---

## METADATOS

```yaml
ARCHIVO: PLAN_IMPLEMENTACION.md
UBICACIÓN: PROTOCOLOS/
VERSIÓN: 1.0.0
FECHA_CREACIÓN: 2025-11-29
CONSCIENCIA: PAIDEIA
PRERREQUISITOS:
  - ARQUITECTURA_PEDAGOGICA.md
  - RUTAS_DE_APRENDIZAJE.md
ESTADO: PROPUESTA
```

---

🧬💎∞ **PAIDEIA - Documentación completa antes de escribir una línea de código**

*"Mide dos veces, corta una vez."*

---

**Esperando tu aprobación para comenzar implementación.**

