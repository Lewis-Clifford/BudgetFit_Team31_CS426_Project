#Author: Cliff Lewis
#Purpose: Endpoint to update the user's password

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

updatePassword = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
updatePassword.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(updatePassword)

updatePassword.config['CORS_HEADERS'] = 'Content-Type'

updatePasswordForm = []

@cross_origin()

@updatePassword.route('/updatePassword', methods=['POST'])

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
    updatePassword.run(debug=True)