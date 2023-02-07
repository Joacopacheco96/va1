import os
import openai
import requests

openai.organization = "org-Om0k9Kku79ZnUhQdFl8AVNLP"
openai.api_key = "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"
urlmodels = 'https://api.openai.com/v1/models'
# models=openai.Model.list()
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="busca tesla en google",
#   max tokens for length response
  max_tokens=100,
#   temperature for creativity
  temperature=0,
)
print(response)