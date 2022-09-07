import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime, date, timedelta
import wikipedia
from time import time

start_time = time()
engine = pyttsx3.init()

# name, key & config of Ai
name = 'libro'
key='AIzaSyBLE7mXeZcujKV6d_GBH2yR5re9S2NKRsU'
attemts = 0
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)
day_es = [line.rstrip('\n') for line in open('src/day/day_es.txt')]
day_en = [line.rstrip('\n') for line in open('src/day/day_en.txt')]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return now


def get_audio():
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f"({attemts}) Escuchando...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
                speak(f'yes Sir')
                print('yes Sir')
            else:
                print(f"please, try again, i don`t understand: {rec}")
                speak(f"please, try again, i don`t understand: {rec}")
        except:
            pass
    return {'text':rec, 'status':status}

while True:
    rec_json = get_audio()
    # rec= ""
    rec = rec_json['text']
    status = rec_json['status']

    if status:
        if 'estás ahí' in rec:
            speak('Of course')

        elif 'reproduce' in rec:        
                music = rec.replace('reproduce', '')
                speak(f'Sure, listen to {music}')
                pywhatkit.playonyt(music)


        elif 'que' in rec:
            if 'hora' in rec:
                hora = datetime.now().strftime('%I:%M %p')
                speak(f"Son las {hora}")

            elif 'dia es' in rec:                
                speak(f"Hoy es {getDay()}")

        elif 'habla de' in rec:
            order = rec.replace('habla de', '')
            speak(f"Ok, searching about {order}")
            wikipedia.set_lang("es")
            info = wikipedia.summary(order, 1)
            speak(info)

        # elif 'cuanto es' in rec:
        #     speak(sm.getResult(rec))

        elif 'descansa' in rec:
            speak("Okay Bye...")
            break

        else:
            print(f"Vuelve a intentarlo 2, no reconozco: {rec}")
        
        attemts = 0
    else:
        attemts += 1

print(f" Ai shut down, time running: { int(time() - start_time) } seconds ")