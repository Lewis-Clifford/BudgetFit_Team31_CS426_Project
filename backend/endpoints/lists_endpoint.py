#Author: Cliff Lewis
#Purpose: Endpoint to process requests pertaining to lists and the 'shop' page

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

lists = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
lists.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(lists)

lists.config['CORS_HEADERS'] = 'Content-Type'



@cross_origin()

@lists.route('/lists', methods=['POST'])

def listsPost():

    listsForm = []
    con = db_engine.engine.raw_connection()
    listsForm = request.get_json()                     #Open database connection
    
    '''
    Expected argument order to store records: (userID, productsID, listName, priority, description, quantity)
    '''

    try:
        
        for i in range(len(listsForm)):
            cursor = con.cursor()                                                   #Create connection cursor
            cursor.callproc('insertToUserList', listsForm[i].values())       #This is the call to the stored procedure
            cursor.close()                                                          #Close connection cursor
            con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(listsForm)
    
@lists.route('/lists', methods=['GET'])

def listReturn():

    userID = request.args.get('userID', type=int)
    listname = request.args.get('listName', type=str)
    


    listsForm = []
    con = db_engine.engine.raw_connection()
                        #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getUserList', [userID, listname])                      #This is the call to the stored procedure
        rs = cursor.fetchall()
        
        
        field_names = [d[0] for d in cursor.description]
        for row in rs:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[field_names[i]] = value

            brand_name, item_name, item_price, images_front_full_url, productsID, item_category, nf_ingredient_statement,\
            nf_calories, nf_calories_from_fat, nf_total_fat, nf_saturated_fat, nf_trans_fatty_acid, nf_polyunsaturated_fat, nf_monounsaturated_fat, nf_cholesterol,\
            nf_sodium, nf_total_carbohydrate, nf_dietary_fiber, nf_sugars, nf_protein, nf_vitamin_a_dv, nf_vitamin_c_dv, nf_calcium_dv, nf_iron_dv,\
            nf_potassium, nf_servings_per_container, nf_serving_size_qty, nf_serving_size_unit, nf_serving_weight_grams, metric_qty,\
            metric_uom, priority, description, listName, quantity = row_dict['brand_name'], row_dict['item_name'], row_dict['item_price'], \
            row_dict['images_front_full_url'], row_dict['productsID'], row_dict['item_category'], row_dict['nf_ingredient_statement'], \
            row_dict['nf_calories'], row_dict['nf_calories_from_fat'], row_dict['nf_total_fat'], row_dict['nf_saturated_fat'], \
            row_dict['nf_trans_fatty_acid'], row_dict['nf_polyunsaturated_fat'], row_dict['nf_monounsaturated_fat'], row_dict['nf_cholesterol'], row_dict['nf_sodium'],\
            row_dict['nf_total_carbohydrate'], row_dict['nf_dietary_fiber'], row_dict['nf_sugars'], row_dict['nf_protein'], row_dict['nf_vitamin_a_dv'],\
            row_dict['nf_vitamin_c_dv'], row_dict['nf_calcium_dv'], row_dict['nf_iron_dv'], row_dict['nf_potassium'], row_dict['nf_servings_per_container'],\
            row_dict['nf_serving_size_qty'], row_dict['nf_serving_size_unit'], row_dict['nf_serving_weight_grams'], row_dict['metric_qty'], row_dict['metric_uom'],\
            row_dict['priority'], row_dict['description'], row_dict['listName'], row_dict['quantity']
            
            product = {'brand_name': brand_name,'item_name': item_name, 'item_price': item_price, 'images_front_full_url': images_front_full_url,\
                       'productsID': productsID, 'item_category': item_category, 'nf_ingredient_statement': nf_ingredient_statement, 'nf_calories': nf_calories,\
                        'nf_calories_from_fat': nf_calories_from_fat, 'nf_total_fat': nf_total_fat, 'nf_saturated_fat': nf_saturated_fat,\
                        'nf_trans_fatty_acid': nf_trans_fatty_acid, 'nf_polyunsaturated_fat': nf_polyunsaturated_fat, 'nf_monounsaturated_fat': nf_monounsaturated_fat,\
                        'nf_cholesterol': nf_cholesterol, 'nf_sodium': nf_sodium, 'nf_total_carbohydrate': nf_total_carbohydrate, 'nf_dietary_fiber': nf_dietary_fiber,\
                        'nf_sugars': nf_sugars, 'nf_protein': nf_protein, 'nf_vitamin_a_dv': nf_vitamin_a_dv, 'nf_vitamin_c_dv': nf_vitamin_c_dv,\
                        'nf_calcium_dv': nf_calcium_dv, 'nf_iron_dv': nf_iron_dv, 'nf_potassium': nf_potassium, 'nf_servings_per_container': nf_servings_per_container,\
                        'nf_serving_size_qty': nf_serving_size_qty, 'nf_serving_size_unit': nf_serving_size_unit, 'nf_serving_weight_grams': nf_serving_weight_grams,\
                        'metric_qty': metric_qty, 'metric_uom': metric_uom, 'priority': priority, 'description': description, 'listName': listName,\
                        'quantity': quantity}
            
            listsForm.append(product)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()         
        print(jsonify(listsForm))                                       #Close database connection
        return jsonify(listsForm) 
    
@lists.route('/newList', methods=['POST'])
def createList():
    
    listsForm = []
    con = db_engine.engine.raw_connection()
    listsForm = request.get_json()                     #Open database connection
    print(listsForm)
    

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('createList', listsForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(listsForm)

@lists.route('/newList', methods=['GET'])
def getListNames():
    
    userID = request.args.get('userID', type=int)
    


    listsForm = []
    con = db_engine.engine.raw_connection()          #Open database connection
    print(listsForm)
    

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getListNames', [userID])       #This is the call to the stored procedure

        rs = cursor.fetchall()
        
        
        field_names = [d[0] for d in cursor.description]
        for row in rs:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[field_names[i]] = value
        
            listName, priority, description = row_dict['listName'], row_dict['priority'], row_dict['description']

            list = {'listName': listName, 'priority': priority, 'description': description}
            listsForm.append(list)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(listsForm)

if __name__ == '__main__':
    lists.run(debug=True)