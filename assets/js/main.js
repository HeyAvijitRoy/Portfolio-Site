
(function(){
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('navLinks');
  if(hamburger && nav){
    hamburger.addEventListener('click', ()=> nav.classList.toggle('show'));
  }
  const toggle = document.getElementById('themeToggle');
  const key='theme';
  const root=document.documentElement;
  const setTheme=t=>{ root.setAttribute('data-theme', t); toggle.textContent = t==='light'?'🌙':'☀️'; };
  setTheme(localStorage.getItem(key)||'dark');
  toggle?.addEventListener('click', ()=>{
    const next = (root.getAttribute('data-theme')==='dark')?'light':'dark';
    setTheme(next); localStorage.setItem(key,next);
  });
  const search = document.getElementById('projectSearch');
  const chips = document.querySelectorAll('.chip');
  const items = Array.from(document.querySelectorAll('#projectGrid .card'));
  if (items.length){
    let currentTag = 'all';
    chips.forEach(ch=>ch.addEventListener('click', ()=>{
      chips.forEach(c=>c.classList.remove('active'));
      ch.classList.add('active');
      currentTag = ch.dataset.tag;
      filter();
    }));
    search?.addEventListener('input', filter);
    function filter(){
      const q = (search?.value||'').toLowerCase();
      items.forEach(el=>{
        const name = el.querySelector('h3').textContent.toLowerCase();
        const tags = (el.dataset.tags||'').toLowerCase();
        const tagOk = currentTag==='all' || tags.includes(currentTag.toLowerCase());
        const textOk = !q || (name.includes(q) || tags.includes(q));
        el.style.display = (tagOk && textOk)?'block':'none';
      });
    }
  }
  const repoGrid = document.getElementById('repoGrid');
  if (repoGrid){
    repoGrid.innerHTML = '<p class="muted">Loading repositories…</p>';
    fetch('https://api.github.com/users/heyavijitroy/repos?per_page=100&sort=updated')
      .then(r=>r.json())
      .then(repos=>{
        if (!Array.isArray(repos)) throw new Error('GitHub error/limit');
        const curated = repos.filter(r=>!r.fork && !r.archived)
          .sort((a,b)=>(b.stargazers_count - a.stargazers_count) || (new Date(b.pushed_at)-new Date(a.pushed_at)));
        repoGrid.innerHTML = curated.slice(0,18).map(r=>`
          <article class="card">
            <h3><a href="${r.html_url}" target="_blank" rel="noopener">${r.name}</a></h3>
            <p class="muted">${(r.description||'No description')}</p>
            <ul class="tags">
              ${r.language?`<li>${r.language}</li>`:''}
              <li>★ ${r.stargazers_count}</li>
              <li>Updated: ${new Date(r.pushed_at).toISOString().split('T')[0]}</li>
            </ul>
          </article>
        `).join('');
      })
      .catch(()=> repoGrid.innerHTML = '<p class="muted">Could not load repos right now.</p>');
  }
})();