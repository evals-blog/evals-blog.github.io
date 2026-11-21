# Evals Blog — Astro blog

Bilingual (Vietnamese / English) blog for **Evals Blog by Thuat Nguyen**, migrated from the Hugo
site `evals-blog/evals-blog.github.io` to **Astro 7 + Tailwind CSS 4**, structured after
[`casoon/astro-v7-template`](https://github.com/casoon/astro-v7-template) and deployable to
GitHub Pages.

The brand shown in `<title>`, the header wordmark and the footer is **Evals Blog**. The home
page's own heading is the longer **Evals Blog by Thuat Nguyen**, with the tagline **Testing for
better** beneath it. The author name otherwise appears only as post byline and in the footer
copyright line.

The site has two topics — **Kiểm thử / Testing** (`testing`) and **Daily tips** (`daily-tips`) — and
two posts, each published in both languages. Keep topic and post slugs identical across locales:
`BaseLayout` builds the `hreflang` alternates by swapping only the locale segment, so a slug that
exists in one language only would advertise a 404.

## Quick start

```bash
npm install
npm run dev      # http://localhost:4323
npm run build    # static output in dist/
npm run preview
```

Requires Node **22.23.4+** (Astro 7's minimum).

## URLs

Both languages are path-prefixed, matching the old Hugo URLs exactly, so no inbound link
breaks:

| Page | URL |
| --- | --- |
| Home (VI) | `/vi/` |
| Home (EN) | `/en/` |
| Topic pages | `/vi/testing/` · `/vi/daily-tips/` (and `/en/…`) |
| Posts | `/vi/testing/em-test-ung-dung-nay-ky-chua/` · `/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it/` |
| Root | `/` → redirects to `/vi/` (the old site's default language) |

Live topics: `testing` (order 5), `daily-tips` (order 10).

## Project structure

```
src/
  content.config.ts        # blog + sections collections (Zod schemas)
  content/
    blog/<locale>/<section>/<slug>.md    # posts
    sections/<locale>/<section>.md       # topic landing pages
  layouts/BaseLayout.astro  # <head>, meta/OG, hreflang, theme init
  components/
    Header.astro            # text wordmark, topic nav, lang switch, theme toggle
    Footer.astro
    PostCard.astro
    PostPage.astro          # article shell + prose
    SectionPage.astro       # topic page
    HomePage.astro          # hero, featured, latest, topics
    Tag.astro
    ThemeToggle.astro
  i18n/                     # en.ts, vi.ts, index.ts — `t(locale)('home.title')`
  utils/                    # i18n path helpers, post queries, date formatting
  styles/app.css            # Tailwind 4 + design tokens + typography
  pages/
    index.astro             # → /vi/
    [locale]/index.astro
    [locale]/[section]/index.astro
    [locale]/[section]/[slug].astro
    404.astro
public/
  images/posts/<locale>/<section>/<slug>/*.svg   # post diagrams
  favicon.svg
  theme-init.js             # sets the theme before first paint
```

## Hugo → Astro mapping

| Hugo | Astro |
| --- | --- |
| `content/<locale>/<section>/<slug>/index.md` | `src/content/blog/<locale>/<section>/<slug>.md` |
| `content/<locale>/<section>/_index.md` | `src/content/sections/<locale>/<section>.md` |
| TOML frontmatter (`+++`) | YAML frontmatter (`---`) |
| `featured_image = 'cover.svg'` | `featuredImage: '/images/posts/…/cover.svg'` |
| `pinned = true` | `pinned: true` (drives the "Featured" block) |
| `show_reading_time` | dropped — reading time is computed from the word count |
| `[menu.main]` block | dropped — navigation comes from the `sections` collection (`order`) |
| `hugo.toml` languages | `src/utils/i18n.ts` (`locales`, `localePath`) |
| `i18n/*.toml` strings | `src/i18n/*.ts` |
| `layouts/` (Ananke theme) | `src/layouts` + `src/components` |
| `themes/ananke` submodule | removed — no theme dependency |

### Frontmatter schema

```yaml
---
title: 'Why AI hallucinates and how to handle it'
description: '…'                       # required, min 10 chars
summary: '…'                           # optional card blurb
date: '2026-09-05T21:10:32+07:00'
draft: false                           # draft: true hides the post entirely
pinned: true                           # optional
featuredImage: '/images/posts/en/daily-tips/why-ai-hallucinates-and-how-to-handle-it/cover.svg'
tags: []                               # optional
---
```

## Current content

Two posts are published, in both languages:

```
src/content/blog/en/testing/em-test-ung-dung-nay-ky-chua.md
src/content/blog/vi/testing/em-test-ung-dung-nay-ky-chua.md
src/content/blog/en/daily-tips/why-ai-hallucinates-and-how-to-handle-it.md
src/content/blog/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it.md
```

The other ten posts are still on disk but carry `draft: true`, so the content collection and
`getStaticPaths` skip them: no page is generated, and nothing links to them. The three retired
topic pages (`evals`, `rag`, `prompting`) carry `draft: true` for the same reason — they vanish
from the header nav, the footer, the home-page topic grid and routing. To delete all of it for
good (this sandbox had no shell, so nothing could be removed here):

```bash
git rm -r src/content/sections/en/{evals,rag,prompting}.md \
          src/content/sections/vi/{evals,rag,prompting}.md \
          src/content/blog/en/{evals,rag,prompting} \
          src/content/blog/en/daily-tips/{agent-skills,what-are-ai-agents}.md \
          src/content/blog/vi/{evals,rag,prompting} \
          src/content/blog/vi/daily-tips/{agent-skills,what-are-ai-agents}.md
```

Their SVGs under `public/images/posts/<locale>/<section>/<slug>/` become unused at the same point.

## What changed from the Hugo site

- **Logo removed.** Hugo's `site_logo = "images/logo.jpg"` and the header image are gone; the
  header now uses a text wordmark. No `logo.*` asset is shipped. A neutral `favicon.svg`
  replaces the logo-derived icon.
- **Theme is Ananke-free.** The site uses Tailwind 4 with an OKLCH token system ported from the
  astro-v7-template, plus light/dark toggle (`theme-init.js` + `.dark` class, persisted in
  `localStorage` and a cookie).
- **Rebranded.** Header, footer, `<title>` and home heading all read *Evals Blog*; the home
  tagline is *Testing for better* (kept in English for both locales, like the brand name).
- **Footer** shows the wordmark, `© <year> Thuat Nguyen`, the topic links and the language
  switch — the "All rights reserved." line was removed.
- **Two topics, two posts.** `testing` (order 5) and `daily-tips` (order 10) are live; the other
  three topics are draft and no longer appear anywhere. Published posts, both languages:
  *Em test ứng dụng này kỹ chưa?* (new) and *Why AI hallucinates and how to handle it*.
- **Content is otherwise verbatim.** Prose and SVG diagrams were ported unchanged, except that
  the post's "Read next" block (which pointed at the retired topics) was dropped, and the
  `daily-tips` intro lost its links to them, so no internal link 404s.
- **Reading time** is derived from word count instead of Hugo's `show_reading_time` flag.

## Deviations from `casoon/astro-v7-template`

The template is a **pnpm monorepo** (`apps/blog`, `apps/starter`, `shared`, pnpm `catalog:`
versions) that deploys to **Cloudflare** and pulls in proprietary `@casoon/*` integrations,
Svelte components, MDX and env validation. This project keeps the template's *architecture and
design language* — content collections with a glob loader and Zod schema, `useTranslations`-style
i18n, `BaseLayout` + `HomePage`/`PostPage` split, OKLCH design tokens, `theme-init.js` — but as a
**single-app, static, npm project**, because:

- GitHub Pages needs a plain static `dist/`, not a Workers adapter.
- A single app avoids the workspace `catalog:` protocol and a pnpm lockfile that could not be
  generated here.
- Dropping Svelte/MDX/`@casoon/*` removes install-time and build-time failure modes for a site
  made of Markdown and SVGs.

Net: no Svelte, no MDX, no Cloudflare, no `@casoon/*` packages. Everything else follows the
template.

## Deploy to GitHub Pages

1. Create the repo `evals-blog/evals-blog.github.io` (or push this project to it) with `main` as
   the default branch.
2. In **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**.
3. Push to `main`. `.github/workflows/deploy.yml` installs dependencies, builds, and deploys
   `dist/` through `actions/deploy-pages`.
4. The site appears at `https://evals-blog.github.io/`.

`astro.config.mjs` sets `site: 'https://evals-blog.github.io'` with no `base`, since this is a
user site served from the domain root. If you ever move it to a **project** page
(`https://<user>.github.io/<repo>/`), add `base: '/<repo>'` and prefix absolute `/images/…`
paths — note that both are currently root-absolute.

`public/.nojekyll` is included so Pages never runs the output through Jekyll.

## Known gaps

- **No `package-lock.json`.** `npm install` runs in CI. Run `npm install` locally once and commit
  the lockfile, then switch the workflow step to `npm ci` for reproducible builds.
- **The site has not been built in this environment.** The shell/job runner was unavailable
  throughout the migration (`subprocess-local: Windows Job runner exited with exit code 216`), so
  `npm install`, `astro build` and `astro check` were never executed here. The source was reviewed
  statically instead (imports/exports, Astro 7 content API, route params, Tailwind tokens, schema
  vs frontmatter, and every image/link reference in all 20 content files). Run the commands under
  "Verifying" before publishing.
- **Leftover probe files** from that workaround, safe to delete:
  `public/images/posts/en/.truncation-probe.txt`, `.truncation-probe2.txt`,
  `.len-2000-probe.txt`, `.edit-probe-test.svg`. They are dot-files and are not referenced by any
  page.

## Verifying

```bash
npm install
npm run check     # astro check: types + content schema
npm run build     # every post must render; getStaticPaths fails loudly on a bad slug
npm run preview   # check /vi/, /en/, both topic pages and a post
```

If a build fails on the content schema, the message names the offending file — usually a
frontmatter value that needs different quoting (single quotes containing an apostrophe).
