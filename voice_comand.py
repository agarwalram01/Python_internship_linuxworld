
import matplotlib.pyplot as plt 
import pyttsx3
import speech_recognition as sr
import webbrowser
import os


speaker = pyttsx3.init()
mic = sr.Recognizer()

speaker.say("Hello, I am Jarvis")
speaker.runAndWait()

with sr.Microphone() as source:
    print("Listening...")
    voice = mic.listen(source)
    try:
        text = mic.recognize_google(voice)
        print(text)
        command = text.lower()
        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com")  
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
        elif "open whatsapp" in command:
             webbrowser.open("https://www.whatsapp.com")
        elif "open instagram" in command:
            webbrowser.open("https://www.instagram.com")
        elif "open facebook" in command:
            webbrowser.open("https://www.facebook.com")
        elif "open twitter" in command:
            webbrowser.open("https://www.twitter.com")
        elif "open linkedin" in command:
            webbrowser.open("https://www.linkedin.com")
        elif "open github" in command:
            webbrowser.open("https://www.github.com")
        elif "open stackoverflow" in command:
            webbrowser.open("https://www.stackoverflow.com")
    except Exception as e:
        print("Error: " + str(e))
