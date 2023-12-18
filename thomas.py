import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import datetime as dt
from time import time
from generate_response import generate_response
from Jobs.checkJobs import check_background_jobs
from Thomasfunctions import open_url
import webbrowser
import validators
#dbs
from db.trainedAnswers.hello import hello
from db.trainedAnswers.haveTrouble import haveTrouble
from db.trainedAnswers.thomaslisten import thomaslisten

###config parameters
name = ['thomas','thom','tomas','tom']
start_time = time()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
vozEng = voices[1].id
engine.setProperty('voice', vozEng)
engine.setProperty('rate', 135)
engine.setProperty('volume', 1)

def check_background():
    check_background_jobs() 
    f = open('./Jobs/jobsPending.txt', 'r',encoding="utf-8")
    mytasks = f.readlines()
    if mytasks:
            speak("You have task pendings to read, Can I Show them now?")
            rec = listen('Backgrond check response..')
            if 'yes' in rec or 'sure' in rec:
                for eachtask in mytasks:
                    records=eachtask.split('*JobTitle*')
                speak(records[0])
                jobsRecords = (records[1]).split(',')
                for job in jobsRecords:
                    jobObj=job.split(' => ')
                    speak(jobObj[0])
                    try:  
                        webbrowser.open(jobObj[1].replace("'",""))
                    except:pass
                deleteBackgroundTasks()
            else:
                speak('Okay i will remind you')

def deleteBackgroundTasks():
    f = open('./Jobs/jobsPending.txt', 'w',encoding="utf-8")
    f.write('')
    speak('Okay Now we are up to date by the moment')


with open("memory/contextconversation.txt","w") as initfile:
    initfile.write("as context in conversation: ")

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def random_answer(x):
    speak(random.choice(list(x)))

def listen(textToShow):
    listen=0
    r = sr.Recognizer()        
    rec=""
    while (len(rec) == 0 and listen < 20):
        listen+=1
        print(f'{listen} {textToShow}')
        with sr.Microphone() as source:
            try:
                r.adjust_for_ambient_noise(source,duration=1)
                audio = r.listen(source)
                rec = r.recognize_google(audio, language='en-EN').lower()
                rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   
            except:pass
    return rec

def init_waiting():  
        check_background()
        
        rec = ""
        rec = listen('Init Waiting..')                    
        if rec in name:
            random_answer(hello)
            return orders()
        else:
            print(f"Activation by name")
            random_answer(thomaslisten)
            return init_waiting()

def orders():
    rec=''
    rec = listen('Listen for order..')            
    print(f"just listen: {rec}")         
    responseGenerated = generate_response(rec)            
    speak(responseGenerated)
    print('resp generated: '+responseGenerated)
    speak('Need anything else?')
    rec = listen('Need anything else?..')            
    if 'yes' in rec or 'sure' in rec:
      return orders()
    else:
        speak('Okay just call me by my name?')
        return init_waiting()
                  
init_waiting()