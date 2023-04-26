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

listsForm = []

@cross_origin()

@lists.route('/listSave', methods=['POST'])

def listsPost():
    
    con = db_engine.engine.raw_connection()
    listsForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('createUserList', listsForm.values())       #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(listsForm)
    
@lists.route('/listView', methods=['POST'])

def listReturn():
    
    con = db_engine.engine.raw_connection()
    listsForm = request.get_json()                     #Open database connection

    try:
        

        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getUserList', listsForm.values())                      #This is the call to the stored procedure
        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(listsForm) 
    
if __name__ == '__main__':
    lists.run(debug=True)