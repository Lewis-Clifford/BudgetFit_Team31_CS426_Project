from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {'name': 'eggs', 'price': 2.99}
    
]



@app.route('/items')

def getItems():
    return jsonify(items)

@app.route('/items', methods=['POST'])

def addItem():
    items.append(request.get_json())
    return '', 204

@app.route('/items', methods=['DELETE'])

def removeItem():

    try:
        items.remove(request.get_json())
        return 'Ok', 200

    except:
        return 'Failed', 400

if __name__ == '__main__':
    app.run(debug=True)