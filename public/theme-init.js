/* Sets the theme before first paint, loaded from BaseLayout as a file (not inline)
   so a future CSP with 'self' keeps working. */
function getStoredTheme() {
  try {
    const cookieTheme = document.cookie.match(/(?:^|;\s*)theme=(dark|light)(?:;|$)/)?.[1];
    return cookieTheme || localStorage.getItem('theme');
  } catch {
    return null;
  }
}

function applyTheme() {
  document.documentElement.classList.remove('no-js');
  const storedTheme = getStoredTheme();
  if (
    storedTheme === 'dark' ||
    (!storedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)
  ) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

applyTheme();
