import google.generativeai as palm
from Integrations.credentials import bardApiKey

def bardapichat(inputString):    
    palm.configure(api_key=bardApiKey)
    response = palm.chat(messages='Hello')
    response = response.reply(inputString)
    return response.last