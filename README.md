# Cursos Integrados de Gestión de Proyectos e IA

Plataforma educativa con tres módulos integrados en una sola página web: 

1. **Fundamentos de Gestión de Proyectos** (basado en PMI, con fases, herramientas como WBS/Gantt, checklists y diagramas).
2. **PMO Virtual con IA** (metodología PMI adaptada a IA, prompts, agents como CrewAI, casos prácticos).
3. **Stack de IA** (guía de herramientas IA/tech, workflows, comparativas de LLMs y extensions VS Code).

El sitio es estático, responsive y interactivo (tabs para cursos, acordeones para secciones, checklists con progreso local, diagramas Mermaid). No requiere servidor para vista local, pero usa CDNs para Tailwind y Mermaid.

## Instrucciones de Uso

### Vista Local
1. Abre `index.html` en cualquier navegador moderno (Chrome, Firefox, Edge).
2. Navega con tabs (cursos) y acordeones (subsecciones).
3. Marca checklists para progreso persistente (usa localStorage).
4. Diagramas Mermaid se renderizan automáticamente.

### Despliegue como Curso Online (GitHub Pages)
1. Crea un repositorio en GitHub llamado "cursos-gestion-ia" (o similar).
2. Sube todos los archivos de esta carpeta al repo (rama `main`).
3. Ve a Settings > Pages > Source: Deploy from branch `main` > Save.
4. URL pública: `https://tuusuario.github.io/cursos-gestion-ia`.
5. Accede desde cualquier dispositivo; certificado descargable al completar checklists.

### Duración y Estructura
- **Total**: 10-15 horas (3-5 horas por curso).
- **Features**:
  - Tabs: Selecciona curso (Fundamentos, PMO IA, Stack IA).
  - Acordeones: Expande secciones para ver checklists, diagramas y prompts.
  - Interactivo: Checklists guardan progreso, Mermaid para visuales.
  - Certificado: Botón en footer genera PDF con progreso (basado en localStorage).

### Contenido por Curso
- **Fundamentos**: 21 secciones sobre PMI (fases, WBS, Gantt, riesgos, ejemplos por industria).
- **PMO IA**: 15 secciones con prompts, stack IAs (Claude, Cursor, CrewAI), casos (SaaS, e-comm, salud).
- **Stack IA**: 20 secciones con comparativas (LLMs, agents), workflows y ejercicios.

### Setup Local (Opcional)
- No necesita dependencias; abre directamente.
- Para editar: Usa VS Code, agrega contenido en backups/ y reconstruye index.html.

### Contribuir
- Edita backups/ (HTML originales) para actualizar.
- Contribuciones bienvenidas: Pull requests para nuevos diagramas o quizzes.

## Licencia
MIT License - Libre para uso educativo y no comercial.

¡Empieza tu aprendizaje en gestión de proyectos con IA!