
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import wikipedia

time = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            print("recognising....")
            query = r.recognize_google(audio, language="en-in")
        except:
            print("voice not recognised ...... please try again!")
        return query


def say(str):
    engine.say(str)
    engine.runAndWait()


def wishme():
    if time > 4 and time < 12:
        say("Good morning user!")
    elif time >= 12 and time < 17:
        say("Good Afternoon User!")
    elif time >= 17 and time < 24:
        say("Good evening ")


if __name__ == '__main__':
    wishme()
    say("I am JARVIS made by mr. Ansh Singhal how may I help you?")

    query = listen().lower()
    print(query)
    if "open youtube" == query:
        webbrowser.open("www.youtube.com")
    elif "flipkart" in query:
        webbrowser.open("www.flipkart.com")
    elif "instagram" in query:
        webbrowser.open("www.instagram.com")
    elif "facebook" in query:
        webbrowser.open("www.facebook.com")
    elif "open google" == query:
        webbrowser.open("www.google.com")
    elif "stackoverflow" in query:
        webbrowser.open("www.stackoverflow.com")
    elif "github" in query:
        webbrowser.open("www.github.com")
    elif "microsoft" in query:
        webbrowser.open("www.microsoft.com")
    elif "send" in query and "whatsapp" in query:
        try:
            number = "+91"
            say("enter the number I have to send message")
            number += listen()
            say("okay, now what should I send?")
            msg = listen()
            minute = int(datetime.datetime.now().strftime("%M"))+2

            pywhatkit.sendwhatmsg(number, msg, time, minute, 10)
        except Exception as e:
            print(e)
            say("I can't send that")
    elif "mail" in query or "email" in query:
        say("please enter sender's email address in terminal")
        sender = input()
        say("enter your password in terminal , it is needed, dont worry it is safe")
        password = input()
        say("please tell the subject of email")
        sub = listen()
        say("please speak the message")
        content = listen()
        say("please enter reciever's email in terminal")
        reciever = input()
        pywhatkit.send_mail(sender, password, sub, content, reciever)
    elif "wikipedia" in query:
        query = query.replace("on wikipedia","")
        query = query.replace("wikipedia","")
        query = query.replace("search","")
        say(f"searching {query} on wikipedia")
        results = wikipedia.summary(query,sentences = 2)
        say("here are the results")
        print(results)
        say(results)
    elif "search" in query and "youtube" in query :
        query = query.replace("search","")
        query = query.replace("on youtube","")
        query = query.replace("youtube","")
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
    elif "search" in query and "google" in query:
        query = query.replace("search","")
        query = query.replace("on google","")
        query = query.replace("google","")
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"

        webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")

    elif "open code" == query or "vs code" in query:
        path = "path of app"
	path = path.replace("\","/")
	webbrowser.open(path)
    else:
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"

        webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")
