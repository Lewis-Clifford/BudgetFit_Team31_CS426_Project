#endpoint to receive json data from login page

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

exerciseOPT = Flask(__name__)

cors = CORS(exerciseOPT)

exerciseOPT.config['CORS_HEADERS'] = 'Content-Type'

exerciseOPTForm = []

@cross_origin()

@exerciseOPT.route('/exerciseOPT', methods=['GET'])

def loginGet():
    if len(exerciseOPTForm) > 0:
        return jsonify(exerciseOPTForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'


@exerciseOPT.route('/exerciseOPT', methods=['POST'])

def loginPost():
    
    try:
        loginForm = request.get_json()
        print(exerciseOPTForm)
        return jsonify(exerciseOPTForm)

    except:
        return 'Failed', 400

@exerciseOPT.route('/exerciseOPT', methods=['DELETE'])

def loginDelete():
    try:
        exerciseOPTForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400
    
if __name__ == '__main__':
    exerciseOPT.run(debug=True)