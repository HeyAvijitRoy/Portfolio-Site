#!/usr/bin/env python3
"""Build the standalone HTML edition of the Git and GitHub student ebook."""

import argparse
import json
import re
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

try:
    import markdown
    from markdown.extensions.codehilite import CodeHiliteExtension
    from markdown.extensions.toc import TocExtension
except ImportError:
    print("Error: install the required package with: pip install markdown")
    sys.exit(1)


SOURCE_FILE = "git-github-for-cpp-students.md"
DEFAULT_OUTPUT = "index.html"
BOOK_TITLE = "Saving Your Work Like a Pro"
BOOK_SUBTITLE = "Git & GitHub for C++ Students"
AUTHOR = "Avijit Roy"
SITE_URL = "https://avijitroy.com/"
AUTHOR_URL = SITE_URL
INSTITUTION = "John Jay College of Criminal Justice, CUNY"
INSTITUTION_URL = "https://www.jjay.cuny.edu/"
PUBLISHED_PATH = "docs/git-version-control/"
CANONICAL_URL = f"{SITE_URL}{PUBLISHED_PATH}"
COVER_IMAGE_PATH = "assets/ebook-cover-letter.jpg"
SOCIAL_IMAGE_PATH = "docs/git-version-control/assets/ebook-og-image.jpg"
SOCIAL_IMAGE = f"{SITE_URL}{SOCIAL_IMAGE_PATH}"
ANALYTICS_ID = "G-Y4VM6347X4"
YEAR = datetime.now().year


CSS = r"""
:root {
  color-scheme: dark;
  --bg: #0b1118;
  --paper: #111a24;
  --paper-raised: #172332;
  --sidebar: #0e1620;
  --line: #263648;
  --line-strong: #385067;
  --ink: #dce5ee;
  --ink-strong: #f3f6f9;
  --muted: #99aabd;
  --accent: #37c87b;
  --accent-deep: #23a965;
  --accent-soft: rgba(55, 200, 123, .13);
  --gold: #e6b45e;
  --code-bg: #081019;
  --shadow: rgba(0, 0, 0, .27);
  --sidebar-w: 20rem;
  --page-w: 51rem;
  --ui: "Sora", "Segoe UI", Arial, sans-serif;
  --reading: "Source Serif 4", Georgia, serif;
  --mono: "JetBrains Mono", "Cascadia Code", Consolas, monospace;
}
[data-theme="light"] {
  color-scheme: light;
  --bg: #eeeae2;
  --paper: #fffdfa;
  --paper-raised: #f7f3ec;
  --sidebar: #f9f6ef;
  --line: #e3dbce;
  --line-strong: #c8bba7;
  --ink: #302c29;
  --ink-strong: #171513;
  --muted: #625c55;
  --accent: #146943;
  --accent-deep: #0e5435;
  --accent-soft: rgba(20, 105, 67, .09);
  --gold: #8a5c17;
  --code-bg: #242a32;
  --shadow: rgba(53, 43, 31, .1);
}
*, *::before, *::after { box-sizing: border-box; }
html { font-size: 16px; scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--reading);
  line-height: 1.72;
}
a { color: var(--accent); text-underline-offset: .17em; }
a:hover { color: var(--accent-deep); }
:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: .18rem;
}
.skip-link {
  position: fixed;
  z-index: 100;
  top: .65rem;
  left: .8rem;
  transform: translateY(-150%);
  padding: .55rem .9rem;
  background: var(--accent);
  color: #07140d;
  font: 600 .9rem var(--ui);
  text-decoration: none;
}
.skip-link:focus { transform: none; }
.reading-progress {
  position: fixed;
  z-index: 40;
  inset: 0 0 auto 0;
  height: .22rem;
  background: transparent;
}
.reading-progress span {
  display: block;
  width: 0;
  height: 100%;
  background: var(--accent);
}
.toolbar {
  position: fixed;
  top: 0;
  right: 0;
  z-index: 31;
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .8rem 1.05rem;
}
.tool-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .48rem;
  min-height: 2.65rem;
  padding: .55rem .9rem;
  border: 1px solid var(--line-strong);
  border-radius: 999px;
  background: var(--paper);
  color: var(--ink-strong);
  cursor: pointer;
  font: 600 .78rem var(--ui);
  letter-spacing: .02em;
}
.tool-button:hover { background: var(--paper-raised); border-color: var(--accent); }
.menu-button { display: none; }
.layout { min-height: 100vh; }
.sidebar {
  position: fixed;
  z-index: 30;
  inset: 0 auto 0 0;
  width: var(--sidebar-w);
  display: flex;
  flex-direction: column;
  background: var(--sidebar);
  border-right: 1px solid var(--line);
}
.sidebar-header {
  padding: 2rem 1.45rem 1.1rem;
  border-bottom: 1px solid var(--line);
}
.sidebar-kicker {
  display: block;
  margin-bottom: .55rem;
  color: var(--accent);
  font: 700 .66rem var(--ui);
  letter-spacing: .17em;
  text-transform: uppercase;
}
.sidebar-title {
  display: block;
  color: var(--ink-strong);
  font: 700 1.05rem/1.35 var(--ui);
  text-decoration: none;
}
.sidebar-subtitle {
  display: block;
  margin-top: .4rem;
  color: var(--muted);
  font: 400 .76rem/1.45 var(--ui);
}
.sidebar-subtitle a {
  color: var(--ink);
  font-weight: 600;
}
.sidebar-subtitle a:hover { color: var(--accent); }
.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 1rem .72rem 1.2rem;
  scrollbar-width: thin;
}
.sidebar-nav::before {
  content: "Chapters";
  display: block;
  padding: 0 .7rem .55rem;
  color: var(--muted);
  font: 700 .65rem var(--ui);
  letter-spacing: .14em;
  text-transform: uppercase;
}
.sidebar-nav ul { margin: 0; padding: 0; list-style: none; }
.sidebar-nav li { margin: .13rem 0; }
.sidebar-nav a {
  display: block;
  padding: .43rem .66rem;
  border-left: 2px solid transparent;
  border-radius: 0 .42rem .42rem 0;
  color: var(--muted);
  font: 500 .74rem/1.42 var(--ui);
  text-decoration: none;
}
.sidebar-nav a:hover {
  color: var(--ink-strong);
  background: var(--paper-raised);
}
.sidebar-nav a[aria-current="location"] {
  color: var(--accent);
  border-left-color: var(--accent);
  background: var(--accent-soft);
}
.sidebar-footer {
  padding: .9rem 1.45rem 1.2rem;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font: .71rem/1.55 var(--ui);
}
.overlay { display: none; }
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
.reader {
  width: min(calc(100% - var(--sidebar-w)), calc(var(--page-w) + 5rem));
  margin-left: var(--sidebar-w);
  padding: 0 2.5rem 4rem;
}
.cover {
  min-height: min(95vh, 53rem);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 5rem 0 4.5rem;
  border-bottom: 1px solid var(--line);
}
.edition {
  display: flex;
  align-items: center;
  gap: .75rem;
  margin-bottom: 2.35rem;
  color: var(--accent);
  font: 700 .72rem var(--ui);
  letter-spacing: .18em;
  text-transform: uppercase;
}
.edition::before { content: ""; width: 3rem; height: 1px; background: var(--accent); }
.cover-art {
  display: none;
  width: min(100%, 31.5rem);
  height: auto;
  margin: 0 0 2.4rem;
  border-radius: .25rem;
  box-shadow: 0 1.2rem 2.8rem rgba(0, 0, 0, .38);
}
.cover h1 {
  max-width: 47rem;
  margin: 0 0 1rem;
  color: var(--ink-strong);
  font: 700 clamp(3rem, 6.4vw, 4.85rem)/1.06 var(--reading);
  letter-spacing: -.045em;
}
.cover h1 span { display: block; color: var(--accent); }
.cover-description {
  max-width: 39rem;
  margin: 0 0 2.6rem;
  color: var(--muted);
  font: 400 clamp(1.08rem, 2vw, 1.2rem)/1.7 var(--reading);
}
.cover-byline {
  max-width: 46rem;
  margin-bottom: 2.7rem;
  color: var(--ink);
  font: .92rem/1.55 var(--ui);
}
.cover-credit { margin: 0 0 1rem; }
.cover-credit strong {
  color: var(--ink-strong);
  font-size: 1.05rem;
}
.cover-affiliations {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
.cover-affiliation {
  padding: .15rem 0 .15rem 1rem;
  border-left: 2px solid var(--accent);
}
.cover-role,
.cover-unit,
.cover-institution { display: block; }
.cover-role {
  color: var(--ink-strong);
  font-weight: 700;
}
.cover-unit { color: var(--ink); }
.cover-institution {
  margin-top: .25rem;
  color: var(--muted);
  font-size: .84rem;
}
.book-facts {
  display: flex;
  flex-wrap: wrap;
  gap: 1.45rem 2rem;
  margin: 0 0 2.7rem;
  padding: 1.15rem 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  list-style: none;
}
.book-facts strong {
  display: block;
  color: var(--ink-strong);
  font: 700 1.15rem var(--ui);
}
.book-facts span {
  color: var(--muted);
  font: 500 .7rem var(--ui);
  letter-spacing: .1em;
  text-transform: uppercase;
}
.cover-actions { display: flex; flex-wrap: wrap; gap: .75rem; }
.cover-actions a {
  display: inline-flex;
  align-items: center;
  padding: .72rem 1.18rem;
  border: 1px solid var(--line-strong);
  border-radius: 999px;
  font: 600 .84rem var(--ui);
  text-decoration: none;
  transition: transform .16s ease, box-shadow .16s ease, background-color .16s ease, border-color .16s ease;
}
.cover-actions .primary {
  border-color: var(--accent);
  background: var(--accent);
  color: #fff;
  box-shadow: 0 .12rem .4rem rgba(0, 0, 0, .13);
}
.cover-actions .primary:hover {
  border-color: var(--accent-deep);
  background: var(--accent-deep);
  color: #fff;
  transform: translateY(-1px);
  box-shadow: 0 .25rem .6rem rgba(0, 0, 0, .18);
}
.cover-actions .primary:active {
  transform: translateY(0);
  box-shadow: 0 .1rem .3rem rgba(0, 0, 0, .13);
}
.book-content {
  padding: 3.5rem 0 1rem;
  font-size: 1.075rem;
}
.book-content h2,
.book-content h3,
.book-content h4 {
  color: var(--ink-strong);
  font-family: var(--reading);
  line-height: 1.25;
  scroll-margin-top: 2rem;
}
.book-content h2 {
  margin: 4.5rem 0 1.3rem;
  padding-top: 1.45rem;
  border-top: 1px solid var(--line);
  font-size: clamp(1.75rem, 3.2vw, 2.18rem);
  letter-spacing: -.028em;
}
.book-content h2:first-child { margin-top: 0; }
.book-content h2[id^="chapter-"] {
  margin-top: 5.4rem;
  padding-top: 2rem;
}
.book-content h3 {
  margin: 2.6rem 0 .85rem;
  font-size: 1.42rem;
  letter-spacing: -.018em;
}
.book-content h4 {
  margin: 2.1rem 0 .65rem;
  font-size: 1.15rem;
}
.header-anchor {
  opacity: 0;
  margin-left: .45rem;
  color: var(--muted);
  font: 400 .7em var(--ui);
  text-decoration: none;
}
h2:hover .header-anchor, h3:hover .header-anchor, .header-anchor:focus { opacity: 1; }
p { margin: 0 0 1.18rem; }
strong { color: var(--ink-strong); }
em { color: var(--gold); }
.book-content ul, .book-content ol { margin: .35rem 0 1.45rem; padding-left: 1.7rem; }
.book-content li { margin: .35rem 0; padding-left: .2rem; }
hr { margin: 2.8rem 0; border: 0; border-top: 1px solid var(--line); }
blockquote {
  margin: 2rem 0;
  padding: 1.15rem 1.45rem;
  border-left: .22rem solid var(--accent);
  border-radius: 0 .4rem .4rem 0;
  background: var(--accent-soft);
  color: var(--ink);
  font-size: 1.08rem;
}
blockquote p:last-child { margin-bottom: 0; }
code {
  padding: .13em .36em;
  border: 1px solid var(--line);
  border-radius: .27rem;
  background: var(--paper-raised);
  color: var(--accent);
  font: .84em var(--mono);
}
pre {
  overflow-x: auto;
  margin: 1.7rem 0;
  padding: 1.35rem 1.45rem;
  border: 1px solid var(--line);
  border-radius: .6rem;
  background: var(--code-bg);
  box-shadow: 0 .4rem 1.1rem var(--shadow);
  color: #e4ecf4;
}
pre code {
  padding: 0;
  border: 0;
  background: none;
  color: inherit;
  font-size: .83rem;
  line-height: 1.7;
}
.highlight .k, .highlight .kd, .highlight .kn, .highlight .kr { color: #c792ea; }
.highlight .s, .highlight .s1, .highlight .s2, .highlight .sb { color: #c3e88d; }
.highlight .c, .highlight .c1, .highlight .cm { color: #8797a7; font-style: italic; }
.highlight .n, .highlight .nx, .highlight .nf { color: #82b9ff; }
.highlight .mi, .highlight .mf { color: #f59c76; }
.highlight .o { color: #44d692; }
table {
  display: block;
  overflow-x: auto;
  width: 100%;
  margin: 1.6rem 0;
  border: 1px solid var(--line);
  border-radius: .45rem;
  border-spacing: 0;
  border-collapse: separate;
  font: .88rem/1.55 var(--ui);
}
thead { background: var(--paper-raised); }
th {
  color: var(--ink-strong);
  font-weight: 700;
  text-align: left;
}
th, td { padding: .72rem .85rem; border-bottom: 1px solid var(--line); }
tr:last-child td { border-bottom: 0; }
.publication-footer {
  margin-top: 4.5rem;
  padding: 2rem 0;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font: .78rem/1.7 var(--ui);
  text-align: center;
}
@media (max-width: 72rem) {
  .toolbar {
    left: 0;
    justify-content: space-between;
    background: var(--bg);
    border-bottom: 1px solid var(--line);
  }
  .menu-button { display: inline-flex; }
  .sidebar { transform: translateX(-100%); transition: transform .2s ease; }
  .sidebar.open { transform: translateX(0); }
  .overlay.open {
    position: fixed;
    z-index: 29;
    inset: 0;
    display: block;
    background: rgba(0, 0, 0, .46);
  }
  .reader {
    width: min(100%, calc(var(--page-w) + 5rem));
    margin: 0 auto;
    padding-top: 2.8rem;
  }
}
@media (max-width: 40rem) {
  .reader { padding-left: 1.15rem; padding-right: 1.15rem; }
  .cover { padding-top: 4.5rem; min-height: auto; }
  .cover h1 { font-size: 2.55rem; }
  .cover-affiliations { grid-template-columns: 1fr; gap: .9rem; }
  .book-content { font-size: 1rem; }
  .tool-button .button-label { display: none; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { transition-duration: .001ms !important; }
}
@page { size: letter; margin: .75in .72in .7in; }
@media print {
  :root, [data-theme="light"] {
    --ink: #171513;
    --ink-strong: #111;
    --muted: #48433d;
    --accent: #111;
    --line: #cfc7ba;
    --paper-raised: #fff;
    --code-bg: #f2f2f2;
  }
  html, body { background: #fff !important; color: #111; font-size: 10.5pt; }
  .skip-link, .reading-progress, .toolbar, .sidebar, .overlay,
  .cover-actions, .header-anchor { display: none !important; }
  .reader { width: auto; margin: 0; padding: 0; }
  .cover {
    min-height: 8.45in;
    padding: 0;
    border: 0;
    page-break-after: always;
    break-after: page;
  }
  .cover .edition, .cover .book-facts { display: none !important; }
  .cover-art {
    display: block;
    width: 100%;
    max-width: 7.05in;
    max-height: 9.42in;
    margin: 0 auto;
    border-radius: 0;
    box-shadow: none;
    object-fit: contain;
  }
  .book-content { padding: 0; font-size: 10.7pt; }
  .book-content h2 { page-break-after: avoid; break-after: avoid; }
  .book-content #table-of-contents {
    page-break-before: always;
    break-before: page;
    page-break-after: avoid;
    break-after: avoid;
  }
  .book-content #table-of-contents + ol {
    page-break-after: always;
    break-after: page;
  }
  .book-content h2[id^="chapter-"],
  .book-content h2[id^="appendix-"] {
    page-break-before: always;
    break-before: page;
    margin-top: 0;
    padding-top: 0;
    border: 0;
  }
  .book-content h3, table, blockquote { page-break-after: avoid; break-after: avoid; }
  pre, table, blockquote { page-break-inside: avoid; break-inside: avoid; }
  pre {
    box-shadow: none;
    color: #111;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
  pre code, code { color: #111; }
  .highlight span { color: #111 !important; }
  a { color: #111; text-decoration: none; }
  .book-content a[href^="http"]::after {
    content: " (" attr(href) ")";
    color: #555;
    font-size: 8.5pt;
    overflow-wrap: anywhere;
  }
  .publication-footer { margin-top: .45in; }
}
"""


JS = r"""
(function () {
  "use strict";
  var root = document.documentElement;
  var toggle = document.getElementById("theme-toggle");
  var menu = document.getElementById("menu-toggle");
  var sidebar = document.getElementById("sidebar");
  var overlay = document.getElementById("overlay");
  var progress = document.getElementById("progress-fill");
  var key = "git-ebook-theme";

  function applyTheme(theme, remember) {
    root.dataset.theme = theme;
    if (remember) {
      try { localStorage.setItem(key, theme); } catch (error) {}
    }
    var next = theme === "dark" ? "light" : "dark";
    toggle.setAttribute("aria-label", "Switch to " + next + " mode");
    toggle.setAttribute("aria-pressed", String(theme === "light"));
    toggle.querySelector(".button-label").textContent =
      next.charAt(0).toUpperCase() + next.slice(1) + " mode";
  }

  try {
    var stored = localStorage.getItem(key);
    if (stored === "light" || stored === "dark") {
      applyTheme(stored, false);
    } else {
      applyTheme(root.dataset.theme, false);
    }
  } catch (error) {
    applyTheme(root.dataset.theme, false);
  }
  toggle.addEventListener("click", function () {
    applyTheme(root.dataset.theme === "dark" ? "light" : "dark", true);
  });

  function setMenu(open) {
    sidebar.classList.toggle("open", open);
    overlay.classList.toggle("open", open);
    menu.setAttribute("aria-expanded", String(open));
    if (open) sidebar.focus();
  }
  menu.addEventListener("click", function () {
    setMenu(!sidebar.classList.contains("open"));
  });
  overlay.addEventListener("click", function () { setMenu(false); });
  sidebar.addEventListener("click", function (event) {
    if (event.target.closest("a") && window.innerWidth <= 1152) setMenu(false);
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") setMenu(false);
  });

  var links = Array.from(document.querySelectorAll(".sidebar-nav a[href^='#']"));
  var headings = links.map(function (link) {
    return document.querySelector(link.getAttribute("href"));
  }).filter(Boolean);
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      links.forEach(function (link) { link.removeAttribute("aria-current"); });
      var active = links.find(function (link) {
        return link.getAttribute("href") === "#" + entry.target.id;
      });
      if (active) {
        active.setAttribute("aria-current", "location");
        active.scrollIntoView({ block: "nearest" });
      }
    });
  }, { rootMargin: "-12% 0px -76% 0px" });
  headings.forEach(function (heading) { observer.observe(heading); });

  function updateProgress() {
    var scrollable = document.documentElement.scrollHeight - window.innerHeight;
    var ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
    progress.style.width = Math.min(100, Math.max(0, ratio * 100)) + "%";
  }
  window.addEventListener("scroll", updateProgress, { passive: true });
  updateProgress();
}());
"""


def strip_front_matter(text: str) -> str:
    """Remove a leading YAML front matter block from the source Markdown."""
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)


def prepare_content(content_html: str) -> str:
    """Remove the duplicated Markdown title page; the HTML shell supplies a cover."""
    about_marker = '<h2 id="about-this-book">'
    start = content_html.find(about_marker)
    return content_html[start:] if start >= 0 else content_html


def schema_json() -> str:
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Book", "LearningResource"],
                "@id": f"{CANONICAL_URL}#book",
                "url": CANONICAL_URL,
                "name": f"{BOOK_TITLE}: {BOOK_SUBTITLE}",
                "description": "A complete, analogy-driven guide to version control for first-semester computer science students learning C++.",
                "author": {"@id": f"{AUTHOR_URL}#person"},
                "publisher": {"@id": f"{AUTHOR_URL}#person"},
                "datePublished": "2026-05-22",
                "bookEdition": "Digital Edition, Version 1.0",
                "inLanguage": "en",
                "educationalLevel": "Beginner",
                "learningResourceType": "Textbook",
                "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
                "about": [
                    {"@type": "Thing", "name": "Git"},
                    {"@type": "Thing", "name": "GitHub"},
                    {"@type": "Thing", "name": "C++ programming"},
                ],
                "isAccessibleForFree": True,
                "license": "https://creativecommons.org/licenses/by/4.0/",
                "image": SOCIAL_IMAGE,
                "mainEntityOfPage": {"@id": CANONICAL_URL},
                "isPartOf": {"@id": f"{SITE_URL}#website"},
            },
            {
                "@type": "WebPage",
                "@id": CANONICAL_URL,
                "url": CANONICAL_URL,
                "name": f"{BOOK_TITLE}: {BOOK_SUBTITLE}",
                "inLanguage": "en",
                "isPartOf": {"@id": f"{SITE_URL}#website"},
                "breadcrumb": {"@id": f"{CANONICAL_URL}#breadcrumb"},
                "mainEntity": {"@id": f"{CANONICAL_URL}#book"},
            },
            {
                "@type": "Person",
                "@id": f"{AUTHOR_URL}#person",
                "name": AUTHOR,
                "url": AUTHOR_URL,
                "affiliation": {"@id": f"{INSTITUTION_URL}#organization"},
            },
            {
                "@type": "CollegeOrUniversity",
                "@id": f"{INSTITUTION_URL}#organization",
                "name": INSTITUTION,
                "url": INSTITUTION_URL,
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}#website",
                "name": AUTHOR,
                "url": SITE_URL,
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{CANONICAL_URL}#breadcrumb",
                "name": f"Breadcrumbs for {BOOK_TITLE}",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Teaching",
                        "item": f"{SITE_URL}teaching/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": BOOK_TITLE,
                        "item": CANONICAL_URL,
                    },
                ],
            },
        ],
    }
    return json.dumps(schema, indent=2)


class LinkInspector(HTMLParser):
    """Collect URL-bearing elements and unsafe external-tab links."""

    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.unsafe_new_tabs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        for attr_name in ("href", "src"):
            value = attributes.get(attr_name)
            if value:
                self.urls.append(value)
        if tag == "a" and attributes.get("target") == "_blank":
            rel = set((attributes.get("rel") or "").lower().split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                self.unsafe_new_tabs.append(attributes.get("href") or "(missing href)")


def validate_output(html: str) -> None:
    """Fail the build if future book content introduces unsafe URL handling."""
    inspector = LinkInspector()
    inspector.feed(html)
    rejected_urls: list[str] = []
    for url in inspector.urls:
        if url.startswith("//"):
            rejected_urls.append(url)
            continue
        scheme = urlparse(url).scheme.lower()
        if scheme and scheme not in {"https", "mailto"}:
            rejected_urls.append(url)
    if rejected_urls:
        raise ValueError(f"Unsafe URL scheme in ebook output: {', '.join(sorted(set(rejected_urls)))}")
    if inspector.unsafe_new_tabs:
        raise ValueError(
            "External new-tab links require rel=\"noopener noreferrer\": "
            + ", ".join(sorted(set(inspector.unsafe_new_tabs)))
        )
    if f'<link rel="canonical" href="{CANONICAL_URL}" />' not in html:
        raise ValueError("Canonical ebook URL is missing from generated output.")


def validate_rendered_content(content_html: str) -> None:
    """Keep authored Markdown from emitting executable or embeddable page content."""
    prohibited_elements = re.compile(
        r"<\s*(script|style|iframe|object|embed|form|base|meta|link)\b",
        flags=re.IGNORECASE,
    )
    match = prohibited_elements.search(content_html)
    if match:
        raise ValueError(f"Prohibited HTML element in ebook source: <{match.group(1)}>")
    if re.search(r"\son[a-z]+\s*=", content_html, flags=re.IGNORECASE):
        raise ValueError("Inline event handler attributes are not allowed in ebook source.")


def build_html(toc_html: str, content_html: str, theme: str) -> str:
    title = f"{BOOK_TITLE}: {BOOK_SUBTITLE}"
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Avijit Roy</title>
  <meta name="description" content="A complete, analogy-driven guide to Git and GitHub for first-semester C++ students, with practical workflows and command references." />
  <meta name="keywords" content="Git ebook, GitHub tutorial, C++ students, version control, Git commands, Git workflow, computer science education" />
  <meta name="author" content="{AUTHOR}" />
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1" />
  <meta name="color-scheme" content="dark light" />
  <meta name="referrer" content="strict-origin-when-cross-origin" />
  <meta name="theme-color" content="#0b1118" />
  <link rel="canonical" href="{CANONICAL_URL}" />
  <meta property="og:type" content="book" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="A formal, print-ready ebook for students learning Git and GitHub through C++ coursework." />
  <meta property="og:url" content="{CANONICAL_URL}" />
  <meta property="og:image" content="{SOCIAL_IMAGE}" />
  <meta property="og:image:secure_url" content="{SOCIAL_IMAGE}" />
  <meta property="og:image:type" content="image/jpeg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Cover art for {title}, by {AUTHOR}" />
  <meta property="og:site_name" content="{AUTHOR}" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="A print-ready guide to Git and GitHub for C++ students." />
  <meta name="twitter:image" content="{SOCIAL_IMAGE}" />
  <meta name="twitter:image:alt" content="Cover art for {title}, by {AUTHOR}" />
  <link rel="icon" href="../../assets/favicons/favicon.ico" sizes="any" />
  <link rel="icon" href="../../assets/favicons/icon.svg" type="image/svg+xml" />
  <link rel="apple-touch-icon" href="../../assets/favicons/apple-touch-icon.png" />
  <link rel="manifest" href="../../assets/favicons/site.webmanifest" />
  <link rel="mask-icon" href="../../assets/favicons/safari-pinned-tab.svg" color="#37c87b" />
  <link rel="preload" as="image" href="{COVER_IMAGE_PATH}" fetchpriority="high" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&amp;family=Sora:wght@400;500;600;700&amp;family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&amp;display=swap" rel="stylesheet" />
  <script type="application/ld+json">
{schema_json()}
  </script>
  <style>{CSS}</style>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ANALYTICS_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{ANALYTICS_ID}');
</script>
</head>
<body>
  <a class="skip-link" href="#book-content">Skip to book content</a>
  <div class="reading-progress" aria-hidden="true"><span id="progress-fill"></span></div>
  <header class="toolbar" aria-label="Reading tools">
    <button class="tool-button menu-button" id="menu-toggle" type="button" aria-controls="sidebar" aria-expanded="false">
      <span aria-hidden="true">&#9776;</span><span class="button-label">Contents</span>
    </button>
    <button class="tool-button" id="theme-toggle" type="button" aria-label="Switch color mode" aria-pressed="false">
      <span aria-hidden="true">&#9680;</span><span class="button-label">Light mode</span>
    </button>
  </header>
  <div class="overlay" id="overlay" aria-hidden="true"></div>
  <div class="layout">
    <aside class="sidebar" id="sidebar" aria-label="Ebook navigation" tabindex="-1">
      <div class="sidebar-header">
        <span class="sidebar-kicker">Digital Edition</span>
        <a class="sidebar-title" href="#cover">{BOOK_TITLE}</a>
        <span class="sidebar-subtitle">{BOOK_SUBTITLE}<br />By <a href="{AUTHOR_URL}">{AUTHOR}</a></span>
      </div>
      <nav class="sidebar-nav" aria-label="Chapters and book sections">
        {toc_html}
      </nav>
      <div class="sidebar-footer">17 chapters &middot; Approx. 90 minutes<br />CC BY 4.0 &middot; CSCI 271 / CSCI 272</div>
    </aside>
    <main class="reader" id="book-content">
      <header class="cover" id="cover">
        <div class="edition">Digital Edition &middot; Version 1.0</div>
        <img class="cover-art" src="{COVER_IMAGE_PATH}" width="1100" height="1422" alt="Cover of {title}, by {AUTHOR}." fetchpriority="high" />
        <h1 id="saving-your-work-like-a-pro">Saving Your Work <span>Like a Pro</span></h1>
        <p class="cover-description" id="git-github-for-c-students">Git &amp; GitHub for C++ Students: a complete, analogy-driven guide to version control, collaboration, and recovery.</p>
        <div class="cover-byline">
          <p class="cover-credit">Written by <strong>{AUTHOR}</strong></p>
          <div class="cover-affiliations" aria-label="Academic appointments">
            <div class="cover-affiliation">
              <span class="cover-role">Substitute Lecturer</span>
              <span class="cover-unit">Computer Science</span>
              <span class="cover-institution">{INSTITUTION}</span>
            </div>
            <div class="cover-affiliation">
              <span class="cover-role">Adjunct Assistant Professor</span>
              <span class="cover-unit">Collins College of Professional Studies</span>
              <span class="cover-institution">St. John's University</span>
            </div>
          </div>
        </div>
        <ul class="book-facts" aria-label="Publication details">
          <li><strong>17</strong><span>Chapters</span></li>
          <li><strong>3</strong><span>Appendices</span></li>
          <li><strong>~90 min</strong><span>Reading time</span></li>
          <li><strong>CC BY 4.0</strong><span>License</span></li>
        </ul>
        <div class="cover-actions">
          <a class="primary" href="#about-this-book">Begin reading</a>
          <a href="#table-of-contents">View contents</a>
        </div>
      </header>
      <article class="book-content">
        {content_html}
      </article>
      <footer class="publication-footer">
        <p>&copy; {YEAR} <a href="{AUTHOR_URL}">{AUTHOR}</a>. Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a>.<br />Prepared for CSCI 271 / CSCI 272 at <a href="{INSTITUTION_URL}">{INSTITUTION}</a>.</p>
      </footer>
    </main>
  </div>
  <script>{JS}</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the standalone Git and GitHub ebook.")
    parser.add_argument("--source", default=SOURCE_FILE, help="Markdown source file")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="HTML output file")
    parser.add_argument(
        "--theme",
        choices=["dark", "light"],
        default="dark",
        help="Initial reader theme; readers can switch themes in the published ebook.",
    )
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"Error: source file '{source_path}' not found.")
        sys.exit(1)

    source = strip_front_matter(source_path.read_text(encoding="utf-8"))
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "tables",
            "attr_list",
            "def_list",
            "abbr",
            "footnotes",
            CodeHiliteExtension(css_class="highlight", guess_lang=True, noclasses=False),
            TocExtension(permalink=True, permalink_class="header-anchor", toc_depth="2"),
        ]
    )
    rendered = md.convert(source)
    content_html = prepare_content(rendered)
    validate_rendered_content(content_html)
    toc_html = md.toc if hasattr(md, "toc") else ""
    final_html = build_html(toc_html, content_html, args.theme)
    validate_output(final_html)
    output_path = Path(args.output)
    output_path.write_text(final_html, encoding="utf-8")

    size_kb = output_path.stat().st_size / 1024
    print(f"Built: {output_path} ({size_kb:.1f} KB)")
    print(f"Initial theme: {args.theme} (toggle enabled in document)")
    print(f"Canonical URL: {CANONICAL_URL}")
    print("URL safety: verified HTTPS/relative links and safe new-tab handling")
    print(f"Source: {source_path} ({len(source.splitlines())} lines)")


if __name__ == "__main__":
    main()
