import pywhatkit

if "send" and "whatsapp" in query:
        try:
            number = "+91"
            say("enter the number I have to send message")
            number += listen()
            say("okay, now what should I send?")
            msg = listen()
            minute = int(datetime.datetime.now().strftime("%M"))+1

            pywhatkit.sendwhatmsg(number,msg,time,minute,10)
        except Exception as e:
            print(e)
            say("I can't send that")