#Author: Cliff Lewis
#Purpose: Updates password field of user table

CREATE DEFINER=`cliff`@`%` PROCEDURE `updatePassword`(IN _userID INT, IN _newPassword VARBINARY(100))
BEGIN
  START TRANSACTION;
    UPDATE user SET user.password = _newPassword, user.modifiedDate = NOW()
      WHERE user.userID = _userID;
  COMMIT;
END