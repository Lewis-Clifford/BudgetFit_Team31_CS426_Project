CREATE DEFINER =`CLIFF`@`%` PROCEDURE `INSERTTOUSERLIST`
(IN _USERID INT, IN _PRODUCTSID INT, IN _LISTNAME 
VARCHAR(100), IN _PRIORITY VARCHAR(20), IN _DESCRIPTION 
VARCHAR(255), IN _QUANTITY INT) BEGIN 
	START TRANSACTION;

SET foreign_key_checks = 0;

INSERT INTO
    lists (
        userID,
        productsID,
        listName,
        priority,
        description,
        quantity,
        modifiedDate,
        createdDate
    )
VALUES (
        _userID,
        _productsID,
        _listName,
        _priority,
        _description,
        _quantity,
        NOW(),
        NOW()
    );

SET foreign_key_checks = 1;

COMMIT;

END 
