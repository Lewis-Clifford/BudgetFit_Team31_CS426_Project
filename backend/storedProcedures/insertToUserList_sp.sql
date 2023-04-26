CREATE DEFINER =`CLIFF`@`%` PROCEDURE `INSERTTOUSERLIST`
(IN _USERID INT, IN _PRODUCTSID INT, IN _LISTNUM INT
, IN _LISTNAME VARCHAR(100)) BEGIN 
	START TRANSACTION;
	INSERT INTO
	    lists (
	        userID,
	        productsID,
	        listNUM,
	        listName,
	        modifiedDate,
	        createdDate
	    )
	VALUES (
	        _userID,
	        _productsID,
	        _listNUM,
	        _listName,
	        NOW(),
	        NOW()
	    );
	COMMIT;
	END 
