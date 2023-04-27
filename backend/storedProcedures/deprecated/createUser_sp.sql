CREATE DEFINER =`CLIFF`@`%` PROCEDURE `CREATEUSER`(
IN USERNAME VARCHAR(100), IN EMAIL VARCHAR(100), IN 
PASSWORD VARBINARY(100)) BEGIN 


	INSERT INTO
	    USER (
	        userName,
	        email,
	        password,
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
	END 
