DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemPrice`
(
    IN _ItemId INT,
    OUT _Price VARCHAR(20)
)
BEGIN
    SELECT
    Price
        FROM
            Item
        INTO
            _Price
        WHERE
            ItemId = _ItemId,
            isActive = 1
        FOR SHARE;
END $$

DELIMITER ;
