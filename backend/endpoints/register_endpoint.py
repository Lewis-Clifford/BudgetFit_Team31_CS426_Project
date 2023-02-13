#endpoint to receive json data from register page

from flask import Flask, jsonify, request

register = Flask(__name__)

registerForm = []


@register.route('/register', methods=['GET'])

def registerGet():
    if len(registerForm) > 0:
        return jsonify(registerForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'


@register.route('/register', methods=['POST'])

def registerPost():
    
    try:
        registerForm.append(request.get_json)
        print(registerForm)
        return 'Success', 200

    except:
        return 'Failed', 400

@register.route('/register', methods=['DELETE'])

def registerDelete():
    try:
        registerForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400