#Author: Cliff Lewis
#Purpose: Endpoint to process requests to create a new user account

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

register = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
register.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)                                                                                      #Create Engine to Use Database

cors = CORS(register)

register.config['CORS_HEADERS'] = 'Content-Type'

registerForm = []

@cross_origin()

@register.route('/register', methods=['GET'])

def registerGet():
    if len(registerForm) > 0:
        return jsonify(registerForm) #Test response
    else:
        return '<h1>Form is Blank</h1>'


@register.route('/register', methods=['POST'])

def registerPost():
    
    con = db_engine.engine.raw_connection()
    registerForm = request.get_json()                     #Open database connection
    try:
        

        cursor = con.cursor()                                   #Create connection cursor
        cursor.callproc('createUser2', registerForm.values())    #This is the call to the stored procedure
        cursor.close()                                          #Close connection cursor
        con.commit()                                            #Commit changes to update database

        
        

    except Exception as e: print(e)
    
    finally:
        con.close()  
        return jsonify(registerForm)
    
                                               #Close database connection

@register.route('/register', methods=['DELETE'])

def registerDelete():
    try:
        registerForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400

if __name__ == '__main__':
    register.run(debug=True)