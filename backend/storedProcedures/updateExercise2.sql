-- Author: Kaden Nesch
-- This stored procedure will send the information that the users filled out in the frontend to the backend table for the required exercise form.

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateExercise2`(IN USERID INT, IN exercisepreference VARCHAR(100), IN exercisetype VARCHAR
(100), IN weightgoal VARCHAR(100), IN weightplan VARCHAR(100))
BEGIN 
	START TRANSACTION;
	UPDATE personform p
	SET
	    p.exercisePreference = exercisepreference,
      p.exerciseType = exercisetype,
      p.weightGoal = weightgoal,
      p.weightPlan = weightplan,
	    p.isActive = 1,
	    p.modifiedDate = NOW()
	WHERE
	    p.userID = userID;
	COMMIT;
	END