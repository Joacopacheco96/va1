# import os
# import openai
import requests
import json

def conversational(query) :
    url = 'https://www.botlibre.com/rest/json/chat'
    headers = {'Content-Type': 'application/json'}
    data = {
        "application": "3752984275464243093",
        "instance": "165",
        "message": query
    }

    response = requests.post(url, json=data, headers=headers)
    response_text = response.text
    data_dict = json.loads(response_text)

    # Print or use the response text as needed
    return(data_dict)




# # openai.organization = 'org-Om0k9Kku79ZnUhQdFl8AVNLP'
# openai.api_key = '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'
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages = [{'role':'user','content':'2 + 2'}],
#     temperature=0
#     )
# print(response)


# from perplexity_api import PerplexityAPI, TimeoutException
# ppl = PerplexityAPI()

# query = "hello world in python"

# try:
#     print(ppl.query(query, follow_up=True))
# except TimeoutException:
#     print("Query timed out:", query)
