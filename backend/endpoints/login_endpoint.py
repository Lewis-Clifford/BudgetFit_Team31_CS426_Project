#endpoint to receive json data from login page

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

login = Flask(__name__)

cors = CORS(login)

login.config['CORS_HEADERS'] = 'Content-Type'

loginForm = []

@cross_origin()

@login.route('/login', methods=['GET'])

def loginGet():
    if len(loginForm) > 0:
        return jsonify(loginForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'


@login.route('/login', methods=['POST'])

def loginPost():
    
    try:
        loginForm = request.get_json()
        print(loginForm)
        return jsonify(loginForm)

    except:
        return 'Failed', 400

@login.route('/login', methods=['DELETE'])

def loginDelete():
    try:
        loginForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400
    
if __name__ == '__main__':
    login.run(debug=True)