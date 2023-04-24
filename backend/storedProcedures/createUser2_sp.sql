CREATE DEFINER =`CLIFF`@`%` PROCEDURE `CREATEUSER2`
(IN USERNAME VARCHAR(100), IN EMAIL VARCHAR(100), 
IN PASSWORD VARBINARY(255)) BEGIN 
	declare tempUserID int;
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
	    personform (
	        userID,
	        name,
	        gender,
	        phoneNumber,
	        weight,
	        birthday,
	        heightFeet,
	        heightInches,
	        workoutExp,
	        fitnessLevel,
	        allergy,
	        diet,
	        profileImage,
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
	        NULL,
	        NULL,
	        NULL,
	        0,
	        NOW(),
	        NULL
	    );
	COMMIT;
	END 
