import { type Locale, localeTags } from './i18n';

/** Long, locale-aware date: "9 tháng 9, 2026" / "September 9, 2026". */
export function formatDate(date: Date, locale: Locale): string {
  return date.toLocaleDateString(localeTags[locale], {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

/** Machine-readable date for <time datetime="…">. */
export function isoDate(date: Date): string {
  return date.toISOString().slice(0, 10);
}
