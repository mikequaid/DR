from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

acts=[
    { "id": 1, "name":"Joe", "totalVotes":4}, 
    { "id": 2, "name":"Andrew", "totalVotes":23}, 
    { "id": 3, "name":"Gareth", "totalVotes":20},
]


nextId=3

# curl "http://127.0.0.1:5000/acts"
@app.route('/acts')
def getAll():
    return jsonify(acts)

# curl "http://127.0.0.1:5000/acts/2"
@app.route('/acts/<int:id>')
def findById(id):
    foundActs = list(filter(lambda t: t['id'] == id, acts))
    if len(foundActs) == 0:
        return jsonify ({}) , 204

    return jsonify(foundActs[0])

# curl  -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"4\",\"name\":\"Elena\",\"totalVotes\":1}" http://127.0.0.1:5000/acts
@app.route('/acts', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    act = {
        "id": nextId,
        "name": request.json['name'],
        "totalVotes":0 # as default before voting 
    }
    nextId += 1
    acts.append(act)
    return jsonify(act)

# curl -X DELETE "http://127.0.0.1:5000/acts/1"
@app.route('/acts/<int:id>' , methods=['DELETE'])
def delete(id):
    foundActs = list(filter(lambda t: t['id']== id, acts))
    if (len(foundActs) == 0):
        abort(404)
    acts.remove(foundActs[0])
    return jsonify({"deleted":True})

# curl  -i -H "Content-Type:application/json" -X POST -d "{\"votes\":122}" http://127.0.0.1:5000/votes/1
@app.route('/votes/<int:actId>', methods = ['POST'])
def addVote(actId):
    # get the acts list:
    foundActs=list(filter(lambda t : t['id']==actId, acts))
    if len(foundActs)== 0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'votes' in request.json or type(request.json['votes']) is not int:
        abort(401)
    newVotes = request.json['votes']

    foundActs[0]['totalVotes'] += newVotes


    return jsonify(foundActs[0])

# curl "http://127.0.0.1:5000/votes/leaderboard"
@app.route('/votes/leaderboard')
def getleaderBoard():
#ut.sort(key=lambda x: x.count, reverse=True) # sort leaserboard by largest to smallest
    acts.sort(key=lambda x: x['totalVotes'], reverse=True) 

    return jsonify(acts)


if __name__ == '__main__' :
    app.run(debug= True)