#Author: Cliff Lewis
#Purpose: Updates user exercise data in the personform table

CREATE DEFINER =`CLIFF`@`%` PROCEDURE `UPDATEEXERCISE`
(IN USERID INT, IN NAME VARCHAR(100), IN GENDER VARCHAR
(100), IN PHONENUMBER VARCHAR(20), IN WEIGHT DECIMAL
(8, 2), IN BIRTHDAY DATE, IN HEIGHTFEET INT, IN HEIGHTINCHES 
INT, IN WORKOUTEXP INT, IN FITNESSLEVEL INT) BEGIN 
	START TRANSACTION;
	UPDATE personform p
	SET
	    p.name = name,
	    p.gender = gender,
	    p.phoneNumber = phoneNumber,
	    p.weight = weight,
	    p.birthday = birthday,
	    p.heightFeet = heightFeet,
	    p.heightInches = heightInches,
	    p.workoutExp = workoutExp,
	    p.fitnessLevel = fitnessLevel,
	    p.isActive = 1,
	    p.modifiedDate = NOW()
	WHERE
p.userID = userID;
	COMMIT;
	END 
