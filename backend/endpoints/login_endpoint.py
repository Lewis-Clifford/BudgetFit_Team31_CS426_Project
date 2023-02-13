#endpoint to receive json data from login page

from flask import Flask, jsonify, request

login = Flask(__name__)

loginForm = []


@login.route('/login', methods=['GET'])

def loginGet():
    if len(loginForm) > 0:
        return jsonify(loginForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'


@login.route('/login', methods=['POST'])

def loginPost():
    
    try:
        loginForm.append(request.get_json)
        print(loginForm)
        return 'Success', 200

    except:
        return 'Failed', 400

@login.route('/login', methods=['DELETE'])

def loginDelete():
    try:
        loginForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400