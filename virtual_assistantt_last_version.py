from lib2to3.pgen2 import token
from timeit import repeat
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime, date
import wikipedia
from time import time
from googlesearch import search

start_time = time()
engine = pyttsx3.init()

# name, key & config of Ai
name = 'tomas'
key='AIzaSyBLE7mXeZcujKV6d_GBH2yR5re9S2NKRsU'
attemts = 0
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 1)
apikeyGoogle="AIzaSyCOwegRzgCV1NMvThM1g2-xRgzq-abIcVo"
engineID="https://cse.google.com/cse.js?cx=6702ec96f3ac64bec"

initial_response = "yes sir ?"
not_understand = "please, try again i dont understand"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return now

def get_audio():
    while True:        
        r = sr.Recognizer()    
        with sr.Microphone() as source:
            print(f"({attemts}) Escuchando...")
            try:
                engine.setProperty('rate', 130)
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                rec = " "
                rec = r.recognize_google(audio, language='es-ES').lower()
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                
                if name in rec:
                    speak(f'{initial_response}')
                    print(f'{initial_response}')
                    return orders()
                else:
                    print(f"Necesaria activacion por su nombre")
                    return get_audio()
            except:pass
def orders():
    while True:
        r = sr.Recognizer()        
        with sr.Microphone() as source:
            print(f"Esperando orden...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            rec=" "
            rec = r.recognize_google(audio, language='es-ES').lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            
        
            if 'estas ahi' in rec:
                speak('of course, what you need')
                return orders()

            elif 'reproduce' in rec:        
                    music = rec.replace('reproduce', '')
                    speak(f'Sure, listen to {music}')
                    pywhatkit.playonyt(music)  
                    return get_audio()              


            elif 'que' in rec:
                if 'hora' in rec:
                    hora = datetime.now().strftime('%I:%M %p')
                    speak(f"Son las {hora}")
                    return get_audio()
                elif 'dia es' in rec:                
                    speak(f"Hoy es {getDay()}")
                    return get_audio()
                
            elif 'busca informacion de' in rec:
                order = rec.replace('busca informacion de', '')
                speak(f"Ok, searching about {order}")
                engine.setProperty('rate', 110)
                wikipedia.set_lang("es")
                info = wikipedia.summary(order, 1)
                speak(info)
                return get_audio()
            
            elif 'busca en internet' in rec:
                order= rec.replace('busca en internet','')
                speak(f'okay there is the first results i found about {order}')
                results = search(f"{order}",num_results = 5)
                for result in results:
                    result = result.replace('http','').replace('https','').replace('://','').replace('www.','')
                    speak(result)
                    print(result)


            elif 'descansa' in rec:
                speak("Okay call me whatever you want")
                return get_audio()
            elif 'terminar procesos' in rec:
                speak("Okay good bye sir")
                break
            else:
                speak(f"{not_understand} {rec}")
                print(f"{not_understand} {rec}")
                return orders()
get_audio()          
print(f" Ai shut down, time running: { int(time() - start_time) } seconds ")