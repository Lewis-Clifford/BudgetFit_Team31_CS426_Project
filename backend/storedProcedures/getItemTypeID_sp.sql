DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemTypeID`
(
    IN @ItemId INT,
    OUT @TypeID INT
)
BEGIN
    SELECT
    TypeID
        FROM
            Item
        INTO
            @TypeID
        WHERE
            ItemId = @ItemId,
            isActive = 1
        FOR SHARE;
END $$

DELIMITER ;
