import googletrans
from googletrans import Translator
from dict import langTrans

class transClass:

	def __init__(self):
		self.translator = Translator()	
		self.langDict = googletrans.LANGUAGES
		self.langTrans = langTrans()	
	
		self.src = ""
		self.srcLang = ""
		self.srcText = ""
		self.howToS = ""

		self.dest = ""
		self.destLang = ""
		self.destText = ""
		self.howToD = ""


		self.test = ""

	# Detect Language
	def detectLang(self, text):
		self.src = self.translator.detect(self.srcText).lang
		self.srcLang = self.langDict[self.src].title()
		self.srcText = text
		self.howToS = self.pronounce(self.srcText, self.src)

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
		return self.srcText

	# Translate: From [Detect Language] to [Choose Language]
	def transChoose(self, text, langDest):
		self.detectLang(text)
		if(len(langDest) == 3):
			self.dest = self.tesTOtra(langDest)
		else :
			self.dest = langDest
		
		self.translate()
		return self.srcText

	def translate(self):
		self.destLang = self.langDict[self.dest].title()
		self.destText = self.translator.translate(self.srcText, dest=self.dest).text
		self.howToD = self.pronounce(self.destText, self.dest)
	
	def tesTOtra(self, langDest):
		return self.langTrans.dict[langDest]

	def report(self):
		print(self.src)
		print(self.srcLang)
		print(self.srcText)
		print(self.howToS)
		print(self.dest)
		print(self.destLang)
		print(self.destText)
		print(self.howToD)
	
	def langCodes(self):
		for i in self.langDict:
			print(i + ": " + self.langDict[i].title())
