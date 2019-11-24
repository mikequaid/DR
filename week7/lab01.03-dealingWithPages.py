# Pagination

import requests
import json
from xlwt import *


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View"
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"] # from JSON
#print (totalPages)
listOfReports = []

# Go through each page:
pageNumber=1
while pageNumber <= totalPages:
    # make a URL based on the page number:
    pageUrl = url + "&page="+ str(pageNumber)
    #print (pageUrl)
    # Get the data:
    data = requests.get(pageUrl).json() # return the data into JSON
    # Add this into the list of reports:
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1 # Increment page number

# output to console
# print (data)
# Output all names:
for reportName in listOfReports:
    print(reportName) 

filename = "allReports.json"
f =  open(filename, 'w')
json.dump(data, f, indent=4)