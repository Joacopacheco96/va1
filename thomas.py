import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime, date
from time import time
import os
import openai
import requests

#dbs
from db.trainedAnswers.hello import hello
from db.trainedAnswers.haveTrouble import haveTrouble
from db.trainedAnswers.listen import listen

start_time = time()
engine = pyttsx3.init()

name = 'tomas'
openai.organization = "org-Om0k9Kku79ZnUhQdFl8AVNLP"
openai.api_key = "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"
voices = engine.getProperty('voices')
vozEsp = voices[3].id
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
                        random_answer(listen)
                        print('need something sir?')
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
            rec = r.recognize_google(audio, language='es-ES').lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   
            print(f"just listen: {rec}")         
        
            if 'estas ahi' in rec:
                random_answer(hello)
                return orders()

            elif 'reproduce' in rec or 'youtube' in rec:
                music = rec.replace('reproduce', '')
                music = rec.replace('youtube', '')
                speak(f'Sure, listen to {music}')
                pywhatkit.playonyt(music)  
                return init_waiting()              

            elif 'que hora es' in rec or 'que dia es' in rec:
                if 'hora' in rec:
                    hora = datetime.now().strftime('%I:%M %p')
                    speak(f"Son las {hora}")
                    return init_waiting()
                elif 'dia' in rec:                
                    speak(f"Hoy es {getDay()}")
                    return init_waiting()
                    
            elif 'busca en google' in rec:
                order= rec.replace('busca en google','')
                speak(f'okay this is what i found on google about {order}')
                pywhatkit.search(f'{order}')
                print(order)
            
            elif 'gracias' in rec or 'go rest' in rec or 'thanks' in rec or 'descanza' in rec:
                speak("Okay call me whatever you want")
                return init_waiting()

            else:
                speak("Okay let me see what i found")
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt= rec,
                max_tokens=256,
                temperature=0.5,
                )
                resp =response.choices[0].text 
                if resp:
                    print(resp)
                    speak(f"{resp}")
                    speak("Anything else sir?")
                else:
                    speak(f"{random_answer(haveTrouble)} {rec}")
                    speak("Anything else sir?")
                    return orders()
                  
init_waiting()          
print(f" Ai shut down, time running: { int(time() - start_time) } seconds ")