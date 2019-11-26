# creating a RESTful API

from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

# Create the table:
books=[
    { "id":1, "Title":"Harry Potter", "Author":"JK", "Price":1000},
    { "id":2, "Title":"The Quiet American", "Author":"Greene", "Price":800},
    { "id":3, "Title":"Something Steamy", "Author":" Jackie Collins", "Price":1100}
]

nextId=4 # This keeps track of the id (global)

#app = Flask(__name__)
# simple server:
#@app.route('/')
#def index():
#    return "Hello"

# create 5 CRUD functions in the interface:

#No 1 function getAll curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    return jsonify(books) # works perfectly !

#No 2 function findById curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id): # take in the id
    foundBooks = list(filter(lambda t: t['id'] == id, books))
    if len(foundBooks) == 0:
        return jsonify ({}) , 204 # works perfectly
    
    return jsonify(foundBooks[0])

    
# No 3 function create curl -X POST "http://127.0.0.1:5000/books/1234"
# internal server error (500) means error in your code
# curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST']) # to Create 
def create():
    global nextId # need to declare as global
    if not request.json:
        abort(400) # returns error

    book = {
    "id": nextId,
    "Title": request.json['Title'],
    "Author": request.json['Author'],
    "Price": request.json['Price'],
    }
    nextId += 1
    books.append(book)
    return jsonify(book)
 #   return str(nextId) # should return "5"
 

# No 4 function update curl -X PUT "http://127.0.0.1:5000/books/1234"
# update/change the books
# curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"Gary Potter\",\"Author\":\"someone\",\"Price\":2357}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
# Find the item that needs to be updated (ie.book)
def update(id): 
    foundBooks = list(filter(lambda t: t['id']== id, books))
    if (len(foundBooks) == 0): # if no book found
        abort(404) # abort
    foundBook = foundBooks[0] # one object found
    if not request.json:
        abort(400)

    reqJson = request.json 
    # Error checking,outputs message if incorrect input
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundBook['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundBook['Price'] = reqJson['Price']
    
    return jsonify(foundBook)   

    return "in update for ID id "+str(id)
        
#No 5 function delete curl -X DELETE "http://127.0.0.1:5000/books/1234"
@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t['id']== id, books))
    if (len(foundBooks) == 0):
        abort(404)
    books.remove(foundBooks[0])
    return jsonify({"deleted":True})

if __name__ == '__main__' :
    app.run(debug= True)