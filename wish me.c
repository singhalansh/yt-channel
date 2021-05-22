import datetime
time = int(datetime.datetime.now().hour)
def wishme():
    if time>4 and time <12:
        say("Good morning user!")
    elif time>= 12 and time<17:
        say("Good Afternoon User!")
    elif time>=17 and time<24:
        say("Good evening user!")

if __name__ == '__main__':
    wishme()