from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import URL

products = Flask(__name__)



#url = URL.create('mysql', username='cliff', password='PervertCamel21@@', host='localhost', database='db_budgetfit')
#products.config['SQLALCHEMY_DATABASE_URI'] = url
url = "mysql://Kaden:Dnss7564$$@localhost/db_budgetfit"
products.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    
db_engine = create_engine(url)                                                                                      

cors = CORS(products)

products.config['CORS_HEADERS'] = 'Content-Type'



@cross_origin()

@products.route('/products', methods=['GET'])
def get_products():
    params = request.get_json()
    with db_engine.connect() as con:  # Open connection
        cursor = con.cursor()
        rs = cursor.callproc('pagination', [params.values()[0], params.values()[1]])
        productsForm = []
        for row in rs:
            item_name, item_price, images_front_full_url = row
            product = {'item_name': item_name, 'item_price': item_price, 'images_front_full_url': images_front_full_url}
            productsForm.append(product)
        return jsonify(productsForm)

if __name__ == '__main__':
    products.run(debug=True)