from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
import math

products = Flask(__name__)

url = "mysql://root:Dnss7564$$@localhost/budgetfit"
products.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    
db_engine = create_engine(url)                                                                                      

cors = CORS(products)

products.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()

@products.route('/products', methods=['GET'])
def get_products():
    limit = request.args.get('limit', type=int)
    page_number = request.args.get('page', type=int)
    sort_order = request.args.get('sort', type=str)
    min_price = request.args.get('min', type=float)
    max_price = request.args.get('max', type=float)
    categories = request.args.get('categories', default='', type=str)
    search_term = request.args.get('search', default='', type=str)

    con = db_engine.engine.raw_connection()
    cursor = con.cursor()
    out_params = cursor.callproc('pagination', [sort_order, limit, page_number, min_price, max_price, categories, search_term])
    total_records = out_params[4]
    productsForm = []
    rs = cursor.fetchall()

    field_names = [d[0] for d in cursor.description]
    for row in rs:
        row_dict = {}
        for i, value in enumerate(row):
            row_dict[field_names[i]] = value

        brand_name, item_name, item_price, images_front_full_url = row_dict['brand_name'], row_dict['item_name'], row_dict['item_price'], row_dict['images_front_full_url']
        product = {'brand_name': brand_name,'item_name': item_name, 'item_price': item_price, 'images_front_full_url': images_front_full_url}
        productsForm.append(product)

    cursor.execute('SELECT @total_records')
    total_records = cursor.fetchone()[0]
    total_products = math.ceil(total_records / limit)

    cursor.close()
    con.commit()
    con.close()

    response = jsonify({'totalPages': total_products, 'data': productsForm})
    return response

if __name__ == '__main__':
    products.run(debug=True)