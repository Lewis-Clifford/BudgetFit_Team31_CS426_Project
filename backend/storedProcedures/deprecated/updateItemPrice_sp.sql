DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateItemPrice`
(
    IN _Price VARCHAR(20),
    IN _ItemId INT
)
BEGIN
    UPDATE
    Items
        SET
            Price = _Price
            modifiedDate = NOW()
        WHERE
            ItemId = _ItemId;
END $$

DELIMITER ;
