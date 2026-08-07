/* Apply the preferred theme before CSS paints the page. */
(function () {
  var root = document.documentElement;
  var savedTheme = null;

  try {
    savedTheme = localStorage.getItem("theme");
  } catch (error) {
    // Storage can be unavailable in restricted browsing contexts.
  }

  var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  var theme = savedTheme === "light" || savedTheme === "dark"
    ? savedTheme
    : (prefersDark ? "dark" : "light");

  root.setAttribute("data-theme", theme);
  root.style.colorScheme = theme;
})();
