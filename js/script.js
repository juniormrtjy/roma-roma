/* 01. MENU MOBILE — o conteúdo permanece acessível se JavaScript estiver desativado. */
document.documentElement.classList.add('js');
const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('.main-nav');
function closeMenu(restoreFocus = false) {
  menu.classList.remove('is-open');
  menuButton.setAttribute('aria-expanded', 'false');
  if (restoreFocus) menuButton.focus();
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menu.classList.toggle('is-open', open);
});
menu.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.classList.contains('is-open')) closeMenu(true); });
document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });
matchMedia('(min-width: 851px)').addEventListener('change', () => closeMenu());

/* 02. REVELAÇÃO DISCRETA — textos já estão no HTML, visíveis sem JavaScript. */
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('[data-reveal]').forEach(element => {
    element.classList.add('reveal-ready');
    revealObserver.observe(element);
  });
}

/* 03. FORMULÁRIO SEM BACKEND — gera um rascunho, nunca envia dados automaticamente.
   INTEGRAR ENVIO AQUI: substituir o comportamento por uma requisição ao endpoint
   aprovado, exibindo sucesso apenas após resposta real do servidor. Atualizar privacidade.
   ALTERAR E-MAIL AQUI e em index.html (contato, rodapé, JSON-LD e aviso de privacidade). */
const contactEmail = 'adm@romaneiropromocoeseeventos.com';
const contactForm = document.querySelector('#contact-form');
const messageDialog = document.querySelector('#message-dialog');
const messagePreview = document.querySelector('#message-preview');
const copyStatus = document.querySelector('#copy-status');
document.querySelector('#prepare-message').disabled = false;

contactForm.addEventListener('submit', event => {
  event.preventDefault();
  if (!contactForm.reportValidity()) return;
  const data = new FormData(contactForm);
  const message = [
    'Olá, equipe Romaneiro!', '',
    `Nome: ${data.get('nome').trim()}`,
    `Empresa: ${data.get('empresa').trim() || 'Não informada'}`,
    `Telefone: ${data.get('telefone').trim() || 'Não informado'}`,
    `E-mail: ${data.get('email').trim()}`,
    `Serviço: ${data.get('servico')}`, '',
    data.get('mensagem').trim()
  ].join('\n');
  messagePreview.value = message;
  copyStatus.textContent = '';
  document.querySelector('#email-draft').href = `mailto:${contactEmail}?subject=${encodeURIComponent('Novo projeto — site Romaneiro')}&body=${encodeURIComponent(message)}`;
  messageDialog.showModal();
});
document.querySelector('.dialog-close').addEventListener('click', () => messageDialog.close());
messageDialog.addEventListener('click', event => {
  const rect = messageDialog.getBoundingClientRect();
  if (event.target === messageDialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) messageDialog.close();
});
document.querySelector('#copy-message').addEventListener('click', async () => {
  try {
    if (!navigator.clipboard) throw new Error('Área de transferência indisponível');
    await navigator.clipboard.writeText(messagePreview.value);
    copyStatus.textContent = 'Mensagem copiada. Cole no seu e-mail ou WhatsApp para enviar.';
  } catch {
    messagePreview.focus();
    messagePreview.select();
    copyStatus.textContent = 'Rascunho selecionado. Use Ctrl+C (ou ⌘C) para copiar.';
  }
});

/* 04. ANO DO RODAPÉ — não interfere no tempo de atuação declarado no PDF. */
document.querySelector('#copyright-year').textContent = new Date().getFullYear();

/* 05. SLIDESHOW DO HERO — mude o intervalo abaixo (em milissegundos).
   As imagens ficam no HTML. Sem JS, somente a primeira é exibida.
   Pausa ao interagir por teclado, ao passar o mouse, sair da tela ou ocultar a aba.
   Movimento reduzido desativa a reprodução automática e o CSS remove o fade. */
const slideshow = document.querySelector('.hero-slideshow');
if (slideshow) {
  const slides = [...slideshow.querySelectorAll('.hero-slide')];
  const controls = slideshow.querySelector('.slideshow-controls');
  const toggle = slideshow.querySelector('.slideshow-toggle');
  const count = slideshow.querySelector('.slideshow-count');
  const status = slideshow.querySelector('.slideshow-status');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const slideInterval = 5000;
  let currentSlide = 0;
  let paused = reducedMotion.matches;
  let hovered = false;
  let inView = true;
  let timer;

  function scheduleSlide() {
    clearTimeout(timer);
    if (!paused && !hovered && inView && !document.hidden && !reducedMotion.matches) {
      timer = setTimeout(() => showSlide(currentSlide + 1), slideInterval);
    }
  }

  function updatePlayback() {
    toggle.textContent = reducedMotion.matches ? 'Automático off' : paused ? 'Reproduzir ▶' : 'Pausar Ⅱ';
    toggle.setAttribute('aria-label', reducedMotion.matches ? 'Troca automática desativada por movimento reduzido' : paused ? 'Iniciar troca automática' : 'Pausar troca automática');
    toggle.disabled = reducedMotion.matches;
    scheduleSlide();
  }

  function showSlide(index, manual = false) {
    currentSlide = (index + slides.length) % slides.length;
    slides.forEach((slide, slideIndex) => {
      const active = slideIndex === currentSlide;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', String(!active));
    });
    count.textContent = `${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    if (manual) {
      paused = true;
      status.textContent = `Imagem ${currentSlide + 1} de ${slides.length}${slides[currentSlide].alt ? ': ' + slides[currentSlide].alt : ''}.`;
    }
    updatePlayback();
  }

  if (slides.length > 1) {
    controls.hidden = false;
    toggle.addEventListener('click', () => { paused = !paused; updatePlayback(); });
    slideshow.querySelector('.slideshow-previous').addEventListener('click', () => showSlide(currentSlide - 1, true));
    slideshow.querySelector('.slideshow-next').addEventListener('click', () => showSlide(currentSlide + 1, true));
    slideshow.addEventListener('mouseenter', () => { hovered = true; scheduleSlide(); });
    slideshow.addEventListener('mouseleave', () => { hovered = false; scheduleSlide(); });
    slideshow.addEventListener('focusin', event => {
      if (event.target !== toggle) { paused = true; updatePlayback(); }
    });
    document.addEventListener('visibilitychange', scheduleSlide);
    reducedMotion.addEventListener('change', () => { paused = true; updatePlayback(); });
    if ('IntersectionObserver' in window) {
      const slideshowObserver = new IntersectionObserver(entries => {
        inView = entries[0].isIntersecting;
        scheduleSlide();
      }, { threshold: 0.15 });
      slideshowObserver.observe(slideshow);
    }
    showSlide(0);
  }
}
