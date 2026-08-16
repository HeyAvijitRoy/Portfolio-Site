document.getElementById('currentYear').textContent = new Date().getFullYear();
const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// MOBILE NAV DROPDOWN
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (navToggle && navLinks) {
  const setOpen = (open) => {
    navLinks.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.querySelector('i').className = open ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
  };
  navToggle.addEventListener('click', () => setOpen(!navLinks.classList.contains('open')));
  navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
  document.addEventListener('click', (e) => {
    if (navLinks.classList.contains('open') && !navLinks.contains(e.target) && !navToggle.contains(e.target)) {
      setOpen(false);
    }
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navLinks.classList.contains('open')) {
      setOpen(false);
      navToggle.focus();
    }
  });
}

// FIGURE LIGHTBOX
const figTrigger = document.getElementById('figZoomTrigger');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightboxImg');
const lightboxClose = document.getElementById('lightboxClose');
if (figTrigger && lightbox && lightboxImg) {
  const sourceImg = figTrigger.querySelector('img');
  const openLightbox = () => {
    lightboxImg.src = sourceImg.src;
    lightboxImg.alt = sourceImg.alt;
    lightbox.classList.add('active');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    lightboxClose.focus();
  };
  const closeLightbox = () => {
    lightbox.classList.remove('active');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    figTrigger.focus();
  };
  figTrigger.addEventListener('click', openLightbox);
  lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'Tab') {
      e.preventDefault();
      lightboxClose.focus();
    }
  });
}

// BACK TO TOP
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
  if (window.pageYOffset > 400) {
    backToTop.classList.add('visible');
  } else {
    backToTop.classList.remove('visible');
  }
});
backToTop.addEventListener('click', (e) => {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
});

// RESULTS CHART — click a legend swatch to isolate that tokenizer
const legendButtons = document.querySelectorAll('.legend-btn[data-series]');
let activeSeries = null;
legendButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const series = btn.dataset.series;
    activeSeries = activeSeries === series ? null : series;
    legendButtons.forEach(b => {
      const selected = b.dataset.series === activeSeries;
      b.classList.toggle('active', selected);
      b.classList.toggle('dimmed', activeSeries !== null && !selected);
      b.setAttribute('aria-pressed', String(selected));
    });
    document.querySelectorAll('.tfr-row').forEach(row => {
      const isMatch = activeSeries === null || row.classList.contains(activeSeries);
      row.style.opacity = isMatch ? '1' : '.25';
    });
  });
});

// SENSITIVITY TIER TOGGLE
const SENS = {
  'Tier 1': { all: 1.65, clean: 2.11 },
  'Tier 2': { all: 1.55, clean: 1.79 },
  'Tier 3': { all: 1.50, clean: 1.79 }
};
const sensButtons = document.querySelectorAll('#sensControls [data-tier]');
sensButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    sensButtons.forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-pressed', 'false');
    });
    btn.classList.add('active');
    btn.setAttribute('aria-pressed', 'true');
    const d = SENS[btn.dataset.tier];
    document.getElementById('sensAll').textContent = d.all.toFixed(2) + '×';
    document.getElementById('sensClean').textContent = d.clean.toFixed(2) + '×';
  });
});

// CONTEXT / IMPACT PICKER
const CONTEXT = {
  English: { ecw: 128000, pct: 100, cost: 0.00 },
  Arabic: { ecw: 89148, pct: 70, cost: 0.06 },
  Bengali: { ecw: 81967, pct: 64, cost: 0.07 },
  Hindi: { ecw: 74461, pct: 58, cost: 0.09 },
  Tamil: { ecw: 61121, pct: 48, cost: 0.14 },
  Yoruba: { ecw: 53951, pct: 42, cost: 0.18 }
};
const picker = document.getElementById('contextPicker');
Object.keys(CONTEXT).forEach(lang => {
  const b = document.createElement('button');
  b.type = 'button';
  b.textContent = lang;
  b.dataset.lang = lang;
  b.setAttribute('aria-controls', 'contextViz');
  b.setAttribute('aria-pressed', String(lang === 'Bengali'));
  if (lang === 'Bengali') b.classList.add('active');
  b.addEventListener('click', () => {
    picker.querySelectorAll('button').forEach(x => {
      x.classList.remove('active');
      x.setAttribute('aria-pressed', 'false');
    });
    b.classList.add('active');
    b.setAttribute('aria-pressed', 'true');
    renderContext(lang);
  });
  picker.appendChild(b);
});

function renderContext(lang) {
  const d = CONTEXT[lang];
  document.getElementById('contextLabel').textContent = lang;
  document.getElementById('contextEq').textContent = d.ecw.toLocaleString() + ' of 128,000';
  document.getElementById('contextFill').style.width = d.pct + '%';
  document.getElementById('contextPct').textContent = d.pct + '%';
  document.getElementById('contextTokens').textContent = d.ecw.toLocaleString();
  document.getElementById('contextCost').textContent = d.cost === 0 ? '$0.00' : '+$' + d.cost.toFixed(2);
  const contextTrack = document.getElementById('contextTrack');
  contextTrack.setAttribute('aria-valuenow', String(d.pct));
  contextTrack.setAttribute('aria-valuetext', `${lang}: ${d.pct} percent`);
  document.getElementById('contextSentence').textContent =
    lang === 'English'
      ? 'English is the 1.00× baseline for the TEA context-equivalent estimate.'
      : `${lang} retains about ${d.pct}% of the English-equivalent capacity in a nominal 128k window.`;
}
renderContext('Bengali');

// TOAST
const toast = document.getElementById('toast');
function showToast(msg) {
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(window._toastTimer);
  window._toastTimer = setTimeout(() => toast.classList.remove('show'), 1800);
}

// COPY BIBTEX — shared by the paper and poster citation blocks
function copyBibtexFrom(blockId, statusId, toastMsg) {
  const block = document.getElementById(blockId);
  const status = document.getElementById(statusId);
  if (!block) return;
  const text = block.innerText.trim();

  function showStatus(message, success = true) {
    if (!status) return;
    status.textContent = message;
    status.classList.add('show');
    status.style.color = success ? '#1c7a4d' : '#b8352f';
    setTimeout(() => status.classList.remove('show'), 2000);
  }

  if (!navigator.clipboard || !window.isSecureContext) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand('copy');
      showStatus('Copied ✓');
      showToast(toastMsg);
    } catch (err) {
      showStatus('Copy failed', false);
    }
    document.body.removeChild(textarea);
    return;
  }

  navigator.clipboard.writeText(text)
    .then(() => {
      showStatus('Copied ✓');
      showToast(toastMsg);
    })
    .catch(() => showStatus('Copy failed', false));
}

function copyBibtex() {
  copyBibtexFrom('bibtexBlock', 'copyStatus', 'Paper BibTeX copied.');
}

function copyBibtexPoster() {
  copyBibtexFrom('bibtexPoster', 'copyStatusPoster', 'Poster BibTeX copied.');
}

function copyBibtexPresentation() {
  copyBibtexFrom('bibtexPresentation', 'copyStatusPresentation', 'Presentation BibTeX copied.');
}

document.getElementById('copyCitation').addEventListener('click', copyBibtex);
