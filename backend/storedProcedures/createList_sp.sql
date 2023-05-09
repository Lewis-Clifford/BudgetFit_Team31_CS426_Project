#Author: Cliff Lewis
#Purpose: Creates a null product in the lists table to select list names per user

CREATE DEFINER =`CLIFF`@`%` PROCEDURE `CREATELIST`(
IN _USERID VARCHAR(255), IN _LISTNAME VARCHAR(255)
, IN _PRIORITY VARCHAR(20), IN _DESCRIPTION VARCHAR
(255)) BEGIN 
	START TRANSACTION;
	INSERT INTO
	    lists (
	        userID,
	        listName,
	        priority,
	        description,
	        createdDate,
	        modifiedDate,
	        quantity
	    )
	VALUES (
	        _userID,
	        _listName,
	        _priority,
	        _description,
	        NOW(),
	        NOW(),
	        0
	    );
	COMMIT;
	END 
