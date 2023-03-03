DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemsFromListAsc`
(
    IN @PersonID INT,
    IN @displayCount INT,
    IN @displayOffset INT,
)
BEGIN
    SELECT -- INNER JOIN
    p.PersonItemID, p.PersonID, p.ItemID, p.ItemListTypeID,
    i.Name, i.Price, i.TypeID, i.CaloricCount
        FROM
            PersonItems AS p
        INNER JOIN
            Items AS i
        ON
            p.ItemID = i.ItemID
        WHERE
            p.PersonID = @PersonID,
            p.isActive = 1
        GROUP BY
            i.Price
            WITH ROLLUP
        ORDER BY
            i.Price
            ASC
        LIMIT
            @displayCount
        OFFSET
            @displayOffset
        FOR SHARE;
END $$

DELIMITER ;
