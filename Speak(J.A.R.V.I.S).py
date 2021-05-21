import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)
def say(str):
    engine.say(str)
    engine.runAndWait()
say("hello there how are you")
