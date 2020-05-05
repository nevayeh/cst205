
"""
This speech recognition, when ran, it records for as long
as it hears the speaking
"""

from gtts import gTTS, lang
import playsound
import os
import pprint
import speech_recognition as sr

class STT:
	def __init__(self):
		super().__init__()

	#function to convert text to speech 
	def tts(self, text, l):
		self.tts = gTTS(text, lang=l)
		self.filename = "temp.mp3"
		self.tts.save(self.filename)
		playsound.playsound(self.filename)
		os.remove(self.filename)
		del(self.tts)

	#function that picks up audio and converts speech to text
	def stt(self):
		self.r = sr.Recognizer()
		with sr.Microphone() as source:
			self.audio = self.r.listen(source)
			self.stt_results = ""
		return self.stt_go()

	# Translate speach into text
	def stt_go(self):
		try:
			#this is to make sure the mic has a stronger focus on the speaker
			self.stt_results = self.r.recognize_google(self.audio)
			return(self.stt_results)
		except Exception as e:
			return(str(e))