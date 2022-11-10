# libraries
import numbers
import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime, date
import wikipedia
from time import time
from googlesearch import search
from StringCalculator import SolveMathProblem
from numbertoint import numbertoint as numbertoint

#dbs
from db.trainedAnswers.hello import hello
from db.trainedAnswers.haveTrouble import haveTrouble

#methods
# from db.methods import reproduce

start_time = time()
engine = pyttsx3.init()

name = 'tomas'

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
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
    attemts = 0
    while True:        
        r = sr.Recognizer()    
        with sr.Microphone() as source:
            print(f"({attemts}) Waiting...")
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
                    return init_waiting()
            except:pass
        attemts=attemts+1

def orders():
    while True:
        r = sr.Recognizer()        
        with sr.Microphone() as source:
            print(f"Esperando orden...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            rec=" "
            rec = r.recognize_google(audio, language='es-ES').lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   
            print(f"just listen: {rec}")         
        
            if 'estas ahi' in rec:
                random_answer(hello)
                return orders()

            elif 'reproduce' in rec:
                # reproduce()        
                music = rec.replace('reproduce', '')
                speak(f'Sure, listen to {music}')
                pywhatkit.playonyt(music)  
                return init_waiting()              

            elif 'que' in rec:
                if 'hora' in rec:
                    hora = datetime.now().strftime('%I:%M %p')
                    speak(f"Son las {hora}")
                    return init_waiting()
                elif 'dia es' in rec:                
                    speak(f"Hoy es {getDay()}")
                    return init_waiting()
            
            elif 'calculadora' in rec:
                speak('que operacion quieres hacer')
                listen()
                order = rec.replace('resultado', '')
                numbers=order.split('+').split('-').split('*').split('/')
                numberone=numbers[0].replace(' ','')
                numbertwo=numbers[1].replace(' ','')
                print(f'operacion es {order}')
                speak(f'operacion es {order}')                
                
            elif 'busca informacion de' in rec:
                order = rec.replace('busca informacion de', '')
                speak(f"Ok, searching about {order}")
                engine.setProperty('rate', 110)
                wikipedia.set_lang("es")
                info = wikipedia.summary(order, 1)
                speak(info)
                return init_waiting()
            
            elif 'busca en internet' in rec:
                order= rec.replace('busca en internet','')
                speak(f'okay there is the first results i found about {order}')
                results = search(f"{order}",num_results = 5)
                for result in results:
                    result = result.replace('https','').replace('http','').replace('://','').replace('www.','')
                    speak(result)
                    print(result)
                    
            elif 'busca en google' in rec:
                order= rec.replace('busca en google','')
                speak(f'okay this is what i found on google about {order}')
                pywhatkit.search(f'{order}')
                print(order)
            
            elif 'descansa' in rec:
                speak("Okay call me whatever you want")
                return init_waiting()
            
            elif 'finaliza procesos' in rec:
                speak("Okay good bye sir")
                break
            else:
                speak(f"{random_answer(haveTrouble)} {rec}")
                print(f"{rec}?")
                return orders()

init_waiting()          
print(f" Ai shut down, time running: { int(time() - start_time) } seconds ")