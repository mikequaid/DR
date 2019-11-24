import requests
import json



#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
# Above URL was permanently moved to the one below:
url= "https://prodapi.metweb.ie/observations/newport-furnace/today"
response = requests.get(url)
data = response.json() # get the data

print(data)

for row in data:
    print(row["pressure"])

#filename = "weathReports.json"
#f =  open(filename, 'w')
#json.dump(data, f, indent=4)