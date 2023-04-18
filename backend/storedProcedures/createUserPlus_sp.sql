CREATE DEFINER =`CLIFF`@`%` PROCEDURE `CREATEUSER2`
(IN USERNAME VARCHAR(100), IN EMAIL VARCHAR(100), 
IN PASSWORD VARBINARY(255)) BEGIN 
	declare tempUserID int;
	DECLARE tempPersonID int;
	START TRANSACTION;
	INSERT INTO
	    USER (
	        userName,
	        email,
	        PASSWORD,
	        activeUser,
	        modifiedDate,
	        createdDate
	    )
	VALUES (
	        userName,
	        email,
	        password,
	        1,
	        NOW(),
	        NOW()
	    );
	SELECT LAST_INSERT_ID() INTO tempUserID;
	INSERT INTO
	    person (
	        userId,
	        isActive,
	        createdDate,
	        modifiedDate
	    )
	VALUES (tempUserID, 0, NULL, NULL);
	INSERT INTO
	    personform (
	        personID,
	        name,
	        gender,
	        phoneNumber,
	        weight,
	        birthday,
	        heightFeet,
	        heightInches,
	        workoutExp,
	        fitnessLevel,
	        isActive,
	        createdDate,
	        modifiedDate
	    )
	VALUES (
	        tempUserID,
	        NULL,
	        NULL,
	        NULL,
	        NULL,
	        NULL,
	        NULL,
	        NULL,
	        NULL,
	        NULL,
	        0,
	        NULL,
	        NULL
	    );
	COMMIT;
	END 