# Creates a new pdf from our carviewer html
import requests
import json

f = open("carviewer.html", "r") # Changed file path to suit my own
html = f.read()
#print (html)

apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html,'apiKey': apiKey}  # The data
response = requests.post(url, json=data) # a post
print (response.status_code)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb") # open a new file
newFile.write(response.content) # extract the content
print(response.status_code)
