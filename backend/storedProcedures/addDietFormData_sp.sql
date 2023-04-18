CREATE DEFINER =`CLIFF`@`%` PROCEDURE `ADDDIETFORMDATA`
(IN _USERID INT, IN _DIET VARCHAR(255), IN _ALLERGY 
VARCHAR(255)) BEGIN 
	START TRANSACTION;
	UPDATE personform p
	SET
	    p.diet = _diet,
	    p.allergy = _allergy,
	    p.isActive = 1,
	    p.modifiedDate = NOW()
	WHERE
	    p.personFormID = _userID;
	UPDATE person p2
	SET
	    p2.isActive = 1,
	    p2.modifiedDate = NOW()
	WHERE p2.personID = userID;
	COMMIT;
	END 
