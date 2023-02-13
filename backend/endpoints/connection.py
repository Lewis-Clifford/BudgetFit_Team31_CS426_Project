from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect, URL


app = Flask(__name__)
url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')
app.config['SQLALCHEMY_DATABASE_URI'] = url #need database URI

engine = create_engine(url)


with engine.connect() as con:
    print("working")




if __name__ == '__main__':

    app.run(debug=True)
    