#Author: Cliff Lewis
#Purpose: Endpoint processes user data to produce usable information for the user
#         derived from the user's data

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import URL
from sqlalchemy import create_engine

exerciseProfile = Flask(__name__)

url = URL.create("mysql", username='cliff', password='PervertCamel21@@',host='localhost',database='db_budgetfit')   #Connection string. Will be different per local database.
exerciseProfile.config['SQLALCHEMY_DATABASE_URI'] = url                                                                    #Connect SQLAlchemy to Database
db_engine = create_engine(url)     

cors = CORS(exerciseProfile)

exerciseProfile.config['CORS_HEADERS'] = 'Content-Type'



@cross_origin()



@exerciseProfile.route('/exerciseProfile', methods=['GET'])
def getListNames():
    
    userID = request.args.get('userID', type=int)
    


    exerciseProfileForm = []
    con = db_engine.engine.raw_connection()          #Open database connection
    
    form = []

    try:
        
        cursor = con.cursor()                                                   #Create connection cursor
        cursor.callproc('getExercise', [userID])       #This is the call to the stored procedure

        rs = cursor.fetchall()
        
        #BMR Calculation: Weight, Height, Age, Gender
        field_names = [d[0] for d in cursor.description]
        for row in rs:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[field_names[i]] = value
        
            name, lastName, gender, birthday, heightFeet, heightInches, weight, fitnessLevel = row_dict['name'], row_dict['lastName'], row_dict['gender'], row_dict['birthday'],\
                  row_dict['heightFeet'], row_dict['heightInches'], row_dict['weight'], row_dict['fitnessLevel']


            data = {'name': name, 'lastName': lastName, 'gender': gender, 'birthday': birthday, 'heightFeet': heightFeet, 'heightInches': heightInches,\
                    'weight': weight, 'fitnessLevel': fitnessLevel}
            exerciseProfileForm.append(data)

        cursor.close()                                                          #Close connection cursor
        con.commit()                                                            #Commit changes to update database

        values = list(exerciseProfileForm[0].values())
        
        BMR1 = (88.362 + (13.397*(float(values[6])/2.2)) + (4.799 * ((12.00*(float(values[4]))+float(values[5]))*2.54))) - (5.677 * (float(2023)-float(values[3].year)))
        BMR2 = 447.593 + (9.247*(float(values[6])/2.2)) + (3.098 * ((12.00*(float(values[4]))+float(values[5]))*2.54)) - (4.33 * (float(2023)-float(values[3].year)))
        if values[2].upper() == 'MALE':
            BMR = BMR1
        elif values[2].upper() == 'FEMALE':
            BMR = BMR2
        else:
            BMR = (BMR1+BMR2)/2
        
        activity = int(values[7])//int(2)
        
        ratio = [1.2, 1.375, 1.55, 1.725, 1.9]
        AMR = BMR * ratio[activity-1]
        lossCalories = AMR - 500
        weeklyLCals = lossCalories * 7
        bulkCalories = AMR + 500
        weeklyBCals = bulkCalories * 7

        
        BMI = round((float(values[6]) / (((12.0*float(values[4]))+float(values[5]))**2))*703, 1)
        if BMI < 18.5:
            BMICategory = 'Underweight'
        elif BMI >= 18.5 and BMI < 25:
            BMICategory = 'Healthy'
        elif BMI >= 25 and BMI < 30:
            BMICategory = 'Overweight'
        elif BMI >= 30:
            BMICategory = 'Obesity'

        if lossCalories < 1200:
            lossCalories = 1200

        fields = {'BMR': int(BMR), 'AMR': int(AMR), 'lossCalories': int(lossCalories), 'weeklyLCals': int(weeklyLCals), 'bulkCalories': int(bulkCalories),\
                   'weeklyBCals': int(weeklyBCals), 'BMI': BMI, 'BMICategory': BMICategory}
        form.append(fields)
    except Exception as e:
        print(e)
    
    finally:
        con.close()                                                #Close database connection
        return jsonify(form)

if __name__ == '__main__':
    exerciseProfile.run(debug=True)