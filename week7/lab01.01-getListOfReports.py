# Writes all reports to a JSON file called allreports.json
# We print out the xml resource name from a for loop and store them in a list
import requests
import json


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
# Above URL was permanently moved to the one below:
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
data = response.json() # get the data

listOfReports = [] # for storing our list below
#output to console
#print (data)

# loop over our extracted data:
for item in data["items"]:
    #print(item["ResourceName"])
    listOfReports.append(item["ResourceName"]) # append in the item (Just the resouce names)

for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName # add on the report name
    print(url) # instead of merely printing...
    response= requests.get(url)
    aReport= response.json()

#other code
#save this to a file
filename = 'allreports.json' # ALL reports
# Writing JSON data
f =  open(filename, 'w')
json.dump(data, f, indent=4)