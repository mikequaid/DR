import requests
import json
from xlwt import * # For excel writing

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json() 


print (data) # print all data

#output cars  
for car in data["cars"]:
    print (car)

#save this to a file
filename = 'cars.json'
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# write to excel file
w = Workbook() # Create new workbook
ws = w.add_sheet('cars') # Add sheet called cars
row = 0; # @ row 0...
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1 # move onto row one by adding one
for car in data["cars"]:
    ws.write(row,0, car["reg"]) # extract the reg & store it in column 0
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1

w.save('cars.xls')