import webbrowser
if __name__ == '__main__':
    wishme()
    say("I am JARVIS made by mr. Ansh Singhal how may I help you?")

    query = listen().lower()
    if "youtube" in query:
        webbrowser.open("www.youtube.com")
    elif "flipkart" in query:
        webbrowser.open("www.flipkart.com")
    elif "instagram" in query:
        webbrowser.open("www.instagram.com")
    elif "facebook" in query:
        webbrowser.open("www.facebook.com")
    