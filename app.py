from flask import Flask, jsonify, abort, request

import random


app = Flask(__name__)

@app.route('/mock', methods=['POST'])
def create_task():
    if not request.json or not 'payload' in request.json:
        abort(400)
    i = random.randint(1, 100)
    if (i>80):
         abort(400)
    msg = {
        'payload': request.json['payload']
    }
    return jsonify({'message': msg}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
