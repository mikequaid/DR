# install package pip install PyGithub
from github import Github
import requests

# remove the minus sign from the key , add this to your code just don't commit it
g = Github("b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e")

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))

# updating a txt file on git:
# Desired repo:
repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile) # prints to check it workd
response = requests.get(urlOfFile)
contentOfFile = response.text # contents of file is response.text
#print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)