import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

// Deployed as a GitHub Pages *user* site, so the site is served from the domain root
// and no `base` path is needed.
export default defineConfig({
  site: 'https://evals-blog.github.io',
  trailingSlash: 'always',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  server: {
    host: true,
    port: 4323,
  },
});
