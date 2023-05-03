CREATE DEFINER=`cliff`@`%` PROCEDURE `updateDiet`(IN _userID INT, IN _diet VARCHAR(255), IN _allergy VARCHAR(255), IN _userAllergy VARCHAR(100))
BEGIN
  START TRANSACTION;
    UPDATE personform p SET p.diet = _diet, p.allergy = _allergy, p.userAllergy = _userAllergy, p.isActive = 1, p.modifiedDate = NOW()
    WHERE p.userID = _userID;


  COMMIT;
END
