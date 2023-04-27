CREATE DEFINER =`CLIFF`@`%` PROCEDURE `GETLISTNAMES`
(IN _USERID INT) BEGIN 
	Start transaction;
	SELECT
	    lists.listName,
	    lists.priority,
	    lists.description
	FROM lists
	WHERE lists.listID in (
	        SELECT max(lists.listID)
	        FROM lists
	        WHERE lists.userID = _userID
	        GROUP BY lists.listName
	    );
	Commit;
	END 
