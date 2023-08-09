import requests
import re
from bs4 import BeautifulSoup
import os

def CheckJobs (urltosearch):    
    oldjobs={}
    newjobs={}
    f = open('./WebScrapper/jobs.txt', 'r')
    mylist = f.readlines()
    for line in mylist:
        oldArr=line.split('=>')
        if oldArr[1]:
            oldObj = {oldArr[0] : oldArr[1]}
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
        keyJob = "{} -- {}".format(thejob,company)
        newjob = "{}=>{}\n".format(keyJob, url)
        # print(newjob)
        if keyJob not in oldjobs.keys():
            with open("./WebScrapper/jobs.txt","a",encoding="utf-8") as file:
                if newjob:
                    file.write(f"{newjob}")
                    newObj = {keyJob : url}
                    newjobs = newjobs | newObj
    if newjobs.keys():
        print(f'total of new jobs {len(newjobs.keys())}')
    else:
        print('no new jobs found')
    return newjobs

lastweek = "https://www.linkedin.com/jobs/search/?keywords=Developer&location=Uruguay&locationId=&geoId=100867946&f_TPR=r604800&position=1&pageNum=0"
print(CheckJobs(lastweek))