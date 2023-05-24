import os
import datetime
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

load_dotenv()


RAPID_API_KEY = os.environ.get("RAPID_API_KEY")



def initialize_engine():
    engine = pyttsx3.init()
    return engine


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.strip().lower()
    except Exception as e:
        command = None

    return command


def ask_chatgpt(command):
    url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"

    payload = { "query": command }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        ans = response.json()
        return ans['response']
    else:
        print('Connection failed.')
        print(response.json())



if __name__ == "__main__":
    engine = initialize_engine()
    
    print("Listening...")
    while True:
        
        text = listen()
        
        
        if text and len(text) > 1:
            print('User said: {}'.format(text))
            print('Searching...')
            ans = ask_chatgpt(command=text)
            
            # print(ans)
            speak(engine, ans)   
            
        
            