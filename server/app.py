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
scores = db.scores


@app.get('/scoreboard')
def get_scores():
    response_object = {'status': 'success'}
    result = scores.find_one({'_id': ObjectId(request.args.get('game_id'))})
    response_object['score_1'] = result['score_1']
    response_object['score_2'] = result['score_2']
    return jsonify(response_object)


@app.post('/scoreboard')
def post_scores():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    result = scores.insert_one({
        'score_1': post_data.get('score_1'),
        'score_2': post_data.get('score_2')
    })
    response_object['game_id'] = str(result.inserted_id)
    response_object['message'] = 'Score updated!'
    return jsonify(response_object)


@app.put('/scoreboard')
def put_scores():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    result = scores.update_one({
        '_id': ObjectId(post_data.get('game_id'))
    }, {
        '$set': {
            'score_1': post_data.get('score_1'),
            'score_2': post_data.get('score_2')
        }
    })
    response_object['message'] = 'Score updated!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
