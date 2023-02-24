DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateItemName`
(
    IN @Name VARCHAR(100),
    IN ItemId INT
)
BEGIN
    UPDATE
    Items
        SET
            Name = @Name
            modifiedDate = NOW()
        WHERE
            ItemId = @ItemId;
END $$

DELIMITER ;
