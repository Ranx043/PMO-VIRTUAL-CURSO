// JS unificado para navegación, tabs, scroll spy y lazy Mermaid.

document.addEventListener('DOMContentLoaded', function() {
  // Inicializar Mermaid
  mermaid.initialize({ startOnLoad: true, theme: 'default' });

  // Toggle para menú móvil
  const menuToggle = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('toc-sidebar');
  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', () => {
      sidebar.classList.toggle('hidden-mobile');
      sidebar.classList.toggle('-translate-x-full');
    });

    // Cerrar menú al click fuera
    document.addEventListener('click', (event) => {
      if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
        sidebar.classList.add('hidden-mobile');
        sidebar.classList.add('-translate-x-full');
      }
    });
  }

  // Tabs functionality
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const targetTab = button.dataset.tab;
      tabButtons.forEach(btn => btn.classList.remove('active'));
      tabContents.forEach(content => content.classList.remove('active'));
      button.classList.add('active');
      document.getElementById(targetTab).classList.add('active');
      
      // Re-init scroll spy for the active tab
      initScrollSpy(targetTab);
    });
  });

  // Función para inicializar scroll spy en una tab específica
  function initScrollSpy(tabId) {
    const sections = document.querySelectorAll(`#${tabId} section[id]`);
    const tocLinks = document.querySelectorAll(`#toc-nav a[href^="#"]`); // All TOC links, but filter by tab if needed
    const observer = new IntersectionObserver((entries) => {
      let activeSectionId = null;
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          activeSectionId = entry.target.id;
        }
      });
      tocLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${activeSectionId}`) {
          link.classList.add('active');
        }
      });
    }, { rootMargin: '0px', threshold: 0.3 });

    sections.forEach(section => observer.observe(section));
  }

  // Inicializar scroll spy para la primera tab activa
  const activeTab = document.querySelector('.tab-content.active');
  if (activeTab) {
    initScrollSpy(activeTab.id);
  }

  // Cerrar menú al click en enlaces TOC
  const tocLinks = document.querySelectorAll('#toc-nav a');
  tocLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth < 1024) {
        sidebar.classList.add('hidden-mobile');
        sidebar.classList.add('-translate-x-full');
      }
    });
  });

  // Progreso localStorage para checklists (opcional)
  const checklists = document.querySelectorAll('.checklist input[type="checkbox"]');
  checklists.forEach(checkbox => {
    const saved = localStorage.getItem(checkbox.id);
    if (saved === 'true') {
      checkbox.checked = true;
    }
    checkbox.addEventListener('change', () => {
      localStorage.setItem(checkbox.id, checkbox.checked);
    });
  });

  // Lazy load Mermaid for acordeones
  const detailsElements = document.querySelectorAll('details');
  detailsElements.forEach(details => {
    details.addEventListener('toggle', () => {
      if (details.open) {
        const mermaidDiv = details.querySelector('.mermaid');
        if (mermaidDiv) {
          mermaid.run({
            nodes: [mermaidDiv],
            callback: (svgCode) => {
              mermaidDiv.innerHTML = svgCode;
            }
          });
        }
      }
    });
  });
});