from googlesearch.googlesearch import GoogleSearch,SearchResult
response = GoogleSearch().search("batman")
# result = SearchResult(response)
# print(result)
print(response)
# for result in response.results:
#     print("Title: " + result.title)
#     print("Content: " + result.getText())