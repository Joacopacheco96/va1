import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import datetime as dt
from time import time
from conversational import conversational
from generate_response import generate_response
from Jobs.checkJobs import check_background_jobs

#dbs
from db.trainedAnswers.hello import hello
from db.trainedAnswers.haveTrouble import haveTrouble
from db.trainedAnswers.thomaslisten import thomaslisten
# from db.trainedAnswers.credentials import credentials

###config parameters
name = 'tomas'
start_time = time()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
vozEng = voices[1].id
engine.setProperty('voice', vozEng)
engine.setProperty('rate', 135)
engine.setProperty('volume', 1)

def check_background():
    f = open('./Jobs/jobsPending.txt', 'r',encoding="utf-8")
    mytasks = f.readlines()
    return mytasks

def deleteBackgroundTasks():
    f = open('./Jobs/jobsPending.txt', 'w',encoding="utf-8")
    f.write('')


with open("contextconversation.txt","w") as initfile:
    initfile.write("as context in conversation: ")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def random_answer(x):
    speak(random.choice(list(x.items()))[1])

def listen(textToShow):
    r = sr.Recognizer()        
    rec=""
    with sr.Microphone() as source:
        try:
            print(f"{textToShow}")
            r.adjust_for_ambient_noise(source,duration=1)
            audio = r.listen(source)
            rec = r.recognize_google(audio, language='en-EN').lower()
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   
        except:pass
    return rec

def init_waiting():
    listenss = 1
    attemts = 0
    rec = ""
    while not rec:
        attemts+=1
        # consola = f"({attemts}) Waiting..."
        # print(consola)
        rec = listen('Waiting..')
    # while True:
        if attemts % 20 == 0:
            tasks_pending = check_background()
            if tasks_pending:
                speak("You have task pendings to read, Can I Show them now?")
                rec = listen('Waiting..')
                if 'yes' in rec or 'sure' in rec:
                  for task in tasks_pending:
                      tasksArr=task.split('***')
                      for eachtask in tasksArr:
                        records=eachtask.split('*JobTitle*')
                        print(records[0])
                        jobsRecords = records[1].split(',')
                        for job in jobsRecords:
                            jobObj=job.split('=>')
                            print(jobObj[0])
                  deleteBackgroundTasks()

        # r = sr.Recognizer()    
        # consola = f"({attemts}) Waiting..."
        # print(consola)
        # with sr.Microphone() as source:
        #     try:
        #         r.adjust_for_ambient_noise(source, duration=1)
        #         audio = r.listen(source)
        #         rec = ""
        #         rec = r.recognize_google(audio, language='es-ES').lower()
        #         rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        if name in rec:
            random_answer(hello)
            return orders()
        else:
            print(f"Activation by name")
            listenss+=1
            if listenss % 3 == 0:
                print(thomaslisten)
                random_answer(thomaslisten)
            # except:pass
        # attemts+=1

def orders():
    # while True:
    rec=''
    while not rec:
        rec = listen('Listen for order..')
        # r = sr.Recognizer()        
        # with sr.Microphone() as source:
        #     print(f"Esperando orden...")
        #     r.adjust_for_ambient_noise(source,duration=1)
        #     audio = r.listen(source)
        #     rec=" "
        #     rec = r.recognize_google(audio, language='en-EN').lower()
        #     rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")   
            
    print(f"just listen: {rec}")         
    responseGenerated = generate_response(rec)            
    speak(responseGenerated)
    print('resp generated: '+responseGenerated)
                  
init_waiting()