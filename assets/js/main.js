/* =====================================================
   Avijit Roy — Main JS
   Handles: Mobile Nav, Filters, Dark/Light Mode Toggle
   ===================================================== */

(function () {
  // ---------- MOBILE NAV ----------
  const hamburger = document.getElementById("hamburger");
  const nav = document.getElementById("navLinks");
  hamburger?.addEventListener("click", () => nav?.classList.toggle("show"));

  // ---------- THEME TOGGLE ----------
  const root = document.documentElement;
  const savedTheme = localStorage.getItem("theme");
  const prefersDark =
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches;

  const currentTheme = savedTheme || (prefersDark ? "dark" : "light");
  root.setAttribute("data-theme", currentTheme);
  updateThemeIcon(currentTheme);

  const toggleBtn = document.getElementById("themeToggle");
  toggleBtn?.addEventListener("click", () => {
    const newTheme =
      root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateThemeIcon(newTheme);
  });

  function updateThemeIcon(theme) {
    const icon = document.getElementById("themeIcon");
    if (!icon) return;
    icon.innerHTML =
      theme === "dark"
        ? `<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>`
        : `<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M6.76 4.84l-1.8-1.79-1.41 1.41 1.79 1.8zM1 13h3v-2H1v2zm10 10h2v-3h-2v3zM4.95 19.07l1.41 1.41 1.8-1.79-1.41-1.41zM13 1h-2v3h2z"/></svg>`;
  }

  // ---------- PROJECT FILTER ----------
  const search = document.getElementById("projectSearch");
  const clearBtn = document.getElementById("clearSearch");
  const chips = document.querySelectorAll(".chip");
  const projects = () =>
    Array.from(
      document.querySelectorAll("#projectGrid .card, #repoGrid .card")
    );

  function applyFilter() {
    const q = (search?.value || "").toLowerCase();
    const activeChip = document.querySelector(".chip.active");
    const tag = activeChip ? activeChip.getAttribute("data-tag") : "all";

    projects().forEach((p) => {
      const name = (p.querySelector("h3")?.textContent || "").toLowerCase();
      const tags = (p.getAttribute("data-tags") || "").toLowerCase();
      const matchesTag = tag === "all" || tags.includes(tag);
      const matchesText = !q || name.includes(q) || tags.includes(q);
      p.style.display = matchesTag && matchesText ? "block" : "none";
    });
  }

  search?.addEventListener("input", applyFilter);
  clearBtn?.addEventListener("click", () => {
    search.value = "";
    search.focus();
    applyFilter();
  });
  chips.forEach((c) =>
    c.addEventListener("click", () => {
      chips.forEach((x) => x.classList.remove("active"));
      c.classList.add("active");
      applyFilter();
    })
  );

  // ---------- LOAD GITHUB REPOS ----------
  const repoGrid = document.getElementById("repoGrid");
  if (repoGrid) {
    repoGrid.innerHTML = "<p class='muted'>Loading repositories…</p>";
    fetch(
      "https://api.github.com/users/heyavijitroy/repos?per_page=100&sort=updated"
    )
      .then((r) => r.json())
      .then((repos) => {
        if (!Array.isArray(repos))
          throw new Error("GitHub API limit or error reached");
        const curated = repos
          .filter((r) => !r.fork && !r.archived)
          .sort((a, b) => new Date(b.pushed_at) - new Date(a.pushed_at))
          .slice(0, 20);
        repoGrid.innerHTML = curated
          .map(
            (r) => `
          <article class="card" data-tags="opensource ${r.language || ""}">
            <h3><a href="${r.html_url}" target="_blank">${r.name}</a></h3>
            <p class="muted">${r.description || "No description"}</p>
            <a class="button small icon" href="${r.html_url}" target="_blank">
              <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8...Z"></path></svg>
            </a>
          </article>`
          )
          .join("");
        applyFilter();
      })
      .catch(() => {
        repoGrid.innerHTML =
          "<p class='muted'>Could not load repositories.</p>";
      });
  }
})();
