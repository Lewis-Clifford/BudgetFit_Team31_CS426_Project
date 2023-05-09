#Test Script for db connection
#Author: Cliff Lewis
from sqlalchemy import URL
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.sql import text


register = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
register.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)                                                                                      #Create Engine to Use Database


registerForm = {'userName': 'Name',
                'email': 'email@email.com', 
                'password': 'testPassword'}

record = {}
userName = None
email = None
password = None

passed1 = False
passed2 = None

con = db_engine.engine.raw_connection()                     #Open database connection

    

cursor = con.cursor()                                   #Create connection cursor
cursor.callproc('createUser', registerForm.values())    #This is the call to the stored procedure
cursor.close()                                          #Close connection cursor
con.commit()                                            #Commit changes to update database
con.close()


#cursor = con.cursor()                                   #Create connection cursor
#record = cursor.callproc('testRecordReturn', [registerForm.get('userName'), userName, email, password])    #This is the call to the stored procedure
#cursor.close()                                          #Close connection cursor
#con.commit()                                            #Commit changes to update database

with db_engine.connect() as conn:

    record = conn.execute(text('SELECT u.userName, u.email, u.password FROM USER u WHERE u.userName = "Name"'))

    for row in record:
        


        if row.userName == "Name":
            passed1 = True


con = db_engine.engine.raw_connection() 
cursor = con.cursor()                                   #Create connection cursor
cursor.callproc('testRecordDelete', ['Name'])    #This is the call to the stored procedure
#record = cursor.callproc('testRecordReturn', [registerForm.get('userName'), userName, email, password])
cursor.close()                                          #Close connection cursor
con.commit()   
con.close()


with db_engine.connect() as conn:

    record = conn.execute(text('SELECT u.userName, u.email, u.password FROM USER u WHERE u.userName = "Name"'))

   
    if record.rowcount == 0:
        passed2 = True
   





print(passed1, passed2)
                                            

if __name__ == '__main__':
    register.run(debug=True, use_reloader=False)