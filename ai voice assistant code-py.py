import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit as pwt
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
        print("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
        print("good afternoon")
    else:
        speak("good evening")
        print("good evening")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.adjust_for_ambient_noise(source)
        speak("now you can speak")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            print("recognizing.....")
            query = r.recognize_google(audio, language="en-us")
            print("user said:", query)
            return query
        except Exception as e:
            speak("Sorry, I didn't understand that.")
            return "none"

def open_app(app_name):
    if app_name == "power point":
        app_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk"
    elif app_name == "ms word":
        app_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"
    elif app_name == "ms excel":
        app_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk"
    else:
        return
    os.startfile(app_path)

wishme()
speak('i am siri, How can i help you')

while True:
    query = command().lower()
    print("give a second")
    speak("give a second")
    if "search in google" in query:
        q = "what do you want to search in google"
        print(q)
        speak(q)
        k = command()
        s = "searching in google"
        print(s)
        speak(s)
        pwt.search(k)
        exit(0)
    elif "youtube" in query:
        webbrowser.open("www.youtube.com")
    elif "open google" in query:
        webbrowser.open("www.google.com")
    elif "time" in query:
        thetime = datetime.datetime.now().strftime("%H:%M:%S")
        print(thetime)
        speak(f"\n\nthe time is {thetime}")
    elif "exit" in query:
        print("Thanks for giving me your time")
        speak("Thanks for giving me your time")
        speak("bye")
        exit(0)
    elif "i love you" in query:
        print("i love you 2 baby")
        speak("i love you 2 baby")
    elif "alone" in query:
        print("don't feel sad i am always with you")
        speak("don't feel sad i am always with you")
    elif "twitter" in query:
        print("opening twitter")
        speak("opening twitter")
        webbrowser.open("www.twitter.com")
        exit(0)
    elif "music" in query:
        t = "playing song"
        print(t)
        speak(t)
        c = "F:\\videos\\song.mp3"
        os.startfile(c)
        elif "music in online" in query:
        print("playing song in youtube")
        speak("playing song in youtube")
        webbrowser.open("https://www.youtube.com/watch?v=YE6LE9cwhXc")
        exit(0)
    elif "instagram" in query:
        print("opening instagram")
        speak("opening instagram")
        webbrowser.open("www.instagram.com")
        exit(0)
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    elif "power point" in query or "ms word" in query or "ms excel" in query:
        open_app(query.lower())
    else:
        o = "sorry for inconvenience this function is not yet developed"
        print(o)
        speak(o)
        exit(0)