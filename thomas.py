import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime, date
from time import time
import os
from conversational import conversational
import requests
from generate_response import generate_response

#dbs
from db.trainedAnswers.hello import hello
from db.trainedAnswers.haveTrouble import haveTrouble
from db.trainedAnswers.thomaslisten import thomaslisten
# from db.trainedAnswers.credentials import credentials

with open("contextconversation.txt","w") as initfile:
    initfile.write("as context in conversation: ")

start_time = time()
engine = pyttsx3.init()

name = 'tomas'

voices = engine.getProperty('voices')
vozEng = voices[1].id
engine.setProperty('voice', vozEng)
engine.setProperty('rate', 135)
engine.setProperty('volume', 1)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return now

def listen():
        r = sr.Recognizer()        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            rec=""
            rec = r.recognize_google(audio, language='es-ES').lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   

def random_answer(x):
    speak(random.choice(list(x.items()))[1])

def init_waiting():
    listenss = 1
    attemts = 0
    while True:        
        r = sr.Recognizer()    
        with sr.Microphone() as source:
            consola = f"({attemts}) Waiting..."
            print(consola)
            try:
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                rec = ""
                rec = r.recognize_google(audio, language='es-ES').lower()
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                
                if name in rec:
                    random_answer(hello)
                    return orders()
                else:
                    print(f"Activation by name")
                    listenss+=1
                    if listenss % 3 == 0:
                        print('need something sir?')
                        random_answer(thomaslisten)
            except:pass
        attemts+=1

def orders():
    while True:
        r = sr.Recognizer()        
        with sr.Microphone() as source:
            print(f"Esperando orden...")
            r.adjust_for_ambient_noise(source,duration=1)
            audio = r.listen(source)
            rec=" "
            rec = r.recognize_google(audio, language='en-EN').lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   
            
            print(f"just listen: {rec}")         
            responseGenerated = generate_response(rec)            
            speak(responseGenerated)
            print('resp generated: '+responseGenerated)
                  
init_waiting()