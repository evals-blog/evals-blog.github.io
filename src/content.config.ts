import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

/**
 * Posts live one folder per locale, mirroring the Hugo source layout:
 *   src/content/blog/<locale>/<section>/<slug>.md  →  id <locale>/<section>/<slug>
 * so a post URL is /<locale>/<section>/<slug>/.
 */
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string().min(1),
    description: z.string().min(10),
    summary: z.string().optional(),
    date: z.coerce.date(),
    lastmod: z.coerce.date().optional(),
    author: z.string().default('Thuat Nguyen'),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    /** Hugo's `pinned`: shown in the "featured" block on the home page. */
    pinned: z.boolean().default(false),
    /** Path under /public, e.g. /images/posts/daily-tips/agent-skills/cover.svg */
    featuredImage: z.string().optional(),
    readTime: z.number().optional(),
  }),
});

/**
 * Topic landing pages (Hugo `_index.md`): src/content/sections/<locale>/<section>.md
 */
const sections = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/sections' }),
  schema: z.object({
    title: z.string().min(1),
    description: z.string().min(10),
    /** Display order in the navigation and on the home page. */
    order: z.number().default(0),
    /** draft: true hides the topic page entirely — no nav entry, no route. */
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog, sections };
