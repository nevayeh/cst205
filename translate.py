# Diana Danvers
# Translator class for 205 Final Project: Enuncreate
# Object created detects the language passed into it and translate it 
# into English or a chosen language. Languages are chosen from the langTrans
# 
# Sample - Spanish and English
# x = transClass()
# print(x.transChoose("Hello World", "es") -> Hola Mundo 
# print(x.transEN("Hola Mundo") -> Hello World

import googletrans
from googletrans import Translator
from dict import langTrans

class transClass:

	def __init__(self):
		self.translator = Translator()	
		#self.langDict = googletrans.LANGUAGES
		self.langDict = langTrans().google_trans_languages
		self.langCodes = dict(map(reversed, self.langDict.items()))
		self.langTrans = langTrans()	
	
		self.src = ""
		self.srcLang = ""
		self.srcText = ""
		self.howToS = ""

		self.dest = ""
		self.destLang = ""
		self.destText = ""
		self.howToD = ""

	# Detect Language
	def detectLang(self, text):
		self.srcText = text
		self.src = self.translator.detect(self.srcText).lang
		self.srcLang = self.langDict[self.src].title()
		self.howToS = self.pronounce(self.srcText, self.src)

	# Attempt to get pronounciation: May not always be available
	def pronounce(self, text, language):
		pronunce = self.translator.translate(text, dest=language).pronunciation
		if(pronunce == "" or pronunce == None):
			return "Not Available"
		else:
			return pronunce
		
	# Translate: From [Detect Language] to [English]	
	def transEN(self, text):
		self.detectLang(text)
		self.dest = "en"
		self.translate()

	# Translate: From [Detect Language] to [Choose Language]
	def transChoose(self, text, langDest):
		self.detectLang(text)
		if(len(langDest) == 3):
			self.dest = self.tesTOtra(langDest)
		else :
			self.dest = langDest
		
		self.translate()
	
	# Actual translation
	def translate(self):
		self.destLang = self.langDict[self.dest].title()
		self.destText = self.translator.translate(self.srcText, dest=self.dest).text
		self.howToD = self.pronounce(self.destText, self.dest)
	
	# Send language code across libraries
	def tesTOtra(self, langDest):
		return self.langTrans.dict[langDest]

	# Vice Versa
	def traTOtes(self, langDest):
		return self.langTrans.rDict[langDest]

	# Output all data
	def report(self):
		print("Source LanCode: " + self.src)
		print("Source Language: " + self.srcLang)
		print("Source Text: " + self.srcText)
		print("Source Pronunciation: " + self.howToS)
		print("Dest LangCode: " + self.dest)
		print("Dest Language: " + self.destLang)
		print("Dest Text: " + self.destText)
		print("Dest Pronunciation: " + self.howToD)
	
	# Helper function for all codes TODO Use for wheel
	def langCodesDisplay(self):
		for i in self.langDict:
			print(i + ": " + self.langDict[i].title())

