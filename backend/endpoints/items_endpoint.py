from flask import Flask, jsonify, request
from models import Item, ItemSchema

app = Flask(__name__)

items = [
    Item("Bread", 3.99, "Smith's", "Starch"),
    Item("Eggs", 6.99, "WalMart", "Protein")
]


@app.route('/items') #router, defaults to GET method

def getItems():
    
    schema = ItemSchema(many=True) #defines schema object
    itemList = schema.dump(items) #serializes list of items

    return jsonify(itemList)

@app.route('/items', methods=['POST']) #POST endpoint

def addItem():
    newItem = ItemSchema().load(request.get_json()) #deserializes json data
    items.append(newItem) #adds item to list
    return 'Posted', 204

@app.route('/items', methods=['DELETE'])

def removeItem():

    rItem = ItemSchema().load(request.get_json())

    try:
        items.clear()
        return 'Success', 200

    except:
        return 'Failed', 400

if __name__ == '__main__':
    app.run(debug=True)