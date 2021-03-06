# flask_web/app.py

from flask import Flask, jsonify, request
import random
import os

app = Flask(__name__)
app.config['SONIFY_PRETTYPRINT_REGULAR'] = False


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(
        {
            'data': {
                'name': os.getenv('HOSTNAME'),
                'device': os.getenv('DEVICE'),
                'temp': random.randrange(-10, 21, 1),
            }
        }
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
