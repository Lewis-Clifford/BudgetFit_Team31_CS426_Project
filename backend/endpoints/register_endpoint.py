#endpoint to receive json data from register page

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

register = Flask(__name__)

cors = CORS(register)

register.config['CORS_HEADERS'] = 'Content-Type'

registerForm = []

@cross_origin()

@register.route('/register', methods=['GET'])

def registerGet():
    if len(registerForm) > 0:
        return jsonify(registerForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'


@register.route('/register', methods=['POST'])

def registerPost():
    
    try:
        registerForm = request.get_json()
        print(registerForm)
        return jsonify(registerForm)

    except:
        return 'Failed', 400

@register.route('/register', methods=['DELETE'])

def registerDelete():
    try:
        registerForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400

if __name__ == '__main__':
    register.run(debug=True)