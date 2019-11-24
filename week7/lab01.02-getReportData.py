# Creating a new workbook for requests

import requests
import json
#import xlwt
#import xlsxwriter
from xlwt import *


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
data = response.json()

listOfReports = []
#output to console
#print (data)
for item in data["items"]:
    #print(item["ResourceName"])
    listOfReports.append(item["ResourceName"])

# Make a new workbook:
w = Workbook()
ws = w.add_sheet('cars')
rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1 

# Iterate through all the reports:
for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    #print(url)
    # Go to URL and retrieve the report:
    response= requests.get(url)
    
    aReport= response.json()
    for row in aReport["rows"]:
        #print(row["ImbalancePrice"]) # print imbalance price
        ws.write(rowNumber,0,row["StartTime"])
        ws.write(rowNumber,1,row["EndTime"])
        ws.write(rowNumber,2,row["ImbalanceVolume"])
        ws.write(rowNumber,3,row["ImbalancePrice"])
        ws.write(rowNumber,4,row["ImbalanceCost"])
        rowNumber += 1
w.save('balance.xls')
filename = 'allreports.json'
# Writing JSON data
f =  open(filename, 'w')
json.dump(data, f, indent=4)