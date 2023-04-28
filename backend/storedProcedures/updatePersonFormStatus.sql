CREATE DEFINER=`root`@`localhost` PROCEDURE `updatePersonFormStatus`(IN _USERID INT)
BEGIN
    DECLARE dietFilledOut INT DEFAULT 0;
    DECLARE exerciseOPTFilledout INT DEFAULT 0;
    DECLARE exerciseREQFilledout INT DEFAULT 0;

    SELECT IFNULL(allergy, '') INTO @allergy FROM personform WHERE userID = _USERID;
    SELECT IFNULL(exercisePreference, '') INTO @exercisePreference FROM personform WHERE userID = _USERID;
    SELECT IFNULL(weightGoal, '') INTO @weightGoal FROM personform WHERE userID = _USERID;

    IF (@allergy != '') THEN SET dietFilledout = 1; END IF;
    IF (@exercisePreference != '') THEN SET exerciseOPTfilledout = 1; END IF;
    IF (@weightGoal != '') THEN SET exerciseREQfilledout = 1; END IF;

    UPDATE personform
    SET dietFilledout = dietFilledout,
        exerciseOPTfilledout = exerciseOPTfilledout,
        exerciseREQfilledout = exerciseREQfilledout
    WHERE userID = _USERID;
END