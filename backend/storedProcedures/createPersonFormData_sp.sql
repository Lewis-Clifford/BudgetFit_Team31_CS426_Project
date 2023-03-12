DELIMITER 

CREATE DEFINER =`ROOT`@`%` PROCEDURE `CREATEPERSONFORMDATA` 
	(
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
INSERT INTO
    personform (
        name,
        gender,
        phoneNumber,
        weight,
        birthday,
        heightFeet,
        heightInches,
        workoutExp,
        fitnessLevel,
        isActive,
        createdDate,
        modifiedDate
    )
VALUES (
        name,
        gender,
        phoneNumber,
        weight,
        birthday,
        heightFeet,
        heightInches,
        workoutExp,
        fitnessLevel,
        1,
        NOW(),
        NOW()
    );

END 

DELIMITER
