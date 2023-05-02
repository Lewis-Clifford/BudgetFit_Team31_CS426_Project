CREATE DEFINER =`CLIFF`@`%` PROCEDURE `INSERTTOUSERLIST`
(IN _USERID INT, IN _PRODUCTSID INT, IN _LISTNAME 
VARCHAR(100), IN _PRIORITY VARCHAR(20), IN _DESCRIPTION 
VARCHAR(255), IN _QUANTITY INT) BEGIN 
	DECLARE productExists INT;

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SET foreign_key_checks = 0;
SELECT
    quantity INTO productExists
FROM lists
WHERE
    lists.userID = _userID
    AND lists.productsID = _productsID FOR
UPDATE;

IF productExists IS NOT NULL THEN 
UPDATE lists
SET
    lists.quantity = _quantity,
    lists.modifiedDate = NOW()
WHERE
    lists.userID = _userID
    AND lists.productsID = _productsID;

ELSE 
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

END IF;
SET foreign_key_checks = 1;
CALL allergyQuery(_userID, _productsID);
COMMIT;

END 