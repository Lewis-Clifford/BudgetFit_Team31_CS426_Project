#Author: Cliff Lewis
#Purpose: Endpoint to process request to update the user's profile data

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

profile = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
profile.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(profile)

profile.config['CORS_HEADERS'] = 'Content-Type'



@cross_origin()

@profile.route('/profile', methods=['POST'])
def createList():
    
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

@profile.route('/profile', methods=['GET'])
def getListNames():
    
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

if __name__ == '__main__':
    profile.run(debug=True)