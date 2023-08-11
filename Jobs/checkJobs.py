from  Jobs.WebScrapper.GetLinkedinJobs import CheckJobs

def check_background_jobs():
    jobs_checked = []
    print('checking jobs')

    search_for_jobs = CheckJobs("https://www.linkedin.com/jobs/search/?keywords=Developer&location=Uruguay&locationId=&geoId=100867946&f_TPR=r604800&position=1&pageNum=0")
    if search_for_jobs:
      linkedinJobs = f'***New Linkedin Jobs *JobTitle*{search_for_jobs} \n'
      jobs_checked.append(linkedinJobs)
    
    with open("./Jobs/jobsPending.txt","a",encoding="utf-8") as file:
        for job in jobs_checked:
          file.write(f"{job}")

# check_background_jobs()