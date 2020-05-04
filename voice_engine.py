<<<<<<< HEAD
from gtts import gTTS, lang
import playsound
import os
import pprint
import speech_recognition as sr

#function to convert text to speech 
def speak(text, l):
	tts = gTTS(text, lang=l)
	filename = "temp.mp3"
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)

#function that picks up audio and converts speech to text
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		text = ""
		try:
			said = r.recognize_google(audio)
			return said
		except Exception as e:
			print(str(e))


"""
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
 'en-au': 'English (Australia)',
 'en-ca': 'English (Canada)',
 'en-gb': 'English (UK)',
 'en-gh': 'English (Ghana)',
 'en-ie': 'English (Ireland)',
 'en-in': 'English (India)',
 'en-ng': 'English (Nigeria)',
 'en-nz': 'English (New Zealand)',
 'en-ph': 'English (Philippines)',
 'en-tz': 'English (Tanzania)',
 'en-uk': 'English (UK)',
 'en-us': 'English (US)',
 'en-za': 'English (South Africa)',
 'eo': 'Esperanto',
 'es': 'Spanish',
 'es-es': 'Spanish (Spain)',
 'es-us': 'Spanish (United States)',
 'et': 'Estonian',
 'fi': 'Finnish',
 'fr': 'French',
 'fr-ca': 'French (Canada)',
 'fr-fr': 'French (France)',
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
 'pt-br': 'Portuguese (Brazil)',
 'pt-pt': 'Portuguese (Portugal)',
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

 def getLanguageDic():
	return language_dic
"""
=======
import pyttsx3

class voice_engine:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()

    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()
>>>>>>> fc06e060bb568ef6b1e67c3d542756bbfb60ad26
