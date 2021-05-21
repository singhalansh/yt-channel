import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            print("recognising....")
            query = r.recognize_google(audio,language="en-in")
        except:
            print("voice not recognised ...... please try again!")
        return query

def say(str):
    engine.say(str)
    engine.runAndWait()
say("hello there how are you")