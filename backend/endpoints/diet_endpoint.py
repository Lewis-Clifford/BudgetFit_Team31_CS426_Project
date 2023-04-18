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
    dietForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('addDietFormData', dietForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(dietForm)
    
 
    
if __name__ == '__main__':
    diet.run(debug=True)