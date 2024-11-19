# import requests

# from pprint import pprint as print

# app_id = "9a092bee"
# app_key = "46d97afa5ae1702d6bcf028fcfa07fd3"
# language = "en-gb"

# word_id = "python"
# url = "https://od-api.oxforddictionaries.com/api/v2/enteries" + language + "/" + word_id.lower()

# response = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# print(response.status_code)
# # res = r.json()
# # print(res)




import requests
from pprint import pprint as print

app_id = "9a092bee"
app_key = "46d97afa5ae1702d6bcf028fcfa07fd3"
language = "en-gb"
word_id = "python"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

response = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(response.status_code)
print(response.text)