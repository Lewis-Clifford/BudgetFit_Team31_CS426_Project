#Author: Cliff Lewis
#Purpose: Queries profile data to display in the front end


CREATE DEFINER =`CLIFF`@`%` PROCEDURE `GETPROFILE`(
IN _USERID INT) BEGIN 
	START TRANSACTION;
	SELECT
	    u.email,
	    p.name,
	    p.lastName,
	    p.phoneNumber,
	    p.profileImage
	FROM user u, personform p
	WHERE u.userID = _userID;
	COMMIT;
	END 
