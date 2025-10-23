// JS unificado mejorado con transiciones suaves, error handling y debug.

document.addEventListener('DOMContentLoaded', function() {
  console.log('JS cargado - Iniciando navegación y transiciones.');

  // Inicializar Mermaid con error handling
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({ startOnLoad: true, theme: 'default' });
    console.log('Mermaid inicializado correctamente.');
  } else {
    console.error('Mermaid no cargó - Verifica conexión a CDN.');
  }

  // Toggle para menú móvil
  const menuToggle = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('toc-sidebar');
  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', () => {
      sidebar.classList.toggle('hidden-mobile');
      sidebar.classList.toggle('-translate-x-full');
      console.log('Menú móvil toggled.');
    });

    // Cerrar menú al click fuera
    document.addEventListener('click', (event) => {
      if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
        sidebar.classList.add('hidden-mobile');
        sidebar.classList.add('-translate-x-full');
        console.log('Menú cerrado por click fuera.');
      }
    });
  } else {
    console.error('Elementos de menú no encontrados.');
  }

  // Tabs functionality with smooth transition
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const targetTab = button.dataset.tab;
      if (targetTab) {
        // Remove active from all
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        // Add active to clicked
        button.classList.add('active');
        document.getElementById(targetTab).classList.add('active');
        console.log(`Tab cambiada a: ${targetTab}`);
        
        // Re-init scroll spy for the active tab
        initScrollSpy(targetTab);
      } else {
        console.error('Dataset tab no encontrado.');
      }
    });
  });

  // Función para inicializar scroll spy en una tab específica
  function initScrollSpy(tabId) {
    const sections = document.querySelectorAll(`#${tabId} section[id]`);
    const tocLinks = document.querySelectorAll(`#toc-nav a[href^="#"]`);
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
    console.log(`Scroll spy inicializado para tab: ${tabId}`);
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

  // Progreso localStorage para checklists with fallback
  const checklists = document.querySelectorAll('.checklist input[type="checkbox"]');
  checklists.forEach(checkbox => {
    const saved = localStorage.getItem(checkbox.id);
    if (saved === 'true') {
      checkbox.checked = true;
    }
    checkbox.addEventListener('change', () => {
      localStorage.setItem(checkbox.id, checkbox.checked);
      console.log(`Checklist actualizada: ${checkbox.id} = ${checkbox.checked}`);
    });
  });

  // Lazy load Mermaid for acordeones with error handling
  const detailsElements = document.querySelectorAll('details');
  detailsElements.forEach(details => {
    details.addEventListener('toggle', () => {
      if (details.open) {
        const mermaidDiv = details.querySelector('.mermaid');
        if (mermaidDiv && typeof mermaid !== 'undefined') {
          mermaid.run({
            nodes: [mermaidDiv],
            callback: (svgCode) => {
              mermaidDiv.innerHTML = svgCode;
              console.log('Mermaid renderizado en acordeón.');
            },
            fallback: (err) => {
              console.error('Error renderizando Mermaid:', err);
            }
          });
        } else {
          console.error('Mermaid no disponible o div no encontrado.');
        }
      }
    });
  });

  // Certificado button with jsPDF
  const certificadoBtn = document.getElementById('certificado-btn');
  if (certificadoBtn && typeof jsPDF !== 'undefined') {
    certificadoBtn.addEventListener('click', () => {
      const doc = new jsPDF();
      const totalCheckboxes = checklists.length;
      const checked = Array.from(checklists).filter(cb => cb.checked).length;
      const percent = Math.round((checked / totalCheckboxes) * 100);
      doc.text(`Certificado de Progreso: ${percent}% completado`, 10, 10);
      doc.save('certificado-progreso.pdf');
      console.log(`Certificado generado: ${percent}%`);
    });
  } else {
    console.error('jsPDF no cargó - Verifica CDN.');
  }

  console.log('JS inicialización completada. Todo listo para transiciones.');
});