CREATE DEFINER=`root`@`localhost` PROCEDURE `getPersonFormStatus`(IN _USERID INT)
BEGIN
    SELECT dietFilledout, exerciseOPTfilledout, exerciseREQfilledout 
    FROM personform 
    WHERE userID = _USERID;
END