from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.mysql import VARBINARY, VARCHAR, BOOLEAN, DATETIME
from sqlalchemy.sql import text
from sqlalchemy import URL
from datetime import datetime
from mysql.connector import MySQLConnection, Error

app = Flask(__name__)
url = URL.create('mysql', username='cliff', password='PervertCamel21@@', host='localhost', database='db_budgetfit')
app.config['SQLALCHEMY_DATABASE_URI'] = url

db_engine = create_engine(url)

# Raw JSON
input = {"Name": "Chicken and Rice", "Price": "8.99", "TypeID": 2, "CaloricCount", 250}

con = db_engine.engine.raw_connection()

try:
    cursor = con.cursor()
    cursor.callproc('CreateItem', input.values())
    cursor.close()
    con.commit()
finally:
    con.close()

print('Item has been added to the catalog.')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
