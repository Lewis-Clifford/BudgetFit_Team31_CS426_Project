from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy #From ORM version, may be able to remove
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey #unused imports left in for later reference
from sqlalchemy.dialects.mysql import VARBINARY, VARCHAR, BOOLEAN, DATETIME
from sqlalchemy.sql import text
from sqlalchemy import inspect, URL
from datetime import datetime


app = Flask(__name__)
url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit') #Connection string
app.config['SQLALCHEMY_DATABASE_URI'] = url 

metadata = MetaData()

user = Table('user', metadata, 
    Column('id', Integer, unique=True, primary_key=True, autoincrement=True, ),
    Column('email', VARCHAR(100), unique=True),
    Column('password', VARBINARY(100)),
    Column('activeUser', BOOLEAN),
    Column('modifiedDate', DATETIME),
    Column('createdDate', DATETIME)
)

engine = create_engine(url)
metadata.create_all(engine)

'''
with engine.connect() as con:
    
    testData = ({"id":1,"email": "test@gmail.com", "password": 0, "activeUser": True, "modifiedDate": datetime.now(), "createdDate": datetime.now()},
    {"id":2,"email": "test@gmail.com", "password": 0, "activeUser": True, "modifiedDate": datetime.now(), "createdDate": datetime.now()}
    )

    input = text("INSERT INTO user(id, email, password, activeUser, modifiedDate, createdDate) VALUES (:id, :email,:password,:activeUser,:modifiedDate,:createdDate)")

    for line in testData:
        con.execute(input, **line)

'''
with engine.connect() as con:

    table = con.execute('SELECT * FROM user')

    for record in table:
        print(record)




if __name__ == '__main__':

    app.run(debug=True)
    