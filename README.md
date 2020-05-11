# Enuncreate

#### Created by

* Diana Danvers - iTransCode [Github](https://github.com/iTransCode)
* Neva Yeh - nevayeh [Github](https://github.com/nevayeh)
* Rodrigo Andrade - randrade8311 [Github](https://github.com/randrade8311)
* Syn Kae Ng - synkae [Github](https://github.com/synkae)

## Table of Contents
1. [Overview](#Overview)
2. [Product Spec](#Product-Spec)
3. [Libraries](#Libraries)
4. [Use](#Use)

## Overview

### Description

Our goal was to help people with dyslexia by creating a reading aid tool. The user can upload a source, such as a text input, an image, or audio file to the app which will convert the source to a desired format of either text or audio. Text is inputted in a simple textbox while image and audio files may be selected from a desired folder or recorded live! Choose the “Use Webcam” option to take a picture on your device’s camera or “Record Mp3” to make your own audio file. The GUI prompts the user to input a source file and defaults to parsing the source to English, however, a handy dictionary is available for the user to translate their source into a different language. Once the source data and destination format is selected, press “Go!” and watch the magic happen. Prying eyes can use the “Detail” button to see all the info our program is working with. Be sure to clear out your results when you’re done! Enjoy!


## Product Spec

### 1. User Stories (Required and Optional)

**Required Must-have Stories**
* Have input box for text
* Read text from image
* Use text to change to speech or show text
* Have translation to other languages
* Record audio to change to text or play it 

**Optional Nice-to-have Stories**

* Show webcam and take a screenshot
* Be able to upload images from folder
* Upload recording from folder
* Have translation to other languages

### 2. Options

* Typing Box
   * For user to input text
* Text-to-Text
   * Shows text with translation if chose
* Text-to-Speech
    * Will play the text inputed
* Speech-to-Speech
    * Will play recording that was either uploaded, or recorded
* Speech-to-Text
    * Changes the recording to text which displays it
* Translation
    * Will translate to other available languages


## Libraries

* googletrans (Google Translate)
* gTTS - (Google Text To Speech)
* pytesseract 
* playsound 
* SpeechRecognition 
* Pyaudio 
* OpenCV


## Use

* To use run: $ python3 main.py
* Demo Video: [Link](https://youtu.be/sPEC8WIBXzs)
