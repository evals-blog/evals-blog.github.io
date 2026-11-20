/**
 * Locale helpers. Unlike the astro-v7-template (which leaves the default locale
 * unprefixed), both locales are URL-prefixed here — /vi/… and /en/… — so the URLs
 * match the original Hugo site and no inbound link breaks.
 */
export const defaultLocale = 'vi' as const;
export const locales = ['vi', 'en'] as const;
export type Locale = (typeof locales)[number];

export const localeNames: Record<Locale, string> = {
  vi: 'Tiếng Việt',
  en: 'English',
};

/** Short label used in the language switch. */
export const localeShort: Record<Locale, string> = {
  vi: 'VI',
  en: 'EN',
};

/** BCP 47 tags for <html lang> and Intl date formatting. */
export const localeTags: Record<Locale, string> = {
  vi: 'vi-VN',
  en: 'en-US',
};

export function isLocale(value: string): value is Locale {
  return (locales as readonly string[]).includes(value);
}

export function getLocaleFromPath(pathname: string): Locale {
  const segment = pathname.split('/')[1] ?? '';
  return isLocale(segment) ? segment : defaultLocale;
}

export function otherLocale(locale: Locale): Locale {
  return locale === 'vi' ? 'en' : 'vi';
}

/** Build an absolute site path for a locale: localePath('/evals/', 'en') → '/en/evals/' */
export function localePath(path: string, locale: Locale): string {
  const clean = path.startsWith('/') ? path : `/${path}`;
  return clean === '/' ? `/${locale}/` : `/${locale}${clean}`;
}

/** Swap the locale segment of any path, keeping the trailing slash. */
export function switchLocalePath(pathname: string, newLocale: Locale): string {
  const segments = pathname.split('/').filter(Boolean);
  if (segments.length > 0 && isLocale(segments[0] as string)) {
    segments.shift();
  }
  return `/${[newLocale, ...segments].join('/')}/`;
}
