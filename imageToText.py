import pytesseract
from PIL import Image
from gtts import gTTS
import os
import pyttsx3

class ITT:#passes in the name of the image
    def __init__(self, name):
        super().__init__()
        self.name=name

    def imageToText(self, lan):
        #this line is to show the program where pytesseract is located
        #it will be different depending on where you installed it
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        #opens image with pillow
        img = Image.open(self.name)
        #we might also be able to pass in the image might make it easier
        #gets the text of the image that was passed in
        text = pytesseract.image_to_string(img, lang = lan)
        #returns the text that was passed in
        print(text)
        return text

    def toSpeech(self, text):
        #pass in the text which you'd like to be said

        #with this lines of code the computer then says what the text passed in is
        engine = pyttsx3.init()
        #you can set the speed of the voice here
        engine.setProperty('rate', 125)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

n = ITT('image1.jpg')

n.toSpeech("What is up man")