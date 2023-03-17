#endpoint to receive json data from login page

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from sqlalchemy import create_engine, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

url = URL.create('mysql', username='cliff', password='PervertCamel21@@', host='localhost', database='db_budgetfit')
app.config['SQLALCHEMY_DATABASE_URI'] = url
db_engine = create_engine(url)

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    login_form = request.json
    if not login_form or not login_form.get('userName') or not login_form.get('password'):
        return jsonify({'msg': 'Invalid login credentials'}), 401

    username = login_form['userName']
    password = login_form['password']

    conn = db_engine.engine.raw_connection()
    cursor = conn.cursor()
    cursor.callproc('userAuth', [username])
    user = cursor.fetchone()

    print(user)

    if user == None:
        return jsonify({'message': 'User not found'})
    
    storedPassword = user[0].decode('utf-8')

    cursor.close()
    conn.close()

    if storedPassword == password:
        access_token = create_access_token(identity=user[2], expires_delta=False)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'msg': 'Invalid login credentials'}), 401

@app.route('/protected')
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    return jsonify({'user_id': user_id}), 200


if __name__ == '__main__':
    app.run(debug=True)