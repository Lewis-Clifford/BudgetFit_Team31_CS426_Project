DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateItemCaloricCount`
(
    IN _CaloricCount INT,
    IN _ItemId INT
)
BEGIN
    UPDATE
    Items
        SET
            CaloricCount = _CaloricCount
            modifiedDate = _modifiedDate
        WHERE
            ItemId = _ItemId;
END $$

DELIMITER ;
