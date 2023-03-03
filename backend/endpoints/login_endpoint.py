#endpoint to receive json data from login page

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
import uuid

login = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
login.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)

cors = CORS(login)

login.config['CORS_HEADERS'] = 'Content-Type'

loginForm = []

@cross_origin()

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'token missing'})
        
        con = db_engine.engine.raw_connection()
        loginForm = request.get_json()

        try:
            data = jwt.decode(token, login.config['SECRET_KEY'], algorithms = ['HS256'])
            #Insert Stored procedure to select user from table
            cursor = con.cursor()                                                           #Create connection cursor
            currentUser = cursor.callproc('userAuth', data['userID'])      #Change Stored Procedure
            cursor.close()                                                                  #Close connection cursor
            con.commit() #Not sure if this line is needed if not changing the database. Should ask Vinh

        except Exception as e:
            print(e)
            #return jsonify({'message': 'token is invalid'}) #Not sure if will cause errors

        finally:
            con.close()
            return f(currentUser, *args, **kwargs)
    return decorator




@login.route('/login', methods=['POST'])

def loginUser():
    auth = request.authorization
    if not auth or auth.username or not auth.password:
        return make_response('could not verify', 401, {'Authentication': '"login required"'})
    
    con = db_engine.engine.raw_connection()
    loginForm = request.get_json()

    try:
        cursor = con.cursor()                                   #Create connection cursor
        currentUser = cursor.callproc('checkUserNamePassword', loginForm.values())    #This is the call to the stored procedure
        cursor.close()                                          #Close connection cursor
        con.commit()

    except Exception as e:
        print(e)

    finally:
        con.close()

    if check_password_hash(currentUser.password, auth.password):
        token = jwt.encode({'public_id': currentUser.userID, 'exp':  datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, login.config['SECRET_KEY'], "HS256")

        return jsonify({'token': token})

    return make_response('could not verify',  401, {'Authentication': '"login required"'})
    

    

@login.route('/login', methods=['DELETE'])

def loginDelete():
    try:
        loginForm.clear()
        return 'Deleted', 200

    except:
        return 'Failed', 400
    
if __name__ == '__main__':
    login.run(debug=True)