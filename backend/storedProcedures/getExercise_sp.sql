#Author: Cliff Lewis
#Purpose: Queries exercise related data to generate derived data in the backend

CREATE DEFINER=`cliff`@`%` PROCEDURE `getExercise`(IN _userID INT)
BEGIN
  START TRANSACTION;
    SELECT p.name, p.lastName, p.gender, p.birthday, p.heightFeet, p.heightInches, p.weight, p.fitnessLevel FROM personform p WHERE p.userID = _userID and p.isActive = 1;
  COMMIT;
END