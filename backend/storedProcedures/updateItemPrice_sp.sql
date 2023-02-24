DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateItemPrice`
(
    IN @Price VARCHAR(20),
    IN @ItemId INT
)
BEGIN
    UPDATE
    Items
        SET
            Price = @Price
            modifiedDate = NOW()
        WHERE
            ItemId = @ItemId;
END $$

DELIMITER ;
