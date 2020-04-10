import requests
import json

# https://github.com/M-Media-Group/Covid-19-API - all the info for API 

# Import the response as text, change  it into json, and  query for Ontario

url = "https://covid-api.mmediagroup.fr/v1"

querystring = {"country":"Canada"}

response = requests.request("GET", url+"/cases", params=querystring)

data=json.loads(response.text)

# print(data["Ontario"]['confirmed'], data["All"])
print(data)
canCases=str(data["All"]["confirmed"])
canDeaths=str(data["All"]["deaths"])
torCases=str(data["Ontario"]["confirmed"])
torDeaths=str(data["Ontario"]["deaths"])
