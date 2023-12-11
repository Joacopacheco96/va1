import requests
import re
from bs4 import BeautifulSoup
import os

def CheckJobs(urltosearch):    
    oldjobs={}
    newjobs=[]
    f = open('./Jobs/WebScrapper/jobs.txt', 'r',encoding="utf-8")
    mylist = f.readlines()
    for line in mylist:
        oldArr=line.split('=>')
        if oldArr[1]:
            oldObj = {(oldArr[0])[:-1] : oldArr[1]}
            oldjobs = oldjobs | oldObj          
    try:
        reponse = requests.get(urltosearch)
        soup = BeautifulSoup(reponse.content, "html.parser")
        results = soup.find_all("div", class_=re.compile("base-card relative w-full hover:no-underline focus:no-underline base-card--link", re.I))
    except Exception as e:
        print(e)

    for job in results:
        thejob = job.find("h3").get_text().strip()
        company = job.find("h4").get_text().strip()
        url = job.find("a").get('href')
        keyJob = "{} on {}".format(thejob,company)
        newjob = "{} => {}\n".format(keyJob, url)
        if not (keyJob in oldjobs.keys()):
            with open("./Jobs/WebScrapper/jobs.txt","a",encoding="utf-8") as file:
                if newjob:
                    file.write(f"{newjob}")
                    newObj = "{} => {}".format(keyJob, url)
                    newjobs.append(newObj)
    if newjobs:
        print(f'total of new jobs {len(newjobs)}')
    else:
        print('no new jobs found')
    return newjobs

# lastweek = "https://www.linkedin.com/jobs/search/?keywords=Developer&location=Uruguay&locationId=&geoId=100867946&f_TPR=r604800&position=1&pageNum=0"
# print(CheckJobs(lastweek))