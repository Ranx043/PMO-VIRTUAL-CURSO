# SPRINTS DETALLADOS - IMPLEMENTACIÓN PAIDEIA

**Fecha**: 2025-11-29
**Versión**: 1.0.0
**Consciencia**: PAIDEIA
**Metodología**: SOUL CORE (Doc First)

---

## ÍNDICE DE SPRINTS

| Sprint | Nombre | Duración | Entregable Principal |
|--------|--------|----------|---------------------|
| 1 | Fundamentos | 2-3 días | Estructura base + SPA |
| 2 | Quiz y Rutas | 2 días | Sistema de perfiles |
| 3 | Niveles 0-1 | 3-4 días | Contenido PM base |
| 4 | Niveles 2-3 | 3-4 días | Contenido IA + Integración |
| 5 | Niveles 4-5 | 2 días | Especialización + Certificación |
| 6 | Deploy | 1-2 días | Producción |

---

# SPRINT 1: FUNDAMENTOS

## Objetivo
Crear la estructura base de la aplicación con navegación funcional.

## Duración Estimada
2-3 días

## Tareas Detalladas

### TAREA 1.1: Crear Estructura de Carpetas

**Descripción**: Crear la estructura de directorios para la nueva plataforma.

**Comando**:
```bash
mkdir -p niveles/{nivel-0,nivel-1,nivel-2,nivel-3,nivel-4,nivel-5}
mkdir -p niveles/nivel-4/{track-desarrollo,track-marketing,track-salud,track-educacion}
mkdir -p rutas
mkdir -p componentes
mkdir -p data
mkdir -p assets/{images,icons,certificates}
mkdir -p legacy
```

**Resultado Esperado**:
```
PMO-VIRTUAL-CURSO/
├── niveles/
│   ├── nivel-0/
│   ├── nivel-1/
│   ├── nivel-2/
│   ├── nivel-3/
│   ├── nivel-4/
│   │   ├── track-desarrollo/
│   │   ├── track-marketing/
│   │   ├── track-salud/
│   │   └── track-educacion/
│   └── nivel-5/
├── rutas/
├── componentes/
├── data/
├── assets/
│   ├── images/
│   ├── icons/
│   └── certificates/
└── legacy/
```

**Criterio de Aceptación**:
- [ ] Todas las carpetas creadas
- [ ] Sin errores de permisos

---

### TAREA 1.2: Mover Cursos Originales a Legacy

**Descripción**: Respaldar los cursos originales antes de reorganizar.

**Comando**:
```bash
mv backups/fundamentos.html legacy/
mv backups/pmo.html legacy/
mv backups/stack.html legacy/
```

**Criterio de Aceptación**:
- [ ] Archivos movidos a /legacy/
- [ ] Carpeta backups puede eliminarse o mantenerse vacía

---

### TAREA 1.3: Crear app.html (Aplicación Principal)

**Descripción**: Crear la página principal de la aplicación (SPA-like).

**Archivo**: `app.html`

**Código**:
```html
<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PAIDEIA - Tu Ruta de Aprendizaje</title>

    <!-- SEO -->
    <meta name="description" content="Plataforma de aprendizaje en Gestión de Proyectos + Inteligencia Artificial">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Configuración Tailwind PAIDEIA -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'paideia': {
                            'dark': '#0f172a',
                            'primary': '#1e3a5f',
                            'secondary': '#3b82f6',
                            'accent': '#f59e0b',
                            'light': '#e0f2fe',
                            'cyan': '#06b6d4',
                        }
                    }
                }
            }
        }
    </script>

    <!-- Fuentes -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <!-- Mermaid para diagramas -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

    <!-- jsPDF para certificados -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

    <style>
        body { font-family: 'Inter', sans-serif; }

        /* Transiciones suaves */
        .fade-in { animation: fadeIn 0.3s ease-in; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Sidebar */
        .sidebar-item.active {
            background: linear-gradient(90deg, #1e3a5f 0%, transparent 100%);
            border-left: 4px solid #f59e0b;
        }

        /* Progress dots */
        .level-dot.completed { background-color: #10b981; }
        .level-dot.current { background-color: #f59e0b; animation: pulse 2s infinite; }
        .level-dot.locked { background-color: #6b7280; }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800">

    <!-- NAVBAR -->
    <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 bg-paideia-dark text-white shadow-lg">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <a href="index.html" class="flex items-center space-x-2">
                    <span class="text-2xl font-bold text-paideia-accent">PAIDEIA</span>
                </a>

                <!-- Nav Items -->
                <div class="hidden md:flex items-center space-x-6">
                    <a href="#" onclick="navegarA('nivel-0')" class="hover:text-paideia-accent transition">Inicio</a>
                    <a href="#" onclick="navegarA('mi-ruta')" class="hover:text-paideia-accent transition">Mi Ruta</a>
                    <a href="#" onclick="navegarA('progreso')" class="hover:text-paideia-accent transition">Progreso</a>
                </div>

                <!-- User Progress -->
                <div class="flex items-center space-x-4">
                    <div class="text-sm">
                        <span class="text-slate-400">Progreso:</span>
                        <span id="nav-progress" class="font-bold text-paideia-accent">0%</span>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- LAYOUT PRINCIPAL -->
    <div class="flex pt-16">

        <!-- SIDEBAR -->
        <aside id="sidebar" class="fixed left-0 top-16 h-[calc(100vh-4rem)] w-64 bg-white border-r border-slate-200 overflow-y-auto">

            <!-- Perfil del Usuario -->
            <div class="p-4 border-b border-slate-200">
                <p class="text-xs text-slate-500 uppercase tracking-wider">Tu Perfil</p>
                <p id="sidebar-perfil" class="font-semibold text-paideia-primary">Sin definir</p>
                <button onclick="navegarA('quiz-perfil')" class="text-xs text-paideia-cyan hover:underline">
                    Cambiar perfil
                </button>
            </div>

            <!-- Niveles -->
            <nav class="p-4">
                <p class="text-xs text-slate-500 uppercase tracking-wider mb-3">Niveles</p>

                <div id="sidebar-niveles" class="space-y-1">
                    <!-- Se genera dinámicamente -->
                </div>
            </nav>

            <!-- Barra de Progreso -->
            <div class="p-4 border-t border-slate-200">
                <p class="text-xs text-slate-500 uppercase tracking-wider mb-2">Progreso Total</p>
                <div class="w-full bg-slate-200 rounded-full h-2">
                    <div id="sidebar-progress-bar" class="bg-paideia-accent h-2 rounded-full transition-all duration-500" style="width: 0%"></div>
                </div>
                <p class="text-right text-sm font-semibold text-paideia-primary mt-1">
                    <span id="sidebar-progress-text">0%</span>
                </p>
            </div>

        </aside>

        <!-- CONTENIDO PRINCIPAL -->
        <main id="content" class="ml-64 flex-1 min-h-[calc(100vh-4rem)] p-8">

            <!-- Aquí se carga el contenido dinámicamente -->
            <div id="content-area" class="max-w-4xl mx-auto fade-in">
                <!-- Contenido inicial: Bienvenida -->
                <div class="text-center py-16">
                    <h1 class="text-4xl font-bold text-paideia-primary mb-4">
                        Bienvenido a PAIDEIA
                    </h1>
                    <p class="text-xl text-slate-600 mb-8">
                        Tu viaje de aprendizaje comienza aquí
                    </p>
                    <button onclick="navegarA('nivel-0/bienvenida')"
                            class="px-8 py-4 bg-paideia-accent text-white font-semibold rounded-lg hover:bg-amber-600 transition">
                        Comenzar Ahora
                    </button>
                </div>
            </div>

        </main>
    </div>

    <!-- SCRIPTS -->
    <script src="js/data.js"></script>
    <script src="js/progress.js"></script>
    <script src="js/router.js"></script>
    <script src="js/app.js"></script>

    <script>
        // Inicializar aplicación
        document.addEventListener('DOMContentLoaded', () => {
            inicializarApp();
        });
    </script>

</body>
</html>
```

**Criterio de Aceptación**:
- [ ] Página carga sin errores
- [ ] Navbar visible y fijo
- [ ] Sidebar visible con secciones
- [ ] Área de contenido responsiva

---

### TAREA 1.4: Crear js/data.js (Datos de la Aplicación)

**Descripción**: Archivo con la estructura de datos de niveles y módulos.

**Archivo**: `js/data.js`

**Código**:
```javascript
/**
 * PAIDEIA - Datos de la Aplicación
 * Estructura de niveles, módulos y rutas
 */

const PAIDEIA_DATA = {

    // Información general
    version: "1.0.0",
    nombre: "PAIDEIA",

    // Niveles del programa
    niveles: [
        {
            id: "nivel-0",
            nombre: "Despertar",
            descripcion: "Introducción a PAIDEIA",
            icono: "🌅",
            duracion: "15 min",
            bloqueado: false,
            modulos: [
                { id: "bienvenida", nombre: "Bienvenida", duracion: "5 min" },
                { id: "quiz-perfil", nombre: "Descubre tu Perfil", duracion: "5 min" },
                { id: "tu-ruta", nombre: "Tu Ruta Personalizada", duracion: "5 min" }
            ]
        },
        {
            id: "nivel-1",
            nombre: "Fundamentos PM",
            descripcion: "Base sólida en gestión de proyectos",
            icono: "📊",
            duracion: "2-3 horas",
            bloqueado: false,
            prerequisito: "nivel-0",
            modulos: [
                { id: "modulo-1-1", nombre: "¿Qué es un Proyecto?", duracion: "20 min" },
                { id: "modulo-1-2", nombre: "Gestión de Proyectos", duracion: "25 min" },
                { id: "modulo-1-3", nombre: "PMO y Roles", duracion: "20 min" },
                { id: "modulo-1-4", nombre: "Fase: Iniciación", duracion: "25 min" },
                { id: "modulo-1-5", nombre: "Fase: Planificación", duracion: "30 min" },
                { id: "modulo-1-6", nombre: "Fases: Ejecución-Cierre", duracion: "25 min" },
                { id: "modulo-1-7", nombre: "Herramientas Esenciales", duracion: "30 min" },
                { id: "quiz-nivel-1", nombre: "Evaluación Nivel 1", duracion: "15 min", esQuiz: true }
            ]
        },
        {
            id: "nivel-2",
            nombre: "Herramientas IA",
            descripcion: "Domina el ecosistema de IA",
            icono: "🤖",
            duracion: "2 horas",
            bloqueado: true,
            prerequisito: "nivel-1",
            modulos: [
                { id: "modulo-2-1", nombre: "¿Qué es IA?", duracion: "15 min" },
                { id: "modulo-2-2", nombre: "Tokens y Costos", duracion: "20 min" },
                { id: "modulo-2-3", nombre: "Tipos de IA", duracion: "25 min" },
                { id: "modulo-2-4", nombre: "Las 10 IAs Esenciales", duracion: "30 min" },
                { id: "modulo-2-5", nombre: "Prompt Engineering", duracion: "25 min" },
                { id: "modulo-2-6", nombre: "Tu Primer Prompt", duracion: "15 min" },
                { id: "quiz-nivel-2", nombre: "Evaluación Nivel 2", duracion: "10 min", esQuiz: true }
            ]
        },
        {
            id: "nivel-3",
            nombre: "PMO + IA",
            descripcion: "Integración completa",
            icono: "🚀",
            duracion: "3-4 horas",
            bloqueado: true,
            prerequisito: "nivel-2",
            modulos: [
                { id: "modulo-3-1", nombre: "¿Qué es PMO Virtual?", duracion: "20 min" },
                { id: "modulo-3-2", nombre: "Iniciación con IA", duracion: "30 min" },
                { id: "modulo-3-3", nombre: "Planificación con IA", duracion: "40 min" },
                { id: "modulo-3-4", nombre: "Ejecución con IA", duracion: "35 min" },
                { id: "modulo-3-5", nombre: "Monitoreo con IA", duracion: "25 min" },
                { id: "modulo-3-6", nombre: "Cierre con IA", duracion: "20 min" },
                { id: "modulo-3-7", nombre: "Templates y Prompts", duracion: "30 min" },
                { id: "quiz-nivel-3", nombre: "Evaluación Nivel 3", duracion: "15 min", esQuiz: true }
            ]
        },
        {
            id: "nivel-4",
            nombre: "Especialización",
            descripcion: "Tu sector específico",
            icono: "🎯",
            duracion: "2 horas",
            bloqueado: true,
            prerequisito: "nivel-3",
            tracks: [
                { id: "track-desarrollo", nombre: "Desarrollo", icono: "💻" },
                { id: "track-marketing", nombre: "Marketing", icono: "📱" },
                { id: "track-salud", nombre: "Salud", icono: "🏥" },
                { id: "track-educacion", nombre: "Educación", icono: "📚" }
            ]
        },
        {
            id: "nivel-5",
            nombre: "Certificación",
            descripcion: "Valida tus competencias",
            icono: "🎓",
            duracion: "Variable",
            bloqueado: true,
            prerequisito: "nivel-4",
            modulos: [
                { id: "examen-final", nombre: "Examen Final", duracion: "60 min" },
                { id: "proyecto-final", nombre: "Proyecto Final", duracion: "Variable" },
                { id: "certificado", nombre: "Tu Certificado", duracion: "5 min" }
            ]
        }
    ],

    // Perfiles disponibles
    perfiles: [
        { id: "programador", nombre: "Programador Full Stack", icono: "🖥️" },
        { id: "empresario", nombre: "Empresario", icono: "💼" },
        { id: "contador", nombre: "Contador", icono: "📊" },
        { id: "marketer", nombre: "Marketer Digital", icono: "📱" },
        { id: "vendedor", nombre: "Vendedor", icono: "🤝" },
        { id: "pm", nombre: "Project Manager", icono: "📋" },
        { id: "disenador", nombre: "Diseñador", icono: "🎨" },
        { id: "estudiante", nombre: "Estudiante", icono: "📚" }
    ],

    // Rutas por perfil (módulos recomendados en orden)
    rutas: {
        programador: ["nivel-0", "modulo-2-2", "modulo-2-4", "modulo-2-5", "modulo-1-4", "modulo-3-4", "track-desarrollo"],
        empresario: ["nivel-0", "nivel-1", "modulo-2-1", "modulo-3-1", "modulo-3-2", "modulo-3-7"],
        contador: ["nivel-0", "modulo-1-2", "modulo-1-6", "modulo-2-1", "modulo-2-2", "modulo-3-5"],
        marketer: ["nivel-0", "modulo-1-4", "modulo-2-1", "modulo-2-3", "modulo-2-5", "modulo-3-4", "track-marketing"],
        vendedor: ["nivel-0", "modulo-1-3", "modulo-1-4", "modulo-2-1", "modulo-3-7"],
        pm: ["nivel-0", "nivel-1", "nivel-2", "nivel-3", "nivel-4", "nivel-5"],
        disenador: ["nivel-0", "modulo-1-6", "modulo-2-3", "modulo-2-5", "modulo-3-4"],
        estudiante: ["nivel-0", "nivel-1", "nivel-2", "nivel-3"]
    }
};

// Exportar para uso global
window.PAIDEIA_DATA = PAIDEIA_DATA;
```

**Criterio de Aceptación**:
- [ ] Archivo carga sin errores
- [ ] Datos accesibles globalmente
- [ ] Estructura coherente con arquitectura

---

### TAREA 1.5: Crear js/progress.js (Sistema de Progreso)

**Descripción**: Funciones para guardar y recuperar progreso del usuario.

**Archivo**: `js/progress.js`

**Código**:
```javascript
/**
 * PAIDEIA - Sistema de Progreso
 * Manejo de localStorage para tracking del usuario
 */

const STORAGE_KEY = 'paideia_progreso';

// Estado inicial del progreso
const PROGRESO_INICIAL = {
    usuario: {
        perfil: null,
        fechaInicio: null,
        tiempoTotal: 0
    },
    niveles: {
        "nivel-0": { completado: false, modulos: {} },
        "nivel-1": { completado: false, modulos: {}, quiz: { intentos: 0, aprobado: false } },
        "nivel-2": { completado: false, modulos: {}, quiz: { intentos: 0, aprobado: false } },
        "nivel-3": { completado: false, modulos: {}, quiz: { intentos: 0, aprobado: false } },
        "nivel-4": { completado: false, tracks: {} },
        "nivel-5": { completado: false, examen: null, proyecto: null }
    },
    certificaciones: []
};

/**
 * Obtener progreso actual
 */
function obtenerProgreso() {
    const guardado = localStorage.getItem(STORAGE_KEY);
    if (guardado) {
        return JSON.parse(guardado);
    }
    return { ...PROGRESO_INICIAL };
}

/**
 * Guardar progreso
 */
function guardarProgreso(progreso) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progreso));
    actualizarUIProgreso();
}

/**
 * Reiniciar progreso (con confirmación)
 */
function reiniciarProgreso() {
    if (confirm('¿Estás seguro de reiniciar todo tu progreso? Esta acción no se puede deshacer.')) {
        localStorage.removeItem(STORAGE_KEY);
        location.reload();
    }
}

/**
 * Marcar módulo como completado
 */
function completarModulo(nivelId, moduloId) {
    const progreso = obtenerProgreso();

    if (!progreso.niveles[nivelId].modulos) {
        progreso.niveles[nivelId].modulos = {};
    }

    progreso.niveles[nivelId].modulos[moduloId] = {
        completado: true,
        fecha: new Date().toISOString()
    };

    // Verificar si el nivel está completo
    verificarNivelCompleto(progreso, nivelId);

    guardarProgreso(progreso);
    return progreso;
}

/**
 * Verificar si todos los módulos de un nivel están completos
 */
function verificarNivelCompleto(progreso, nivelId) {
    const nivelData = PAIDEIA_DATA.niveles.find(n => n.id === nivelId);
    if (!nivelData || !nivelData.modulos) return;

    const modulosRequeridos = nivelData.modulos.filter(m => !m.esQuiz);
    const modulosCompletados = Object.keys(progreso.niveles[nivelId].modulos || {})
        .filter(id => progreso.niveles[nivelId].modulos[id].completado);

    const todosCompletos = modulosRequeridos.every(m =>
        modulosCompletados.includes(m.id)
    );

    // También verificar quiz si existe
    const tieneQuiz = nivelData.modulos.some(m => m.esQuiz);
    const quizAprobado = !tieneQuiz || progreso.niveles[nivelId].quiz?.aprobado;

    if (todosCompletos && quizAprobado) {
        progreso.niveles[nivelId].completado = true;
        desbloquearSiguienteNivel(progreso, nivelId);
    }
}

/**
 * Desbloquear el siguiente nivel
 */
function desbloquearSiguienteNivel(progreso, nivelActualId) {
    const niveles = PAIDEIA_DATA.niveles;
    const indiceActual = niveles.findIndex(n => n.id === nivelActualId);

    if (indiceActual < niveles.length - 1) {
        const siguienteNivel = niveles[indiceActual + 1];
        // El desbloqueo se maneja en la UI, no en los datos
        console.log(`Nivel desbloqueado: ${siguienteNivel.nombre}`);
    }
}

/**
 * Establecer perfil del usuario
 */
function establecerPerfil(perfilId) {
    const progreso = obtenerProgreso();
    progreso.usuario.perfil = perfilId;

    if (!progreso.usuario.fechaInicio) {
        progreso.usuario.fechaInicio = new Date().toISOString();
    }

    guardarProgreso(progreso);
    return progreso;
}

/**
 * Calcular porcentaje de progreso total
 */
function calcularProgresoTotal() {
    const progreso = obtenerProgreso();
    let totalModulos = 0;
    let completados = 0;

    PAIDEIA_DATA.niveles.forEach(nivel => {
        if (nivel.modulos) {
            totalModulos += nivel.modulos.length;

            const modulosNivel = progreso.niveles[nivel.id]?.modulos || {};
            completados += Object.values(modulosNivel).filter(m => m.completado).length;
        }
    });

    return totalModulos > 0 ? Math.round((completados / totalModulos) * 100) : 0;
}

/**
 * Verificar si un nivel está bloqueado
 */
function nivelEstaBloqueado(nivelId) {
    const nivel = PAIDEIA_DATA.niveles.find(n => n.id === nivelId);
    if (!nivel || !nivel.prerequisito) return false;

    const progreso = obtenerProgreso();
    const prerequisito = progreso.niveles[nivel.prerequisito];

    return !prerequisito?.completado;
}

/**
 * Actualizar UI con el progreso actual
 */
function actualizarUIProgreso() {
    const progreso = obtenerProgreso();
    const porcentaje = calcularProgresoTotal();

    // Actualizar navbar
    const navProgress = document.getElementById('nav-progress');
    if (navProgress) navProgress.textContent = `${porcentaje}%`;

    // Actualizar sidebar
    const sidebarProgressBar = document.getElementById('sidebar-progress-bar');
    const sidebarProgressText = document.getElementById('sidebar-progress-text');

    if (sidebarProgressBar) sidebarProgressBar.style.width = `${porcentaje}%`;
    if (sidebarProgressText) sidebarProgressText.textContent = `${porcentaje}%`;

    // Actualizar perfil en sidebar
    const sidebarPerfil = document.getElementById('sidebar-perfil');
    if (sidebarPerfil && progreso.usuario.perfil) {
        const perfil = PAIDEIA_DATA.perfiles.find(p => p.id === progreso.usuario.perfil);
        if (perfil) {
            sidebarPerfil.textContent = `${perfil.icono} ${perfil.nombre}`;
        }
    }

    // Actualizar lista de niveles en sidebar
    renderizarSidebarNiveles();
}

/**
 * Renderizar niveles en el sidebar
 */
function renderizarSidebarNiveles() {
    const container = document.getElementById('sidebar-niveles');
    if (!container) return;

    const progreso = obtenerProgreso();

    container.innerHTML = PAIDEIA_DATA.niveles.map(nivel => {
        const nivelProgreso = progreso.niveles[nivel.id];
        const bloqueado = nivelEstaBloqueado(nivel.id);

        let estado = '⭕';
        let clase = '';

        if (bloqueado) {
            estado = '🔒';
            clase = 'opacity-50 cursor-not-allowed';
        } else if (nivelProgreso?.completado) {
            estado = '✅';
            clase = 'bg-green-50';
        } else if (Object.keys(nivelProgreso?.modulos || {}).length > 0) {
            estado = '🔄';
            clase = 'bg-amber-50';
        }

        return `
            <a href="#"
               onclick="${bloqueado ? 'return false' : `navegarA('${nivel.id}')`}"
               class="sidebar-item flex items-center justify-between p-3 rounded-lg hover:bg-slate-100 transition ${clase}">
                <span class="flex items-center space-x-2">
                    <span>${nivel.icono}</span>
                    <span class="text-sm font-medium">${nivel.nombre}</span>
                </span>
                <span>${estado}</span>
            </a>
        `;
    }).join('');
}

// Exportar funciones
window.obtenerProgreso = obtenerProgreso;
window.guardarProgreso = guardarProgreso;
window.completarModulo = completarModulo;
window.establecerPerfil = establecerPerfil;
window.calcularProgresoTotal = calcularProgresoTotal;
window.nivelEstaBloqueado = nivelEstaBloqueado;
window.actualizarUIProgreso = actualizarUIProgreso;
window.reiniciarProgreso = reiniciarProgreso;
```

**Criterio de Aceptación**:
- [ ] Progreso se guarda en localStorage
- [ ] Progreso persiste entre sesiones
- [ ] UI se actualiza al cambiar progreso

---

### TAREA 1.6: Crear js/router.js (Navegación SPA)

**Descripción**: Sistema de routing para navegación sin recargar página.

**Archivo**: `js/router.js`

**Código**:
```javascript
/**
 * PAIDEIA - Router SPA
 * Navegación sin recarga de página
 */

// Historial de navegación
let historialNavegacion = [];

/**
 * Navegar a una sección/módulo
 */
async function navegarA(ruta) {
    console.log('Navegando a:', ruta);

    // Verificar si está bloqueado
    const partes = ruta.split('/');
    const nivelId = partes[0];

    if (nivelEstaBloqueado(nivelId)) {
        mostrarMensaje('Este nivel está bloqueado. Completa el nivel anterior primero.', 'warning');
        return;
    }

    // Guardar en historial
    historialNavegacion.push(ruta);

    // Actualizar URL (sin recargar)
    window.history.pushState({ ruta }, '', `#${ruta}`);

    // Cargar contenido
    await cargarContenido(ruta);

    // Actualizar sidebar (marcar activo)
    actualizarSidebarActivo(nivelId);
}

/**
 * Cargar contenido de un módulo
 */
async function cargarContenido(ruta) {
    const contentArea = document.getElementById('content-area');
    if (!contentArea) return;

    // Mostrar loading
    contentArea.innerHTML = `
        <div class="flex items-center justify-center py-16">
            <div class="animate-spin rounded-full h-12 w-12 border-4 border-paideia-accent border-t-transparent"></div>
        </div>
    `;

    try {
        // Construir ruta del archivo
        const archivoHTML = construirRutaArchivo(ruta);

        // Intentar cargar el archivo
        const response = await fetch(archivoHTML);

        if (response.ok) {
            const html = await response.text();
            contentArea.innerHTML = `<div class="fade-in">${html}</div>`;

            // Inicializar Mermaid si hay diagramas
            if (html.includes('class="mermaid"')) {
                mermaid.init(undefined, '.mermaid');
            }
        } else {
            // Mostrar contenido placeholder
            contentArea.innerHTML = generarPlaceholder(ruta);
        }

    } catch (error) {
        console.error('Error cargando contenido:', error);
        contentArea.innerHTML = generarPlaceholder(ruta);
    }

    // Scroll al top
    window.scrollTo(0, 0);
}

/**
 * Construir ruta del archivo HTML
 */
function construirRutaArchivo(ruta) {
    const partes = ruta.split('/');

    if (partes.length === 1) {
        // Es un nivel: niveles/nivel-X/index.html
        return `niveles/${ruta}/index.html`;
    } else {
        // Es un módulo: niveles/nivel-X/modulo.html
        return `niveles/${partes[0]}/${partes[1]}.html`;
    }
}

/**
 * Generar placeholder para contenido no disponible
 */
function generarPlaceholder(ruta) {
    const partes = ruta.split('/');
    const nivelId = partes[0];
    const moduloId = partes[1] || 'index';

    // Buscar información del nivel/módulo
    const nivel = PAIDEIA_DATA.niveles.find(n => n.id === nivelId);
    let titulo = nivel?.nombre || ruta;
    let descripcion = nivel?.descripcion || '';

    if (moduloId !== 'index' && nivel?.modulos) {
        const modulo = nivel.modulos.find(m => m.id === moduloId);
        if (modulo) {
            titulo = modulo.nombre;
            descripcion = `Parte de ${nivel.nombre}`;
        }
    }

    return `
        <div class="fade-in">
            <div class="bg-white rounded-xl shadow-lg p-8 max-w-2xl mx-auto">
                <div class="text-center mb-8">
                    <span class="text-6xl">${nivel?.icono || '📄'}</span>
                    <h1 class="text-3xl font-bold text-paideia-primary mt-4">${titulo}</h1>
                    <p class="text-slate-600 mt-2">${descripcion}</p>
                </div>

                <div class="bg-amber-50 border border-amber-200 rounded-lg p-4 mb-6">
                    <p class="text-amber-800">
                        <strong>🚧 Contenido en desarrollo</strong><br>
                        Este módulo estará disponible próximamente.
                    </p>
                </div>

                ${nivel?.modulos ? `
                    <div class="border-t pt-6">
                        <h3 class="font-semibold text-lg mb-4">Módulos de este nivel:</h3>
                        <ul class="space-y-2">
                            ${nivel.modulos.map(m => `
                                <li class="flex items-center justify-between p-3 bg-slate-50 rounded-lg">
                                    <span>${m.nombre}</span>
                                    <span class="text-sm text-slate-500">${m.duracion}</span>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                ` : ''}

                <div class="flex justify-between mt-8">
                    <button onclick="navegarAtras()"
                            class="px-4 py-2 text-slate-600 hover:text-paideia-primary transition">
                        ← Atrás
                    </button>
                    <button onclick="marcarComoCompletado('${nivelId}', '${moduloId}')"
                            class="px-6 py-2 bg-paideia-accent text-white rounded-lg hover:bg-amber-600 transition">
                        Marcar como completado
                    </button>
                </div>
            </div>
        </div>
    `;
}

/**
 * Navegar hacia atrás
 */
function navegarAtras() {
    if (historialNavegacion.length > 1) {
        historialNavegacion.pop(); // Quitar actual
        const anterior = historialNavegacion.pop(); // Obtener anterior
        navegarA(anterior);
    } else {
        navegarA('nivel-0');
    }
}

/**
 * Marcar módulo como completado y avanzar
 */
function marcarComoCompletado(nivelId, moduloId) {
    completarModulo(nivelId, moduloId);
    mostrarMensaje('¡Módulo completado!', 'success');

    // Buscar siguiente módulo
    const nivel = PAIDEIA_DATA.niveles.find(n => n.id === nivelId);
    if (nivel?.modulos) {
        const indice = nivel.modulos.findIndex(m => m.id === moduloId);
        if (indice < nivel.modulos.length - 1) {
            const siguiente = nivel.modulos[indice + 1];
            setTimeout(() => navegarA(`${nivelId}/${siguiente.id}`), 1000);
        } else {
            // Era el último módulo del nivel
            mostrarMensaje('¡Has completado todos los módulos de este nivel!', 'success');
        }
    }
}

/**
 * Actualizar elemento activo en sidebar
 */
function actualizarSidebarActivo(nivelId) {
    document.querySelectorAll('.sidebar-item').forEach(item => {
        item.classList.remove('active');
    });

    const activo = document.querySelector(`[onclick*="${nivelId}"]`);
    if (activo) {
        activo.classList.add('active');
    }
}

/**
 * Mostrar mensaje temporal
 */
function mostrarMensaje(texto, tipo = 'info') {
    const colores = {
        success: 'bg-green-500',
        warning: 'bg-amber-500',
        error: 'bg-red-500',
        info: 'bg-blue-500'
    };

    const mensaje = document.createElement('div');
    mensaje.className = `fixed bottom-4 right-4 ${colores[tipo]} text-white px-6 py-3 rounded-lg shadow-lg z-50 fade-in`;
    mensaje.textContent = texto;

    document.body.appendChild(mensaje);

    setTimeout(() => {
        mensaje.remove();
    }, 3000);
}

// Manejar navegación del navegador (botón atrás)
window.addEventListener('popstate', (event) => {
    if (event.state?.ruta) {
        cargarContenido(event.state.ruta);
    }
});

// Exportar funciones
window.navegarA = navegarA;
window.navegarAtras = navegarAtras;
window.marcarComoCompletado = marcarComoCompletado;
window.mostrarMensaje = mostrarMensaje;
```

**Criterio de Aceptación**:
- [ ] Navegación funciona sin recargar página
- [ ] URL se actualiza al navegar
- [ ] Botón atrás del navegador funciona
- [ ] Contenido se carga dinámicamente

---

### TAREA 1.7: Crear js/app.js (Inicialización)

**Descripción**: Archivo principal que inicializa la aplicación.

**Archivo**: `js/app.js`

**Código**:
```javascript
/**
 * PAIDEIA - Aplicación Principal
 * Inicialización y coordinación
 */

/**
 * Inicializar la aplicación
 */
function inicializarApp() {
    console.log('🎓 PAIDEIA v' + PAIDEIA_DATA.version + ' iniciando...');

    // Inicializar Mermaid
    mermaid.initialize({ startOnLoad: true, theme: 'default' });

    // Cargar progreso guardado
    const progreso = obtenerProgreso();

    // Actualizar UI con progreso
    actualizarUIProgreso();

    // Verificar si hay hash en URL
    const hash = window.location.hash.slice(1);
    if (hash) {
        navegarA(hash);
    } else if (progreso.usuario.perfil) {
        // Usuario ya tiene perfil, ir a su nivel actual
        const nivelActual = encontrarNivelActual(progreso);
        navegarA(nivelActual);
    } else {
        // Usuario nuevo, ir a bienvenida
        navegarA('nivel-0/bienvenida');
    }

    console.log('✅ PAIDEIA inicializada correctamente');
}

/**
 * Encontrar el nivel actual del usuario
 */
function encontrarNivelActual(progreso) {
    for (const nivel of PAIDEIA_DATA.niveles) {
        const nivelProgreso = progreso.niveles[nivel.id];

        if (!nivelProgreso?.completado) {
            return nivel.id;
        }
    }

    // Todos completados, ir a certificación
    return 'nivel-5';
}

/**
 * Obtener estadísticas del usuario
 */
function obtenerEstadisticas() {
    const progreso = obtenerProgreso();

    let modulosCompletados = 0;
    let totalModulos = 0;
    let nivelesCompletados = 0;

    PAIDEIA_DATA.niveles.forEach(nivel => {
        if (nivel.modulos) {
            totalModulos += nivel.modulos.length;

            const modulosNivel = progreso.niveles[nivel.id]?.modulos || {};
            modulosCompletados += Object.values(modulosNivel).filter(m => m.completado).length;
        }

        if (progreso.niveles[nivel.id]?.completado) {
            nivelesCompletados++;
        }
    });

    return {
        modulosCompletados,
        totalModulos,
        nivelesCompletados,
        totalNiveles: PAIDEIA_DATA.niveles.length,
        porcentaje: calcularProgresoTotal(),
        perfil: progreso.usuario.perfil,
        fechaInicio: progreso.usuario.fechaInicio
    };
}

/**
 * Modo debug - mostrar estado actual
 */
function debug() {
    console.group('🔍 PAIDEIA Debug');
    console.log('Progreso:', obtenerProgreso());
    console.log('Estadísticas:', obtenerEstadisticas());
    console.log('Datos:', PAIDEIA_DATA);
    console.groupEnd();
}

// Exportar funciones
window.inicializarApp = inicializarApp;
window.obtenerEstadisticas = obtenerEstadisticas;
window.debug = debug;
```

**Criterio de Aceptación**:
- [ ] App inicializa sin errores
- [ ] Progreso se carga al inicio
- [ ] Navegación automática según estado del usuario

---

### TAREA 1.8: Actualizar index.html (Landing Page)

**Descripción**: Agregar botón que enlaza a app.html.

**Archivo**: `index.html`

**Cambio**: Modificar el botón "Empezar Ahora" para que enlace a `app.html`

```html
<!-- Cambiar de: -->
<a href="#pricing">Empezar Ahora</a>

<!-- A: -->
<a href="app.html">Empezar Ahora</a>
```

**Criterio de Aceptación**:
- [ ] Botón lleva a app.html
- [ ] Transición fluida entre páginas

---

## ENTREGABLES SPRINT 1

| # | Archivo | Estado |
|---|---------|--------|
| 1 | Estructura de carpetas | ⬜ |
| 2 | legacy/ con cursos originales | ⬜ |
| 3 | app.html | ⬜ |
| 4 | js/data.js | ⬜ |
| 5 | js/progress.js | ⬜ |
| 6 | js/router.js | ⬜ |
| 7 | js/app.js | ⬜ |
| 8 | index.html actualizado | ⬜ |

## CRITERIOS DE ACEPTACIÓN SPRINT 1

- [ ] Usuario puede acceder a app.html desde landing
- [ ] Sidebar muestra lista de niveles
- [ ] Navegación entre secciones funciona
- [ ] Progreso se guarda en localStorage
- [ ] Progreso persiste entre sesiones
- [ ] UI se actualiza al completar módulos

---

# SPRINT 2: QUIZ Y RUTAS

## Objetivo
Implementar el sistema de quiz de perfil y rutas personalizadas.

## Duración Estimada
2 días

## Tareas Detalladas

### TAREA 2.1: Crear data/quiz-perfil.json

**Descripción**: Archivo JSON con las preguntas del quiz de perfil.

**Archivo**: `data/quiz-perfil.json`

**Código**:
```json
{
  "titulo": "Descubre tu Ruta de Aprendizaje",
  "descripcion": "Responde 5 preguntas para personalizar tu experiencia",
  "preguntas": [
    {
      "id": 1,
      "pregunta": "¿Cuál describe mejor tu trabajo actual?",
      "opciones": [
        { "texto": "Escribo código / desarrollo software", "perfil": "programador", "peso": 3 },
        { "texto": "Tengo mi propio negocio / empresa", "perfil": "empresario", "peso": 3 },
        { "texto": "Trabajo con números / finanzas / contabilidad", "perfil": "contador", "peso": 3 },
        { "texto": "Creo contenido / campañas de marketing", "perfil": "marketer", "peso": 3 },
        { "texto": "Vendo productos o servicios", "perfil": "vendedor", "peso": 3 },
        { "texto": "Coordino proyectos o equipos", "perfil": "pm", "peso": 3 },
        { "texto": "Diseño / creo cosas visuales", "perfil": "disenador", "peso": 3 },
        { "texto": "Estoy estudiando o cambiando de carrera", "perfil": "estudiante", "peso": 3 }
      ]
    },
    {
      "id": 2,
      "pregunta": "¿Cuánta experiencia tienes en gestión de proyectos?",
      "opciones": [
        { "texto": "Ninguna - Soy completamente nuevo", "modificador": { "estudiante": 2 } },
        { "texto": "Básica - He participado en proyectos", "modificador": {} },
        { "texto": "Intermedia - He liderado proyectos pequeños", "modificador": { "pm": 1 } },
        { "texto": "Avanzada - Gestiono proyectos regularmente", "modificador": { "pm": 2 } }
      ]
    },
    {
      "id": 3,
      "pregunta": "¿Qué tanto conoces sobre Inteligencia Artificial?",
      "opciones": [
        { "texto": "Nada o muy poco", "modificador": { "estudiante": 1 } },
        { "texto": "He usado ChatGPT de forma básica", "modificador": {} },
        { "texto": "Uso varias IAs en mi trabajo", "modificador": { "programador": 1, "marketer": 1 } },
        { "texto": "Soy usuario avanzado de IA", "modificador": { "programador": 2 } }
      ]
    },
    {
      "id": 4,
      "pregunta": "¿Cuál es tu objetivo principal con PAIDEIA?",
      "opciones": [
        { "texto": "Aprender desde cero", "modificador": { "estudiante": 2 } },
        { "texto": "Ser más productivo en mi trabajo actual", "modificador": {} },
        { "texto": "Obtener una certificación profesional", "modificador": { "pm": 2 } },
        { "texto": "Emprender o lanzar un proyecto propio", "modificador": { "empresario": 2 } },
        { "texto": "Automatizar tareas repetitivas", "modificador": { "programador": 1, "contador": 1 } }
      ]
    },
    {
      "id": 5,
      "pregunta": "¿Cuánto tiempo puedes dedicar por semana al aprendizaje?",
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

---

### TAREA 2.2: Crear js/quiz.js

**Descripción**: Lógica del quiz de selección de perfil.

**Archivo**: `js/quiz.js`

**Código**:
```javascript
/**
 * PAIDEIA - Sistema de Quiz
 * Quiz de perfil y evaluaciones
 */

let quizData = null;
let respuestasQuiz = [];
let preguntaActual = 0;

/**
 * Cargar datos del quiz de perfil
 */
async function cargarQuizPerfil() {
    try {
        const response = await fetch('data/quiz-perfil.json');
        quizData = await response.json();
        return quizData;
    } catch (error) {
        console.error('Error cargando quiz:', error);
        return null;
    }
}

/**
 * Iniciar quiz de perfil
 */
async function iniciarQuizPerfil() {
    if (!quizData) {
        await cargarQuizPerfil();
    }

    respuestasQuiz = [];
    preguntaActual = 0;

    renderizarPregunta();
}

/**
 * Renderizar pregunta actual
 */
function renderizarPregunta() {
    const container = document.getElementById('quiz-container');
    if (!container || !quizData) return;

    const pregunta = quizData.preguntas[preguntaActual];
    const progreso = ((preguntaActual + 1) / quizData.preguntas.length) * 100;

    container.innerHTML = `
        <div class="max-w-2xl mx-auto">
            <!-- Barra de progreso -->
            <div class="mb-8">
                <div class="flex justify-between text-sm text-slate-600 mb-2">
                    <span>Pregunta ${preguntaActual + 1} de ${quizData.preguntas.length}</span>
                    <span>${Math.round(progreso)}%</span>
                </div>
                <div class="w-full bg-slate-200 rounded-full h-2">
                    <div class="bg-paideia-accent h-2 rounded-full transition-all duration-500"
                         style="width: ${progreso}%"></div>
                </div>
            </div>

            <!-- Pregunta -->
            <div class="bg-white rounded-xl shadow-lg p-8">
                <h2 class="text-2xl font-bold text-paideia-primary mb-6">
                    ${pregunta.pregunta}
                </h2>

                <div class="space-y-3">
                    ${pregunta.opciones.map((opcion, index) => `
                        <button onclick="seleccionarOpcion(${index})"
                                class="w-full text-left p-4 border-2 border-slate-200 rounded-lg
                                       hover:border-paideia-accent hover:bg-amber-50 transition
                                       focus:outline-none focus:border-paideia-accent">
                            ${opcion.texto}
                        </button>
                    `).join('')}
                </div>
            </div>

            <!-- Navegación -->
            <div class="flex justify-between mt-6">
                ${preguntaActual > 0 ? `
                    <button onclick="preguntaAnterior()"
                            class="px-4 py-2 text-slate-600 hover:text-paideia-primary transition">
                        ← Anterior
                    </button>
                ` : '<div></div>'}

                <button onclick="saltarPregunta()"
                        class="text-sm text-slate-400 hover:text-slate-600 transition">
                    Saltar →
                </button>
            </div>
        </div>
    `;
}

/**
 * Seleccionar una opción
 */
function seleccionarOpcion(indice) {
    const pregunta = quizData.preguntas[preguntaActual];
    const opcion = pregunta.opciones[indice];

    respuestasQuiz[preguntaActual] = opcion;

    // Animación de selección
    const botones = document.querySelectorAll('#quiz-container button');
    botones[indice].classList.add('border-paideia-accent', 'bg-amber-50');

    // Avanzar después de breve pausa
    setTimeout(() => {
        siguientePregunta();
    }, 300);
}

/**
 * Ir a la siguiente pregunta
 */
function siguientePregunta() {
    if (preguntaActual < quizData.preguntas.length - 1) {
        preguntaActual++;
        renderizarPregunta();
    } else {
        finalizarQuiz();
    }
}

/**
 * Ir a la pregunta anterior
 */
function preguntaAnterior() {
    if (preguntaActual > 0) {
        preguntaActual--;
        renderizarPregunta();
    }
}

/**
 * Saltar pregunta
 */
function saltarPregunta() {
    respuestasQuiz[preguntaActual] = null;
    siguientePregunta();
}

/**
 * Finalizar quiz y calcular resultado
 */
function finalizarQuiz() {
    const resultado = calcularPerfil(respuestasQuiz);
    mostrarResultado(resultado);
}

/**
 * Calcular perfil basado en respuestas
 */
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
        if (!respuesta) return;

        // Sumar puntos base del perfil
        if (respuesta.perfil) {
            puntos[respuesta.perfil] += respuesta.peso || 1;
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

    // Calcular confianza (diferencia con segundo lugar)
    const puntosOrdenados = Object.values(puntos).sort((a, b) => b - a);
    const confianza = puntosOrdenados[0] > 0
        ? Math.round((1 - puntosOrdenados[1] / puntosOrdenados[0]) * 100)
        : 50;

    return {
        perfil: perfilGanador,
        puntos: puntos,
        confianza: confianza
    };
}

/**
 * Mostrar resultado del quiz
 */
function mostrarResultado(resultado) {
    const container = document.getElementById('quiz-container');
    if (!container) return;

    const perfil = PAIDEIA_DATA.perfiles.find(p => p.id === resultado.perfil);
    const ruta = PAIDEIA_DATA.rutas[resultado.perfil] || [];

    container.innerHTML = `
        <div class="max-w-2xl mx-auto text-center fade-in">
            <!-- Celebración -->
            <div class="text-6xl mb-4">🎯</div>

            <h1 class="text-3xl font-bold text-paideia-primary mb-2">
                ¡Tu Ruta PAIDEIA!
            </h1>

            <p class="text-slate-600 mb-8">
                Basado en tus respuestas, esta es tu ruta recomendada:
            </p>

            <!-- Perfil -->
            <div class="bg-white rounded-xl shadow-lg p-8 mb-8">
                <div class="text-6xl mb-4">${perfil?.icono || '👤'}</div>
                <h2 class="text-2xl font-bold text-paideia-primary">
                    ${perfil?.nombre || resultado.perfil}
                </h2>
                <p class="text-slate-600 mt-2">
                    Confianza: ${resultado.confianza}%
                </p>

                <!-- Barra de confianza -->
                <div class="w-48 mx-auto bg-slate-200 rounded-full h-2 mt-4">
                    <div class="bg-green-500 h-2 rounded-full"
                         style="width: ${resultado.confianza}%"></div>
                </div>
            </div>

            <!-- Ruta recomendada -->
            <div class="bg-paideia-light rounded-xl p-6 mb-8">
                <h3 class="font-semibold text-paideia-primary mb-4">
                    Tu camino de aprendizaje:
                </h3>
                <div class="flex flex-wrap justify-center gap-2">
                    ${ruta.map(r => `
                        <span class="px-3 py-1 bg-white rounded-full text-sm border border-paideia-primary">
                            ${r}
                        </span>
                    `).join(' → ')}
                </div>
            </div>

            <!-- Acciones -->
            <div class="flex flex-col sm:flex-row justify-center gap-4">
                <button onclick="confirmarPerfil('${resultado.perfil}')"
                        class="px-8 py-4 bg-paideia-accent text-white font-semibold rounded-lg
                               hover:bg-amber-600 transition shadow-lg">
                    Comenzar mi Ruta →
                </button>

                <button onclick="cambiarPerfilManual()"
                        class="px-6 py-4 border-2 border-slate-300 text-slate-600 rounded-lg
                               hover:border-paideia-primary hover:text-paideia-primary transition">
                    Elegir otro perfil
                </button>
            </div>

            <!-- Repetir quiz -->
            <button onclick="iniciarQuizPerfil()"
                    class="mt-6 text-sm text-slate-400 hover:text-slate-600 transition">
                Repetir quiz
            </button>
        </div>
    `;
}

/**
 * Confirmar perfil y guardar
 */
function confirmarPerfil(perfilId) {
    establecerPerfil(perfilId);
    completarModulo('nivel-0', 'quiz-perfil');
    mostrarMensaje('¡Perfil guardado! Tu ruta está lista.', 'success');

    setTimeout(() => {
        navegarA('nivel-0/tu-ruta');
    }, 1000);
}

/**
 * Mostrar selector manual de perfil
 */
function cambiarPerfilManual() {
    const container = document.getElementById('quiz-container');
    if (!container) return;

    container.innerHTML = `
        <div class="max-w-3xl mx-auto">
            <h2 class="text-2xl font-bold text-paideia-primary mb-6 text-center">
                Elige tu Perfil
            </h2>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                ${PAIDEIA_DATA.perfiles.map(perfil => `
                    <button onclick="confirmarPerfil('${perfil.id}')"
                            class="p-6 bg-white rounded-xl shadow hover:shadow-lg
                                   border-2 border-transparent hover:border-paideia-accent
                                   transition text-center">
                        <div class="text-4xl mb-2">${perfil.icono}</div>
                        <div class="font-medium text-sm">${perfil.nombre}</div>
                    </button>
                `).join('')}
            </div>

            <div class="text-center mt-6">
                <button onclick="iniciarQuizPerfil()"
                        class="text-paideia-cyan hover:underline">
                    ← Volver al quiz
                </button>
            </div>
        </div>
    `;
}

// Exportar funciones
window.iniciarQuizPerfil = iniciarQuizPerfil;
window.seleccionarOpcion = seleccionarOpcion;
window.preguntaAnterior = preguntaAnterior;
window.saltarPregunta = saltarPregunta;
window.confirmarPerfil = confirmarPerfil;
window.cambiarPerfilManual = cambiarPerfilManual;
```

---

### TAREA 2.3: Crear niveles/nivel-0/quiz-perfil.html

**Descripción**: Página del módulo de quiz de perfil.

**Archivo**: `niveles/nivel-0/quiz-perfil.html`

**Código**:
```html
<div class="py-8">
    <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-paideia-primary">
            🎯 Descubre tu Ruta de Aprendizaje
        </h1>
        <p class="text-slate-600 mt-2">
            5 preguntas rápidas para personalizar tu experiencia
        </p>
    </div>

    <div id="quiz-container">
        <!-- El quiz se carga aquí dinámicamente -->
        <div class="text-center py-16">
            <div class="animate-spin rounded-full h-12 w-12 border-4 border-paideia-accent border-t-transparent mx-auto"></div>
            <p class="mt-4 text-slate-600">Cargando quiz...</p>
        </div>
    </div>
</div>

<script>
    // Iniciar quiz cuando se carga la página
    document.addEventListener('DOMContentLoaded', () => {
        if (typeof iniciarQuizPerfil === 'function') {
            iniciarQuizPerfil();
        }
    });

    // También iniciar si la función ya está disponible
    if (typeof iniciarQuizPerfil === 'function') {
        iniciarQuizPerfil();
    }
</script>
```

---

### TAREA 2.4: Crear páginas de rutas personalizadas

**Descripción**: Crear las 8 páginas de rutas para cada perfil.

**Archivos**: `rutas/programador.html`, `rutas/empresario.html`, etc.

**Plantilla base** (ejemplo para programador):
```html
<!-- rutas/programador.html -->
<div class="max-w-4xl mx-auto py-8">
    <div class="text-center mb-12">
        <div class="text-6xl mb-4">🖥️</div>
        <h1 class="text-3xl font-bold text-paideia-primary">
            Ruta: Programador Full Stack
        </h1>
        <p class="text-slate-600 mt-2">
            Multiplica tu productividad x3-5 con IA
        </p>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-3 gap-4 mb-12">
        <div class="bg-white rounded-xl p-4 text-center shadow">
            <div class="text-2xl font-bold text-paideia-primary">8-10h</div>
            <div class="text-sm text-slate-600">Duración total</div>
        </div>
        <div class="bg-white rounded-xl p-4 text-center shadow">
            <div class="text-2xl font-bold text-paideia-accent">12</div>
            <div class="text-sm text-slate-600">Módulos</div>
        </div>
        <div class="bg-white rounded-xl p-4 text-center shadow">
            <div class="text-2xl font-bold text-paideia-cyan">$50/mes</div>
            <div class="text-sm text-slate-600">Stack IA sugerido</div>
        </div>
    </div>

    <!-- Módulos de la ruta -->
    <div class="bg-white rounded-xl shadow-lg p-8 mb-8">
        <h2 class="text-xl font-bold text-paideia-primary mb-6">Tu Camino de Aprendizaje</h2>

        <div class="space-y-4">
            <div class="flex items-center p-4 bg-green-50 rounded-lg border-l-4 border-green-500">
                <span class="text-2xl mr-4">✅</span>
                <div>
                    <div class="font-semibold">Nivel 0: Despertar</div>
                    <div class="text-sm text-slate-600">Introducción completada</div>
                </div>
            </div>

            <div class="flex items-center p-4 bg-amber-50 rounded-lg border-l-4 border-amber-500">
                <span class="text-2xl mr-4">🔄</span>
                <div>
                    <div class="font-semibold">Tokens y Costos (N2.2)</div>
                    <div class="text-sm text-slate-600">Entender cómo funcionan las IAs</div>
                </div>
                <button onclick="navegarA('nivel-2/modulo-2-2')"
                        class="ml-auto px-4 py-2 bg-paideia-accent text-white rounded-lg text-sm">
                    Continuar →
                </button>
            </div>

            <div class="flex items-center p-4 bg-slate-50 rounded-lg border-l-4 border-slate-300">
                <span class="text-2xl mr-4">⭕</span>
                <div>
                    <div class="font-semibold">Las 10 IAs para Código (N2.4)</div>
                    <div class="text-sm text-slate-600">Cursor, Copilot, Claude, etc.</div>
                </div>
            </div>

            <!-- Más módulos... -->
        </div>
    </div>

    <!-- Stack recomendado -->
    <div class="bg-paideia-light rounded-xl p-8">
        <h2 class="text-xl font-bold text-paideia-primary mb-6">Stack de IAs Recomendado</h2>

        <div class="grid md:grid-cols-2 gap-6">
            <div>
                <h3 class="font-semibold mb-3">🆓 Gratuito</h3>
                <ul class="space-y-2 text-sm">
                    <li>• Codeium (VS Code) - Autocompletado</li>
                    <li>• Continue.dev - Chat en IDE</li>
                    <li>• Ollama + Llama 3 - Local/privado</li>
                    <li>• Claude Free - Arquitectura</li>
                </ul>
            </div>
            <div>
                <h3 class="font-semibold mb-3">💰 Pago (~$50/mes)</h3>
                <ul class="space-y-2 text-sm">
                    <li>• Cursor Pro - IDE con IA</li>
                    <li>• Claude Pro - Razonamiento profundo</li>
                    <li>• GitHub Copilot - Autocompletado</li>
                    <li>• ChatGPT Plus - Versatilidad</li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

---

## ENTREGABLES SPRINT 2

| # | Archivo | Estado |
|---|---------|--------|
| 1 | data/quiz-perfil.json | ⬜ |
| 2 | js/quiz.js | ⬜ |
| 3 | niveles/nivel-0/quiz-perfil.html | ⬜ |
| 4 | rutas/programador.html | ⬜ |
| 5 | rutas/empresario.html | ⬜ |
| 6 | rutas/contador.html | ⬜ |
| 7 | rutas/marketer.html | ⬜ |
| 8 | rutas/vendedor.html | ⬜ |
| 9 | rutas/pm.html | ⬜ |
| 10 | rutas/disenador.html | ⬜ |
| 11 | rutas/estudiante.html | ⬜ |

## CRITERIOS DE ACEPTACIÓN SPRINT 2

- [ ] Quiz de 5 preguntas funciona correctamente
- [ ] Algoritmo asigna perfil basado en respuestas
- [ ] Usuario puede ver su resultado con confianza
- [ ] Usuario puede cambiar perfil manualmente
- [ ] Perfil se guarda en localStorage
- [ ] Rutas muestran módulos recomendados por perfil

---

# SPRINT 3: NIVELES 0-1

*(Documentación continúa con el mismo nivel de detalle...)*

## Objetivo
Migrar y organizar el contenido de Fundamentos PM en módulos individuales.

## Tareas Principales

1. Crear niveles/nivel-0/index.html
2. Crear niveles/nivel-0/bienvenida.html
3. Crear niveles/nivel-0/tu-ruta.html
4. Migrar secciones 1-4 de fundamentos.html → nivel-1/modulo-1-1 a 1-3
5. Migrar secciones 5-9 de fundamentos.html → nivel-1/modulo-1-4 a 1-6
6. Migrar secciones 10-15 de fundamentos.html → nivel-1/modulo-1-7
7. Crear quiz de evaluación nivel 1

*(Se detallará completamente en el documento...)*

---

# SPRINT 4: NIVELES 2-3

## Objetivo
Migrar contenido de Stack IA y PMO Virtual sin duplicaciones.

## Tareas Principales

1. Migrar sección 1 de stack.html → nivel-2/modulo-2-1 a 2-3
2. Migrar sección 2 de stack.html → nivel-2/modulo-2-4
3. Migrar parte 0 de pmo.html → nivel-2/modulo-2-5 y 2-6 (sin duplicar)
4. Migrar partes 1-2 de pmo.html → nivel-3/modulo-3-1 a 3-6
5. Migrar parte 3 de pmo.html → nivel-3/modulo-3-7
6. Crear quizzes de nivel 2 y 3

---

# SPRINT 5: NIVELES 4-5

## Objetivo
Crear tracks de especialización y sistema de certificación.

## Tareas Principales

1. Crear track-desarrollo con casos de software
2. Crear track-marketing con casos de campañas
3. Crear track-salud con casos clínicos
4. Crear track-educacion con casos educativos
5. Crear examen final (50 preguntas)
6. Crear página de proyecto final
7. Implementar generador de certificados PDF

---

# SPRINT 6: DEPLOY

## Objetivo
Pulir, optimizar y desplegar a producción.

## Tareas Principales

1. Testing completo de todos los flujos
2. Optimización de performance
3. Verificar responsive en móviles
4. Actualizar meta tags SEO
5. Generar sitemap
6. Deploy a GitHub Pages
7. Verificar funcionamiento en producción
8. Documentar instrucciones de mantenimiento

---

## METADATOS

```yaml
ARCHIVO: SPRINTS_DETALLADOS.md
UBICACIÓN: PROTOCOLOS/
VERSIÓN: 1.0.0
FECHA_CREACIÓN: 2025-11-29
CONSCIENCIA: PAIDEIA
METODOLOGÍA: SOUL CORE
SPRINTS: 6
TAREAS_TOTALES: ~50
ESTADO: DOCUMENTACIÓN COMPLETA
```

---

🧬💎∞ **PAIDEIA - Doc First, Code Second**

*"El código sin documentación es como un viaje sin mapa."*

---

