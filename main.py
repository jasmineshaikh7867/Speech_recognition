import webbrowser
import os
import pyttsx3
# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import speech_recognition as sr
import datetime
import wikipedia
import random

name2 = ""

engine = pyttsx3.init('sapi5')
# sapi5 is used to take the inbuilt voice of windows

voices = engine.getProperty('voices')
# get the voices from windows
# print(voices)

engine.setProperty('voices', voices[1].id)


# this set the voice 0 or 1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("hello, I am tutie, how can I help you")


def takeCommand():
    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    # with takes care of all the exceptions and using the with statement makes the code compact and much more readable.
    # Thus, with statement helps avoiding bugs and leaks by ensuring that a resource is properly released when the code using the resource is completely executed.
    with sr.Microphone() as source:
        print("Listening....")
        speak(name2 + " Please Speak")
        r.pause_threshold = 0.6
        # pause_threshold is seconds of non speaking time before it execute
        audio = r.listen(source)
    try:
        print("Recognising..")
        query = r.recognize_google(audio)
        # query = r.recognize_google(audio, languge="en-in")
        print("user said :", query)
    except Exception as e:
        # print(e);
        speak("Please say that again " + name2)
        print("Please say that again...")
        return "None"
    return query


def authenticate():
    speak("please tell me passcode")
    tquery = takeCommand()
    if tquery == "hello open":
        return True
    speak("wrong passcode")
    print('wrong passcode')
    return False


def telltime():
    hour = (datetime.datetime.now().hour)
    min = (datetime.datetime.now().minute)
    s = "the time is " + str(hour) + " " + str(min)
    speak(s)


def telljoke():
    r = random.randint(0, 1)
    if r == 0:
        speak("This one is an acquired taste. what do you call a rose that wants to go to the moon. gulab ja moon")
    else:
        speak("why don't some couples go to gym?. . .Because some relations don't work out")


if __name__ == "__main__":
    wishMe()
    #while True:
        # flag = authenticate()
        # if flag:
          #   break

    speak("What's your sweet name?")
    name2 = takeCommand()
    if name2 == "None":
        n = takeCommand()
        name2 = n
        speak("Hello " + n)
    else:
        speak("Hello " + name2)

    while True:
        query = takeCommand().lower()
        # logic for excuting task
        if 'search' in query:
            speak("searching in wikipedia..")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'time' in query:
            telltime()
        elif 'joke' in query:
            telljoke()
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in query:
            codepath = "C:\\Users\\Dell\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'exit' in query:
            break
# install
# pip install pipwin
# pipwin install pyaudiom
# pip install pyttsx3
# pip install speech_recognition
# pip install wikipedia
