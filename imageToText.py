import pytesseract
from PIL import Image
import pyttsx3

#from gtts import gTTS


class ITT: 
    def __init__(self):
        super().__init__()

        

    def imageToText(self, name, lan):
        #opens image with pillow
        self.img = Image.open(name)
        #we might also be able to pass in the image might make it easier
        #gets the text of the image that was passed in
        
        self.text = pytesseract.image_to_string(self.img, lang = lan)
        #returns the text that was passed in
        
        return self.text

    def toSpeech(self):
        #pass in the text which you'd like to be said

        #with this lines of code the computer then says what the text passed in is
        engine = pyttsx3.init()
        #you can set the speed of the voice here
        engine.setProperty('rate', 125)
        engine.say(self.text)
        engine.runAndWait()
        engine.stop()

    def demo(self):
        #x = ITT()
        self.imageToText('image2.jpg', "eng")
        self.toSpeech()
        #self.toSpeech("What is up man")

x = ITT()
#x.demo()