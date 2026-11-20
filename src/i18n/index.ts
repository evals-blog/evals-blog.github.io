import type { Locale } from '@/utils/i18n';
import en from './en';
import vi from './vi';

export type TranslationKey = keyof typeof en;

const dictionaries: Record<Locale, Record<TranslationKey, string>> = { en, vi };

/** Returns a synchronous translate function for one locale: `const tr = t(locale); tr('home.title')` */
export function t(locale: Locale): (key: TranslationKey) => string {
  const dictionary = dictionaries[locale] ?? en;
  return (key: TranslationKey) => dictionary[key] ?? en[key] ?? key;
}
