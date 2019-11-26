# creating a RESTful API

from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='.')

#@app.route('/')
#def index():
#    return "Hello World"

@app.route('/books')
def getAll():
    return "in getAll"

@app.route('/books/<int:id>')
def findById(id): # take in the id
    return "in findById for id"+str(id)

if __name__ == '__main__' :
    app.run(debug= True)