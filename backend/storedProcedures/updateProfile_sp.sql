CREATE DEFINER =`CLIFF`@`%` PROCEDURE `UPDATEPROFILE`
(IN _USERID INT, IN _NAME VARCHAR(100), IN _LASTNAME 
VARCHAR(100), IN _EMAIL VARCHAR(255), IN _PHONENUMBER 
VARCHAR(20), IN _PROFILEIMAGE VARCHAR(255)) BEGIN 
	START TRANSACTION;
	UPDATE user u
	SET u.email = _email
	WHERE u.userID = _userID;
	UPDATE personform p
	SET
	    p.name = _name,
	    p.lastName = _lastName,
	    p.profileImage = _profileImage,
	    p.phoneNumber = _phoneNumber
	WHERE p.userID = _userID;
	COMMIT;
	END 
