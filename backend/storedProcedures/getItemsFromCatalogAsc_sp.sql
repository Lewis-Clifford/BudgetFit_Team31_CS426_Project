DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemsFromCatalogAsc`
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
            ASC
        LIMIT
            @displayCount
        OFFSET
            @displayOffset
        FOR SHARE;
END $$

DELIMITER ;
