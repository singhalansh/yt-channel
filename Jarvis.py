import speech_recognition as sr
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

print(listen())
