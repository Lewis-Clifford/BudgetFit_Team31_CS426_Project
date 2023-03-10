DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemsFromCatalogAsc`
(
    IN _displayCount INT,
    IN _displayOffset INT,
)
BEGIN
    SELECT
    ItemId, Name, Price, TypeID, CaloricCount
        FROM
            Item
        WHERE
            isActive = 1
        GROUP BY
            Price
            WITH ROLLUP
        ORDER BY
            Price
            ASC
        LIMIT
            _displayCount
        OFFSET
            _displayOffset
        FOR SHARE;
END $$

DELIMITER ;
