from flask import Flask, jsonify, request
from bson import ObjectId
from pymongo import MongoClient
from flask_cors import CORS
import os

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

for variable, value in os.environ.items():
    app.config[variable] = value

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

client = MongoClient(app.config['SB_DATABASE_HOST'], int(app.config['SB_DATABASE_PORT']))

db = client.flask_db
games = db.games


@app.get('/games')
def get_games():
    result = games.find()
    response_object = []
    for game in result:
        response_object.append({
            'gameId': str(game['_id']),
            'score_1': game['score_1'],
            'score_2': game['score_2']
        })
    return jsonify(response_object)


@app.post('/games')
def post_games():
    response_object = {}
    result = games.insert_one({
        'score_1': 0,
        'score_2': 0
    })
    response_object['gameId'] = str(result.inserted_id)
    return jsonify(response_object)


@app.get('/games/<gameId>')
def get_game(gameId):
    response_object = {}
    result = games.find_one({
        '_id': ObjectId(gameId)
    })
    response_object['gameId'] = str(result['_id'])
    response_object['score_1'] = result['score_1']
    response_object['score_2'] = result['score_2']
    return jsonify(response_object)


@app.put('/games/<gameId>')
def put_game(gameId):
    response_object = {}
    result = games.update_one({
        '_id': ObjectId(gameId)
    }, {
        '$set': {
            'score_1': request.json['score_1'],
            'score_2': request.json['score_2']
        }
    })
    response_object['gameId'] = str(result.upserted_id)
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
