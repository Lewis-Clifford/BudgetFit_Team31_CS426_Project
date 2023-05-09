-- Author: Kaden Nesch
-- This stored procedure gets the personForm status to see if the forms are filled out or not.

CREATE DEFINER=`root`@`localhost` PROCEDURE `getPersonFormStatus`(IN _USERID INT)
BEGIN
    SELECT dietFilledout, exerciseOPTfilledout, exerciseREQfilledout 
    FROM personform 
    WHERE userID = _USERID;
END