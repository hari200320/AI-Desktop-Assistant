import webbrowser

import pyttsx3
import speech_recognition as sr


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in",)
            print(f"user said : {query}")
            return query
        except Exception as e:
            return "Sorry, I didn't hear that"

if __name__ == '__main__':
    print("Pycharm")
    say("Hello I am Nexus AI. Is there anything that I can do for you? ")
    print("listening.......")
    query = takecommand()
    site_name = query.replace("open", "").strip()
    # site_name=
    if site_name:
        say(f"Searching for {site_name}")
        search_url = f"https://www.google.com/search?q={site_name}"
        webbrowser.open(search_url)
    # say(query)