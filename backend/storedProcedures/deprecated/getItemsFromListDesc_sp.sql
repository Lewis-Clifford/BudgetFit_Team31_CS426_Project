DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetItemsFromListDesc`
(
    IN _PersonID INT,
    IN _displayCount INT,
    IN _displayOffset INT,
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
            p.PersonID = _PersonID,
            p.isActive = 1
        GROUP BY
            i.Price
            WITH ROLLUP
        ORDER BY
            i.Price
            DESC
        LIMIT
            _displayCount
        OFFSET
            _displayOffset
        FOR SHARE;
END $$

DELIMITER ;
