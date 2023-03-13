from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy import text

products = Flask(__name__)

url = "mysql://root:Dnss7564$$@localhost/budgetfit"
products.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    
db_engine = create_engine(url)                                                                                      

cors = CORS(products)

products.config['CORS_HEADERS'] = 'Content-Type'



@cross_origin()

@products.route('/products', methods=['GET'])
def get_products():
    limit = request.args.get('limit', default=9, type=int)
    page_number = request.args.get('page', default=1, type=int)
    print('working')
    con = db_engine.engine.raw_connection()
    cursor = con.cursor()                                   #Create connection cursor
    cursor.callproc('pagination', [limit, page_number])    #This is the call to the stored procedure

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

    cursor.close()                                          #Close connection cursor
    con.commit()                                            #Commit changes to update database
    con.close()
    return jsonify(productsForm)

if __name__ == '__main__':
    products.run(debug=True)