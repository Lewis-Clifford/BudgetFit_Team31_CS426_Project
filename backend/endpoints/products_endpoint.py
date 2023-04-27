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

        productsID, brand_name, item_category, item_name, nf_ingredient_statement, nf_calories, nf_calories_from_fat, nf_total_fat, nf_saturated_fat, nf_trans_fatty_acid, nf_polyunsaturated_fat, nf_monounsaturated_fat, nf_cholesterol, nf_sodium, nf_total_carbohydrate, nf_dietary_fiber, nf_sugars, nf_protein, nf_vitamin_a_dv, nf_vitamin_c_dv, nf_calcium_dv, nf_iron_dv, nf_potassium, nf_servings_per_container, nf_serving_size_qty, nf_serving_size_unit, nf_serving_weight_grams, metric_qty, metric_uom, images_front_full_url, item_price = row_dict['productsID'], row_dict['brand_name'], row_dict['item_category'], row_dict['item_name'], row_dict['nf_ingredient_statement'], row_dict['nf_calories'], row_dict['nf_calories_from_fat'], row_dict['nf_total_fat'], row_dict['nf_saturated_fat'], row_dict['nf_trans_fatty_acid'], row_dict['nf_polyunsaturated_fat'], row_dict['nf_monounsaturated_fat'], row_dict['nf_cholesterol'], row_dict['nf_sodium'], row_dict['nf_total_carbohydrate'], row_dict['nf_dietary_fiber'], row_dict['nf_sugars'], row_dict['nf_protein'], row_dict['nf_vitamin_a_dv'], row_dict['nf_vitamin_c_dv'], row_dict['nf_calcium_dv'], row_dict['nf_iron_dv'], row_dict['nf_potassium'], row_dict['nf_servings_per_container'], row_dict['nf_serving_size_qty'], row_dict['nf_serving_size_unit'], row_dict['nf_serving_weight_grams'], row_dict['metric_qty'], row_dict['metric_uom'], row_dict['images_front_full_url'], row_dict['item_price']
        product = {'productsID': productsID,
           'brand_name': brand_name,
           'item_category': item_category,
           'item_name': item_name,
           'nf_ingredient_statement': nf_ingredient_statement,
           'nf_calories': nf_calories,
           'nf_calories_from_fat': nf_calories_from_fat,
           'nf_total_fat': nf_total_fat,
           'nf_saturated_fat': nf_saturated_fat,
           'nf_trans_fatty_acid': nf_trans_fatty_acid,
           'nf_polyunsaturated_fat': nf_polyunsaturated_fat,
           'nf_monounsaturated_fat': nf_monounsaturated_fat,
           'nf_cholesterol': nf_cholesterol,
           'nf_sodium': nf_sodium,
           'nf_total_carbohydrate': nf_total_carbohydrate,
           'nf_dietary_fiber': nf_dietary_fiber,
           'nf_sugars': nf_sugars,
           'nf_protein': nf_protein,
           'nf_vitamin_a_dv': nf_vitamin_a_dv,
           'nf_vitamin_c_dv': nf_vitamin_c_dv,
           'nf_calcium_dv': nf_calcium_dv,
           'nf_iron_dv': nf_iron_dv,
           'nf_potassium': nf_potassium,
           'nf_servings_per_container': nf_servings_per_container,
           'nf_serving_size_qty': nf_serving_size_qty,
           'nf_serving_size_unit': nf_serving_size_unit,
           'nf_serving_weight_grams': nf_serving_weight_grams,
           'metric_qty': metric_qty,
           'metric_uom': metric_uom,
           'images_front_full_url': images_front_full_url,
           'item_price': item_price}
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