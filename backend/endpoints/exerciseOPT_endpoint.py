#endpoint to receive json data from exercise page

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

exerciseOPT = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
exerciseOPT.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(exerciseOPT)

exerciseOPT.config['CORS_HEADERS'] = 'Content-Type'

exerciseOPTForm = []

@cross_origin()

@exerciseOPT.route('/exerciseOPT', methods=['POST'])

def exerciseOPTPost():
    
    con = db_engine.engine.raw_connection()
    exerciseOPTForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('createPersonFormData', exerciseOPTForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e: print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(exerciseOPTForm)
    
 
    
if __name__ == '__main__':
    exerciseOPT.run(debug=True)