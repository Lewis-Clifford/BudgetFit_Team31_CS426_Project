DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemsFromCatalogDesc`
(
    IN @displayCount INT,
    IN @displayOffset INT,
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
            DESC
        LIMIT
            @displayCount
        OFFSET
            @displayOffset
        FOR SHARE;
END $$

DELIMITER ;
