#Author: Cliff Lewis
#Purpose: Queries for login data to be processed in the backend

CREATE DEFINER =`KADEN`@`%` PROCEDURE `USERAUTH`(IN 
UNAME VARCHAR(100)) BEGIN 
	SELECT
	    u.password,
	    u.userName,
	    u.userID
	FROM user u
	WHERE
	    u.userName = uName
	    AND u.activeUser = 1;
	END 
