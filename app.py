from flask import Flask, jsonify, abort, request

import random
import logging


app = Flask(__name__)

logger = logging.getLogger('werkzeug') #WSGI logger

@app.route('/mock', methods=['POST'])
def create_task():
    logger.info("received {}".format(request))
    logger.info("received generic json: {}".format(request.json))
    if not request.json or not 'payload' in request.json:
        abort(400)
    logger.info("received json: {}".format(request.json))
    i = random.randint(1, 100)
    if (i>80):
         abort(500)
    msg = {
        'payload': request.json['payload']
    }
    return jsonify({'message': msg}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
