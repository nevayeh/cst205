
import pprint
import googletrans
from googletrans import Translator
dic = {
 'af': 'afr',
 'ar': 'ara',
 'be': 'bel',
 'bn': 'ben',
 'bs': 'bos',
 'ca': 'cat',
 'cy': 'cym',
 'da': 'dan',
 'de': 'deu',
 'el': 'ell',
 'en': 'eng',
 'eo': 'epo',
 'es': 'spa',
 'et': 'est',
 'fi': 'fin',
 'fr': 'fra',
 'gu': 'guj',
 'hi': 'hin',
 'hr': 'hrv',
 'hu': 'hun',
 'id': 'ind',
 'is': 'isl',
 'it': 'ita',
 'ja': 'jpn',
 'jw': 'jav',
 'km': 'khm',
 'kn': 'kan',
 'ko': 'kor',
 'la': 'lat',
 'lv': 'lav',
 'mk': 'mkd',
 'ml': 'mal',
 'mr': 'mar',
 'my': 'mya',
 'ne': 'nep',
 'nl': 'nld',
 'no': 'nor',
 'pl': 'pol',
 'pt': 'por',
 'ro': 'ron',
 'ru': 'rus',
 'si': 'sin',
 'sk': 'slk',
 'sq': 'sqi',
 'sr': 'srp',
 'sv': 'swe',
 'sw': 'swa',
 'ta': 'tel',
 'th': 'tha',
 'tr': 'tur',
 'uk': 'ukr',
 'ur': 'urd',
 'vi': 'vie',
 'yi': 'yid',
 'zh-cn': 'chi_sim',
 'zh-tw': 'chi_tra'
}

language_dic = {
 'af': 'Afrikaans',
 'ar': 'Arabic',
 'bn': 'Bengali',
 'bs': 'Bosnian',
 'ca': 'Catalan',
 'cs': 'Czech',
 'cy': 'Welsh',
 'da': 'Danish',
 'de': 'German',
 'el': 'Greek',
 'en': 'English',
 'eo': 'Esperanto',
 'es': 'Spanish',
 'et': 'Estonian',
 'fi': 'Finnish',
 'fr': 'French',
 'gu': 'Gujarati',
 'hi': 'Hindi',
 'hr': 'Croatian',
 'hu': 'Hungarian',
 'hy': 'Armenian',
 'id': 'Indonesian',
 'is': 'Icelandic',
 'it': 'Italian',
 'ja': 'Japanese',
 'jw': 'Javanese',
 'km': 'Khmer',
 'kn': 'Kannada',
 'ko': 'Korean',
 'la': 'Latin',
 'lv': 'Latvian',
 'mk': 'Macedonian',
 'ml': 'Malayalam',
 'mr': 'Marathi',
 'my': 'Myanmar (Burmese)',
 'ne': 'Nepali',
 'nl': 'Dutch',
 'no': 'Norwegian',
 'pl': 'Polish',
 'pt': 'Portuguese',
 'ro': 'Romanian',
 'ru': 'Russian',
 'si': 'Sinhala',
 'sk': 'Slovak',
 'sq': 'Albanian',
 'sr': 'Serbian',
 'su': 'Sundanese',
 'sv': 'Swedish',
 'sw': 'Swahili',
 'ta': 'Tamil',
 'te': 'Telugu',
 'th': 'Thai',
 'tl': 'Filipino',
 'tr': 'Turkish',
 'uk': 'Ukrainian',
 'ur': 'Urdu',
 'vi': 'Vietnamese',
 'zh-cn': 'Chinese (Mandarin/China)',
 'zh-tw': 'Chinese (Mandarin/Taiwan)'
 }

dd = {
 'afr': 'af',
 'ara': 'ar',
 'bel': 'be',
 'ben': 'bn',
 'bos': 'bs',
 'cat': 'ca',
 'chi_sim': 'zh-cn',
 'chi_tra': 'zh-tw',
 'cym': 'cy',
 'dan': 'da',
 'deu': 'de',
 'ell': 'el',
 'eng': 'en',
 'epo': 'eo',
 'est': 'et',
 'fin': 'fi',
 'fra': 'fr',
 'guj': 'gu',
 'hin': 'hi',
 'hrv': 'hr',
 'hun': 'hu',
 'ind': 'id',
 'isl': 'is',
 'ita': 'it',
 'jav': 'jw',
 'jpn': 'ja',
 'kan': 'kn',
 'khm': 'km',
 'kor': 'ko',
 'lat': 'la',
 'lav': 'lv',
 'mal': 'ml',
 'mar': 'mr',
 'mkd': 'mk',
 'mya': 'my',
 'nep': 'ne',
 'nld': 'nl',
 'nor': 'no',
 'pol': 'pl',
 'por': 'pt',
 'ron': 'ro',
 'rus': 'ru',
 'sin': 'si',
 'slk': 'sk',
 'spa': 'es',
 'sqi': 'sq',
 'srp': 'sr',
 'swa': 'sw',
 'swe': 'sv',
 'tel': 'ta',
 'tha': 'th',
 'tur': 'tr',
 'ukr': 'uk',
 'urd': 'ur',
 'vie': 'vi',
 'yid': 'yi'
}

 other_dic = {
	 'af': 'afrikaans',
	 'ar': 'arabic',
	 'bn': 'bengali',
	 'bs': 'bosnian',
	 'ca': 'catalan',
	 'cs': 'czech',
	 'cy': 'welsh',
	 'da': 'danish',
	 'de': 'german',
	 'el': 'greek',
	 'en': 'english',
	 'eo': 'esperanto',
	 'es': 'spanish',
	 'et': 'estonian',
	 'fi': 'finnish',
	 'fr': 'french',
	 'gu': 'gujarati',
	 'hi': 'hindi',
	 'hr': 'croatian',
	 'hu': 'hungarian',
	 'hy': 'armenian',
	 'id': 'indonesian',
	 'is': 'icelandic',
	 'it': 'italian',
	 'ja': 'japanese',
	 'jw': 'javanese',
	 'km': 'khmer',
	 'kn': 'kannada',
	 'ko': 'korean',
	 'la': 'latin',
	 'lv': 'latvian',
	 'mk': 'macedonian',
	 'ml': 'malayalam',
	 'mr': 'marathi',
	 'my': 'myanmar (burmese)',
	 'ne': 'nepali',
	 'nl': 'dutch',
	 'no': 'norwegian',
	 'pl': 'polish',
	 'pt': 'portuguese',
	 'ro': 'romanian',
	 'ru': 'russian',
	 'si': 'sinhala',
	 'sk': 'slovak',
	 'sq': 'albanian',
	 'sr': 'serbian',
	 'su': 'sundanese',
	 'sv': 'swedish',
	 'sw': 'swahili',
	 'ta': 'tamil',
	 'te': 'telugu',
	 'th': 'thai',
	 'tl': 'filipino',
	 'tr': 'turkish',
	 'uk': 'ukrainian',
	 'ur': 'urdu',
	 'vi': 'vietnamese',
	 'zh-cn': 'chinese (simplified)',
	 'zh-tw': 'chinese (traditional)'
 }

#new_dict = dict([(value, key) for key, value in dic.items()]) 
#sorted(new_dict)
langDict = googletrans.LANGUAGES
pprint.pprint(langDict)
