DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateItemCaloricCount`(
IN @CaloricCount INT, IN @ItemId INT) BEGIN
        UPDATE
        Items
            SET
                CaloricCount = @CaloricCount
                modifiedDate = @modifiedDate
            WHERE
                ItemId = @ItemId;
        END $$

DELIMITER ;
