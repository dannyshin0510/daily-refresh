import requests
import json
import datetime

# https://github.com/M-Media-Group/Covid-19-API - all the info for API 

# Import the response as text, change  it into json, and query for Canada and Ontario

url = "https://covid-api.mmediagroup.fr/v1"
querystringCases = {"country":"Canada"}
responseCases = requests.request("GET", url+"/cases", params=querystringCases)
data=json.loads(responseCases.text)

def commaPlacer(num):
    return ("{:,}".format(num))

canCases=commaPlacer(data["All"]["confirmed"])
canDeaths=commaPlacer(data["All"]["deaths"])
ontCases=commaPlacer(data["Ontario"]["confirmed"])
ontDeaths=commaPlacer(data["Ontario"]["deaths"])

querystringCases = {"country":"Canada", "status":"Confirmed"}
responseHistory = requests.request("GET", url+"/history", params=querystringCases)
data=json.loads(responseHistory.text)

# Rate for Canada
nowDate=datetime.datetime.now().date()
canHistory=data["All"]["dates"]
print(canHistory)
print(canHistory[str(nowDate)])
print(canHistory[str(nowDate-datetime.timedelta(days=1))])
print(canHistory[str(nowDate-datetime.timedelta(days=2))])
todayDiffCan = canHistory[str(nowDate)] - canHistory[str(nowDate-datetime.timedelta(days=1))]
yesterdayDiffCan=canHistory[str(nowDate-datetime.timedelta(days=1))]-canHistory[str(nowDate-datetime.timedelta(days=2))]
canRate=""
if (yesterdayDiffCan>=todayDiffCan):
    canRate="increased"
else:
    canRate="decreased"

# Rate for Ontario
nowDate=datetime.datetime.now().date()
ontHistory=data["Ontario"]["dates"]
print(ontHistory)
print(ontHistory[str(nowDate)])
print(ontHistory[str(nowDate-datetime.timedelta(days=1))])
print(ontHistory[str(nowDate-datetime.timedelta(days=2))])
todayDiffOnt = ontHistory[str(nowDate)] - ontHistory[str(nowDate-datetime.timedelta(days=1))]
yesterdayDiffOnt=ontHistory[str(nowDate-datetime.timedelta(days=1))]-ontHistory[str(nowDate-datetime.timedelta(days=2))]
ontRate=""
if (yesterdayDiffOnt<=todayDiffOnt):
    ontRate="increased"
else:
    ontRate="decreased"
