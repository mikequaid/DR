import json
 
data = {
  'name':'joe',
  'age':21,
  'student':'True'}
 
# print(data)

file = open("simple.json",'w')
# json.dump(data,file,indent=4)
jsonString = json.dumps(data)
print(jsonString)

import requests
 
url = 'https://gmit.ie'
response = requests.get(url)
print(response.status_code)
#print(response.status_text)
print(response.status_headers)

