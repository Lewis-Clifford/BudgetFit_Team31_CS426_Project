DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateItemName`
(
    IN _Name VARCHAR(100),
    IN ItemId INT
)
BEGIN
    UPDATE
    Items
        SET
            Name = _Name
            modifiedDate = NOW()
        WHERE
            ItemId = _ItemId;
END $$

DELIMITER ;
