import pywhatkit     
if "mail" or "email" in query:
        say("please enter sender's email address in terminal")
        sender = input()
        say("enter your password in terminal , it is needed, dont worry it is safe")
        password= input()
        say("please tell the subject of email")
        sub = listen()
        say("please speak the message")
        content = listen()
        say("please enter reciever's email in terminal")
        reciever = input()
        pywhatkit.send_mail(sender,password, sub,content,reciever)
