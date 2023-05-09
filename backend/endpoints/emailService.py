#Author: Cliff Lewis
#Purpose: Email service endpoint. Failed due to updated gmail security.

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine
import smtplib

emailService = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
emailService.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(emailService)

emailService.config['CORS_HEADERS'] = 'Content-Type'

emailServiceForm = []

@cross_origin()

@emailService.route('/emailService', methods=['POST'])

def emailServicePost():
    
    
    emailServiceForm = request.get_json()                    
    email = str(emailServiceForm.get('email'))
    print(email)

    gmail_user = 'budgetfit1@gmail.com'
    gmail_password = 'BFITpassword1!'

    sent_from = gmail_user
    to = email
    subject = 'BudgetFit'
    body = 'Welcome to BudgetFit'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, to, subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
                  
                                                  #Close database connection
    return jsonify(emailServiceForm)
    
 
    
if __name__ == '__main__':
    emailService.run(debug=True)