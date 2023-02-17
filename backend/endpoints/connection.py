from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy #From ORM version, may be able to remove
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey #unused imports left in for later reference
from sqlalchemy.dialects.mysql import VARBINARY, VARCHAR, BOOLEAN, DATETIME
from sqlalchemy.sql import text
from sqlalchemy import URL
from datetime import datetime
from mysql.connector import MySQLConnection, Error



app = Flask(__name__)
url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit') #Connection string
app.config['SQLALCHEMY_DATABASE_URI'] = url 






db_engine = create_engine(url)
    

input = {"email": "test@gmail.com", "password": None}
    
con = db_engine.engine.raw_connection()


### Call stored procedure
try:
    cursor = con.cursor()
    cursor.callproc('createUser', input.values())
    cursor.close()
    con.commit()   
finally:
    con.close()     


with db_engine.connect() as con:

    table = con.execute(text('SELECT * FROM user'))

    for record in table:
        print(record)




if __name__ == '__main__':

    app.run(debug=True, use_reloader=False)
    