import speech_recognition as sr

"""
This speech recognition, when ran, it records for as long
as it hears the speaking
"""

"""possibly add language as a parameter"""
def recordaudio():
    """this sets up the speech recognizer"""
    r = sr.Recognizer()
    """the mic is set to the default mic"""
    mic = sr.Microphone()
    """records the audio"""
    with mic as source:
        #this line is to make sure the mic has a stronger focus on the speaker
        r.adjust_for_ambient_noise(source)
        #this line records
        audio = r.listen(source)

    """returns audio"""
    #return audio
    """returns audio changes to text"""
    #return r.recognize_google(audio, """language of the recording""")

#This is for testing, prints out the audio in text
print(recordaudio())