import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime, date
from time import time
import os
from Integrations.conversational import conversational
from Integrations.bardApi import bardapichat
from Integrations.asanaApi import getTasksByProject
import requests
name = 'tomas'

#dbs
from db.trainedAnswers.hello import hello
from db.trainedAnswers.haveTrouble import haveTrouble
from db.trainedAnswers.thomaslisten import thomaslisten
    
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

start_time = time()
engine = pyttsx3.init()

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return now

def random_answer(x):
    return (random.choice(list(x.items()))[1])

def generate_response(rec):
    response = 'Sorry can not found a response to that'
    with open("memory/contextconversation.txt","a") as file:
        file.write((" user question: {} \n").format(rec))

    if 'estas ahi' in rec or 'are you there' in rec:
       response = random_answer(hello)

    elif 'reproduce' in rec or 'youtube' in rec:
        music = rec.replace('reproduce', '')
        music = rec.replace('youtube', '')
        response = (f'Sure, listen to {music}')              
        pywhatkit.playonyt(music)  

    elif 'what hour' in rec or 'what day' in rec:
        if 'hour' in rec :
            hora = datetime.now().strftime('%I:%M %p')
            response = (f"It is {hora}")
        elif 'day' in rec:                
            response = (f"It is {getDay()}")
            
    elif 'busca en google' in rec or 'search on google' in rec:
        order= rec.replace('busca en google','')
        order= rec.replace('search on google','')
        googlesearch = pywhatkit.search(f'{order}')
        response=(f'okay showing what i found on google about {order}')
    
    elif 'asana' in rec or 'check work items' in rec:
        response = getTasksByProject('1203537349306106')
        tasknames = []
        for item in response:
           tasknames.append(item['name']) if item['completed']==False else None
        response=(f'Following tasks are pendings: {str(tasknames)}')        
    
    elif 'gracias' in rec or 'go rest' in rec or 'thanks' in rec or 'thank you' in rec:
        response = "Okay call me whatever you want"
    else:
        speak("Okay")
        # resp = conversational(rec)
        resp = bardapichat(rec)
        if resp:
            print(resp)
            response = (f"{resp}")
        else:
            response = (f"{random_answer(haveTrouble)} {rec}")
            
    with open("memory/contextconversation.txt","a") as writefile:
        writefile.write((" response: {} \n").format(response))
    return response
    