DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemPrice`(
IN @ItemId INT, OUT @Price VARCHAR(20)) BEGIN
        SELECT
        Price
            FROM
                Item
            INTO
                @Price
            WHERE
                ItemId = @ItemId,
                isActive = 1
            FOR SHARE;
        END $$

DELIMITER ;
