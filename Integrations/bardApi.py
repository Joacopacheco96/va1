import google.generativeai as genai
from Integrations.credentials import bardApiKey

def bardapichat(inputString):    
    genai.configure(api_key=bardApiKey)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(inputString)
    return response.text