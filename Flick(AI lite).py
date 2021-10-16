import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("INTIALIZING FLICK")
Sir = ("Mister DEEPANSHU")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# THIS FUNCTION WILL WISH ME AS PER THE TIME


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 4 and hour < 12):
        speak("GOOD MORNING" + Sir + "...")
    elif(hour >= 12 and hour < 16):
        speak("GOOD AFTERNOON " + Sir + "...")
    elif(hour >= 16 and hour < 20):
        speak("GOOD EVENING " + Sir + "...")
    # elif(hour >= 20 and hour <= 24 or hour >= 0 and hour < 4):
    #     speak("GOOD NIGHT DEEPANSHU SIR")
    else:
        speak("GOOD NIGHT " + Sir + "...")
        speak("NOW, TELL ME SIR HOW MAY I HELP YOU?")


# THIS FUNCTION WILL TAKE INPUT FROM ME THROUGH MICROPHONE
def takCommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try:
        print(Recognizing)
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said : {query}\n")

    except Exeption as e:
        print("Say that again please")
        query = None

    return query


# MAIN PROGRAM STARTS FROM HERE
speak("INITIALIZING FLICK...")
speak("FLICK IS AT YOUR SERVICE SIR...")
wishMe()
takCommond()
