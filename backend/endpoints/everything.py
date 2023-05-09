from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine, URL
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, jwt_required
import hashlib
import math
from twilio.rest import Client

# Author: Kaden Nesch
# This page consists of all of the endpoints used during the final demo. 
# I will only comment endpoints that have not already been commented by Cliff.

account_sid = 'AC81f423bcf59f27ca20c14cbd6f94301e'
auth_token = 'c738d9d80933af32f45777423e59b32e'
client = Client(account_sid, auth_token)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'newsecret'

url = URL.create('mysql', username='root', password='Dnss7564$$', host='localhost', database='budgetfit')
app.config['SQLALCHEMY_DATABASE_URI'] = url
db_engine = create_engine(url)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

registerForm = []

jwt = JWTManager(app)
blacklist = set()

@cross_origin()


# Endpoint to deal with logging out, destroying the token once a user logs out must use protected routes.
@app.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    
    jti = get_jwt()['jti']
    blacklist.add(jti)
    return jsonify({'message': 'Successfully logged out'}), 200




@app.route('/login', methods=['POST'])
def login():
    login_form = request.json
    if not login_form or not login_form.get('username') or not login_form.get('password'):
        return jsonify({'msg': 'Invalid login credentials'}), 405

    username = login_form['username']
    password = login_form['password']
    password1 = hashlib.sha256(password.encode('utf-8')).hexdigest()

    conn = db_engine.engine.raw_connection()
    cursor = conn.cursor()
    cursor.callproc('userAuth', [username])
    user = cursor.fetchone()

    if user is None:
        cursor.close()
        conn.close()
        return jsonify({'message': 'User not found'}), 401
    
    if user[1] != username:
        cursor.close()
        conn.close()
        return jsonify({'message': 'Incorrect username or password'}), 401
    
    storedPassword = user[0].decode('utf-8')


    if storedPassword != password1:
        cursor.close()
        conn.close()
        return jsonify({'msg': 'Invalid login credentials'}), 401

    access_token = create_access_token(identity=user[2], expires_delta=False)

    while cursor.nextset():
        pass

    cursor.close()
    conn.close()

    return jsonify({'access_token': access_token, 'userID': user[2]}), 200



@app.route('/register', methods=['GET'])

def registerGet():
    if len(registerForm) > 0:
        return jsonify(registerForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'





@app.route('/register', methods=['POST'])
def registerPost():
    con = db_engine.engine.raw_connection()
    registerForm = request.get_json()
    
    try:
        cursor = con.cursor()
        cursor.callproc('createUser2', registerForm.values())
        cursor.close()
        con.commit()
        
    except Exception as e:
        error_msg = str(e)
        if 'Duplicate entry' in error_msg:
            error_msg = 'Username or Email already taken'
        return jsonify({'error': error_msg}), 500
        
    finally:
        con.close()
        
    return jsonify(registerForm)
        
    
                                               #Close database connection

@app.route('/register', methods=['DELETE'])

def registerDelete():
    try:
        registerForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400




# Endpoint for obtaining all of the products stored in the database.
# Endpoint will also take in arguments for the mastersearch to work properly.
# User inputted arguments will let them search for products using prices, categories, search, and sort by.
@app.route('/products', methods=['GET'])
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






@app.route('/lists', methods=['POST'])

def listsPost():

    listsForm = []
    con = db_engine.engine.raw_connection()
    listsForm = request.get_json()                     #Open database connection
    print(listsForm)
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
    




@app.route('/lists', methods=['GET'])

def listReturn():

    userID = request.args.get('userID', type=int)
    listName = request.args.get('listName', type=str)
    


    listsForm = []
    con = db_engine.engine.raw_connection()
                        #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getUserList', [userID, listName])                      #This is the call to the stored procedure
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
            metric_uom, priority, description, listName, quantity, allergy, diet = row_dict['brand_name'], row_dict['item_name'], row_dict['item_price'], \
            row_dict['images_front_full_url'], row_dict['productsID'], row_dict['item_category'], row_dict['nf_ingredient_statement'], \
            row_dict['nf_calories'], row_dict['nf_calories_from_fat'], row_dict['nf_total_fat'], row_dict['nf_saturated_fat'], \
            row_dict['nf_trans_fatty_acid'], row_dict['nf_polyunsaturated_fat'], row_dict['nf_monounsaturated_fat'], row_dict['nf_cholesterol'], row_dict['nf_sodium'],\
            row_dict['nf_total_carbohydrate'], row_dict['nf_dietary_fiber'], row_dict['nf_sugars'], row_dict['nf_protein'], row_dict['nf_vitamin_a_dv'],\
            row_dict['nf_vitamin_c_dv'], row_dict['nf_calcium_dv'], row_dict['nf_iron_dv'], row_dict['nf_potassium'], row_dict['nf_servings_per_container'],\
            row_dict['nf_serving_size_qty'], row_dict['nf_serving_size_unit'], row_dict['nf_serving_weight_grams'], row_dict['metric_qty'], row_dict['metric_uom'],\
            row_dict['priority'], row_dict['description'], row_dict['listName'], row_dict['quantity'], row_dict['allergy'], row_dict['diet']
            
            product = {'brand_name': brand_name,'item_name': item_name, 'item_price': item_price, 'images_front_full_url': images_front_full_url,\
                       'productsID': productsID, 'item_category': item_category, 'nf_ingredient_statement': nf_ingredient_statement, 'nf_calories': nf_calories,\
                        'nf_calories_from_fat': nf_calories_from_fat, 'nf_total_fat': nf_total_fat, 'nf_saturated_fat': nf_saturated_fat,\
                        'nf_trans_fatty_acid': nf_trans_fatty_acid, 'nf_polyunsaturated_fat': nf_polyunsaturated_fat, 'nf_monounsaturated_fat': nf_monounsaturated_fat,\
                        'nf_cholesterol': nf_cholesterol, 'nf_sodium': nf_sodium, 'nf_total_carbohydrate': nf_total_carbohydrate, 'nf_dietary_fiber': nf_dietary_fiber,\
                        'nf_sugars': nf_sugars, 'nf_protein': nf_protein, 'nf_vitamin_a_dv': nf_vitamin_a_dv, 'nf_vitamin_c_dv': nf_vitamin_c_dv,\
                        'nf_calcium_dv': nf_calcium_dv, 'nf_iron_dv': nf_iron_dv, 'nf_potassium': nf_potassium, 'nf_servings_per_container': nf_servings_per_container,\
                        'nf_serving_size_qty': nf_serving_size_qty, 'nf_serving_size_unit': nf_serving_size_unit, 'nf_serving_weight_grams': nf_serving_weight_grams,\
                        'metric_qty': metric_qty, 'metric_uom': metric_uom, 'priority': priority, 'description': description, 'listName': listName,\
                        'quantity': quantity, 'allergy': allergy, 'diet': diet}
            
            listsForm.append(product)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()         
        print(jsonify(listsForm))                                       #Close database connection
        return jsonify(listsForm) 
    




@app.route('/newList', methods=['POST'])
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
    


@app.route('/newList', methods=['DELETE'])
def deleteItem():

    userID = request.args.get('userID', type=int)
    productsID = request.args.get('productsID', type=int)
    listName = request.args.get('listName', type=str)
    
    deleteForm = []
    con = db_engine.engine.raw_connection()                 #Open database connection
    print(deleteForm)
    

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('deleteFromUserList', [userID, productsID, listName])       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(deleteForm)





@app.route('/newList', methods=['GET'])
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





@app.route('/diet', methods=['POST'])

def dietPost():
    
    con = db_engine.engine.raw_connection()
    dietForm = request.get_json()   
    userID = dietForm.get('userID')
    userAllergy = dietForm.get('customAllergy')
    values = list(dietForm.values())                  #Open database connection
    allergyList = []
    dietList = []
    if 'Peanut' in values[2]:
        allergyList.append('Peanut')
    if 'Dairy' in values[2]:
        allergyList.append('Dairy')
    if 'Gluten' in values[2]:
        allergyList.append('Gluten')
    if 'Eggs' in values[2]:
        allergyList.append('Eggs')
    if 'Soy' in values[2]:
        allergyList.append('Soy')
    if 'Fish' in values[2]:
        allergyList.append('Fish')
    if 'Crustaceans' in values[2]:
        allergyList.append('Crustaceans')


    if 'Keto' in values[1]:
        dietList.append('Keto')
    if 'Vegetarian' in values[1]:
        dietList.append('Vegetarian')
    if 'Vegan' in values[1]:
        dietList.append('Vegan')
    if 'Pescatarian' in values[1]:
        dietList.append('Pescatarian')
    if 'Low Sodium' in values[1]:
        dietList.append('Low Sodium')

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('updateDiet', [userID, ', '.join(str(e) for e in dietList), ', '.join(str(e) for e in allergyList), userAllergy])       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(dietForm)
    




@app.route('/exerciseOPT', methods=['POST'])

def exerciseOPTPost():
    
    con = db_engine.engine.raw_connection()
    exerciseOPTForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('updateExercise', exerciseOPTForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(exerciseOPTForm)
    



# Endpoint for the required form in the exercise page, sends data to backend table.
@app.route('/exerciseREQ', methods=['POST'])

def exerciseREQPost():
    
    con = db_engine.engine.raw_connection()
    exerciseREQForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('updateExercise2', exerciseREQForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(exerciseREQForm)






@app.route('/profile', methods=['POST'])
def updateProfile():
    
    profileForm = []
    con = db_engine.engine.raw_connection()
    profileForm = request.get_json()                     #Open database connection
    print(profileForm)
    

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('updateProfile', profileForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(profileForm)





@app.route('/profile', methods=['GET'])
def getProfile():
    
    userID = request.args.get('userID', type=int)
    


    profileForm = []
    con = db_engine.engine.raw_connection()          #Open database connection
    print(profileForm)
    

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getProfile', [userID])       #This is the call to the stored procedure
        rs = cursor.fetchall()
        
        
        field_names = [d[0] for d in cursor.description]
        for row in rs:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[field_names[i]] = value
        
            email, name, lastName, phoneNumber, profileImage = row_dict['email'], row_dict['name'], row_dict['lastName'], row_dict['phoneNumber'], row_dict['profileImage']

            list = {'email': email, 'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'profileImage': profileImage}
            profileForm.append(list)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(profileForm)
    
# Endpoint for retrieving the status of the forms for the user so they can be marked as complete or incomplete.
@app.route('/status', methods=['GET'])
def getFormStatus():
    
    userID = request.args.get('userID', type=int)

    formStatus = []
    con = db_engine.engine.raw_connection()          #Open database connection
    print(formStatus)

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getPersonFormStatus', [userID])       #This is the call to the stored procedure
        rs = cursor.fetchall()
        
        
        field_names = [d[0] for d in cursor.description]
        for row in rs:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[field_names[i]] = value
        
            dietFilledout, exerciseOPTfilledout ,exerciseREQfilledout= row_dict['dietFilledout'], row_dict['exerciseOPTfilledout'], row_dict['exerciseREQfilledout']

            list = {'dietFilledout': dietFilledout, 'exerciseOPTfilledout': exerciseOPTfilledout, 'exerciseREQfilledout': exerciseREQfilledout}
            formStatus.append(list)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(formStatus)
    
# Endpoint to update that status of the forms upon completion.
@app.route('/updateStatus', methods=['POST'])
def updateStatus():
    
    userID = request.args.get('userID', type=int)

    updateStatusForm = []
    con = db_engine.engine.raw_connection()                  #Open database connection
    print(updateStatusForm)
    

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('updatePersonFormStatus', [userID])       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(updateStatusForm)

@app.route('/exerciseProfile', methods=['GET'])
def getExercise():
    
    userID = request.args.get('userID', type=int)
    


    exerciseProfileForm = []
    con = db_engine.engine.raw_connection()          #Open database connection
    
    form = []

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getExercise', [userID])       #This is the call to the stored procedure

        rs = cursor.fetchall()
        
        #BMR Calculation: Weight, Height, Age, Gender
        field_names = [d[0] for d in cursor.description]
        for row in rs:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[field_names[i]] = value
        
            name, lastName, gender, birthday, heightFeet, heightInches, weight, fitnessLevel = row_dict['name'], row_dict['lastName'], row_dict['gender'], row_dict['birthday'],\
                  row_dict['heightFeet'], row_dict['heightInches'], row_dict['weight'], row_dict['fitnessLevel']

            data = {'name': name, 'lastName': lastName, 'gender': gender, 'birthday': birthday, 'heightFeet': heightFeet, 'heightInches': heightInches,\
                    'weight': weight, 'fitnessLevel': fitnessLevel}
            exerciseProfileForm.append(data)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

        values = list(exerciseProfileForm[0].values())
        
        BMR1 = (88.362 + (13.397*(float(values[6])/2.2)) + (4.799 * ((12.00*(float(values[4]))+float(values[5]))*2.54))) - (5.677 * (float(2023)-float(values[3].year)))
        BMR2 = 447.593 + (9.247*(float(values[6])/2.2)) + (3.098 * ((12.00*(float(values[4]))+float(values[5]))*2.54)) - (4.33 * (float(2023)-float(values[3].year)))
        if values[2].upper() == 'MALE':
            BMR = BMR1
        elif values[2].upper() == 'FEMALE':
            BMR = BMR2
        else:
            BMR = (BMR1+BMR2)/2
        
        activity = int(values[7])//int(2)
        
        ratio = [1.2, 1.375, 1.55, 1.725, 1.9]
        AMR = BMR * ratio[activity-1]
        lossCalories = AMR - 500
        weeklyLCals = lossCalories * 7
        bulkCalories = AMR + 500
        weeklyBCals = bulkCalories * 7

        
        BMI = round((float(values[6]) / (((12.0*float(values[4]))+float(values[5]))**2))*703, 1)
        if BMI < 18.5:
            BMICategory = 'Underweight'
        elif BMI >= 18.5 and BMI < 25:
            BMICategory = 'Healthy'
        elif BMI >= 25 and BMI < 30:
            BMICategory = 'Overweight'
        elif BMI >= 30:
            BMICategory = 'Obesity'

        if lossCalories < 1200:
            lossCalories = 1200

        fields = {'BMR': int(BMR), 'AMR': int(AMR), 'lossCalories': int(lossCalories), 'weeklyLCals': int(weeklyLCals), 'bulkCalories': int(bulkCalories),\
                   'weeklyBCals': int(weeklyBCals), 'BMI': BMI, 'BMICategory': BMICategory}
        form.append(fields)
    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(form)
    

# Endpoint for sending text messages to users who fill out their phone number in the personform table.
@app.route('/send_sms', methods=['POST'])
def send_sms():
    
    number = request.json.get('number')
    message = request.json.get('message')

    twilio_number = '+13204336455'
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=number
    )
    return 'Message sent!'

@app.route('/updatePassword', methods=['POST'])

def updatePasswordPost():
    
    con = db_engine.engine.raw_connection()
    updatePasswordForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('updatePassword', updatePasswordForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(updatePasswordForm)

if __name__ == '__main__':
    app.run(debug=True)