DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemTypeID`
(
    IN _ItemId INT,
    OUT _TypeID INT
)
BEGIN
    SELECT
    TypeID
        FROM
            Item
        INTO
            _TypeID
        WHERE
            ItemId = _ItemId,
            isActive = 1
        FOR SHARE;
END $$

DELIMITER ;
