import { type CollectionEntry, getCollection } from 'astro:content';
import type { Locale } from './i18n';

export type BlogPost = CollectionEntry<'blog'>;
export type Section = CollectionEntry<'sections'>;

/**
 * Post ids are `<locale>/<section>/<slug>`, so the public path is
 * everything after the locale: `evals/llm-evals`.
 */
export function getPostPathParts(post: BlogPost): { locale: string; section: string; slug: string } {
  const [locale = '', section = '', ...rest] = post.id.split('/');
  return { locale, section, slug: rest.join('/') };
}

export function getPostSection(post: BlogPost): string {
  return getPostPathParts(post).section;
}

export function getPostSlug(post: BlogPost): string {
  return getPostPathParts(post).slug;
}

export function getSectionSlug(section: Section): string {
  return section.id.split('/').pop() ?? section.id;
}

export async function getSections(locale: Locale): Promise<Section[]> {
  const sections = await getCollection(
    'sections',
    (entry: Section) => entry.id.startsWith(`${locale}/`) && !entry.data.draft
  );
  return sections.sort((a: Section, b: Section) => {
    const byOrder = a.data.order - b.data.order;
    return byOrder !== 0 ? byOrder : a.data.title.localeCompare(b.data.title);
  });
}

export async function getPosts(locale: Locale): Promise<BlogPost[]> {
  const posts = await getCollection(
    'blog',
    (post: BlogPost) => post.id.startsWith(`${locale}/`) && !post.data.draft
  );
  return posts.sort((a: BlogPost, b: BlogPost) => b.data.date.valueOf() - a.data.date.valueOf());
}

/** Pinned posts first, then the rest, newest first. */
export function splitPinned(posts: BlogPost[]): { pinned: BlogPost[]; recent: BlogPost[] } {
  return {
    pinned: posts.filter((post: BlogPost) => post.data.pinned),
    recent: posts.filter((post: BlogPost) => !post.data.pinned),
  };
}

export function getPostHref(post: BlogPost, locale: Locale): string {
  const { section, slug } = getPostPathParts(post);
  return `/${locale}/${section}/${slug}/`;
}

const WORDS_PER_MINUTE = 200;

export function readingTime(
  body: string | undefined,
  explicitMinutes?: number
): { minutes: number; words: number } {
  const text = (body ?? '').trim();
  const words = text ? text.split(/\s+/).length : 0;
  const minutes = explicitMinutes ?? Math.max(1, Math.round(words / WORDS_PER_MINUTE));
  return { minutes, words };
}

/**
 * Static paths for `/[locale]/[section]/[slug].astro`.
 */
export async function getPostStaticPaths(locale: Locale) {
  const posts = await getPosts(locale);
  return posts.map((post: BlogPost) => {
    const { section, slug } = getPostPathParts(post);
    return {
      params: { section, slug },
      props: { post },
    };
  });
}

/**
 * Static paths for `/[locale]/[section]/index.astro`.
 */
export async function getSectionStaticPaths(locale: Locale) {
  const sections = await getSections(locale);
  return sections.map((section: Section) => ({
    params: { section: getSectionSlug(section) },
    props: { section },
  }));
}
