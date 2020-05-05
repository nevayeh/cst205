import pytesseract
from PIL import Image
import pyttsx3


class ITT: 
    def __init__(self):
        super().__init__()

    # Parses text from an image given a source file and language
    def imageToText(self, name, lan):
      
        #opens image with pillow
        self.img = Image.open(name)
        
        #gets the text of the image that was passed in
        self.text = pytesseract.image_to_string(self.img, lang = lan)
        
        #returns the text that was passed in
        return self.text
