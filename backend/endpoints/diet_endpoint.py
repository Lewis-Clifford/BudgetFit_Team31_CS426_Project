#endpoint to receive json data from diet page

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

diet = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
diet.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(diet)

diet.config['CORS_HEADERS'] = 'Content-Type'

dietForm = []

@cross_origin()

@diet.route('/diet', methods=['POST'])

def dietPost():
    
    con = db_engine.engine.raw_connection()
    dietForm = request.get_json()   
    userID = dietForm.get('userID')
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

    userAllergy = values[2].replace(',', '')
    userAllergy = userAllergy.replace('Peanut', '')
    userAllergy = userAllergy.replace('Dairy', '')
    userAllergy = userAllergy.replace('Gluten','')
    userAllergy = userAllergy.replace('Eggs', '')
    userAllergy = userAllergy.replace('Soy', '')
    userAllergy = userAllergy.replace('Fish', '')
    userAllergy = userAllergy.replace('Crustaceans', '')
    if userAllergy[0] == '':
        userAllergy = userAllergy[1:]
    
    print(userAllergy)
    if userAllergy == '':
        userAllergy = None;

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
    
 
    
if __name__ == '__main__':
    diet.run(debug=True)