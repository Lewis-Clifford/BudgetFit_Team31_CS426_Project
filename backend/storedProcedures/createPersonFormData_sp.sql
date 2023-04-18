CREATE DEFINER =`CLIFF`@`%` PROCEDURE `CREATEPERSONFORMDATA` 
	(
	    IN userID INT,
	    IN name VARCHAR(100),
	    IN gender VARCHAR(100),
	    IN phoneNumber VARCHAR(20),
	    IN weight DECIMAL(8, 2),
	    IN birthday DATE,
	    IN heightFeet INT,
	    IN heightInches INT,
	    IN workoutExp INT,
	    IN fitnessLevel INT
	)

BEGIN
START TRANSACTION;

UPDATE personform p
SET
    p.name = name,
    p.gender = gender,
    p.phoneNumber = phoneNumber,
    p.weight = weight,
    p.birthday = birthday,
    p.heightFeet = heightFeet,
    p.heightInches = heightInches,
    p.workoutExp = workoutExp,
    p.fitnessLevel = fitnessLevel,
    p.isActive = 1,
    p.createdDate = NOW(),
    p.modifiedDate = NOW()
WHERE
    p.personFormID = userID;

UPDATE person p2
SET
    p2.isActive = 1,
    p2.createdDate = NOW(),
    p2.modifiedDate = NOW()
WHERE p2.personID = userID;

COMMIT;
END 
