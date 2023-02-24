DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CREATEPERSONITEMS` (
IN @PersonID INT, IN @ItemID INT, IN @ItemListTypeID INT) BEGIN
        INSERT INTO
            PersonItems (
                PersonID,
                ItemID,
                ItemListTypeID,
                isActive,
                createdDate,
                modifiedDate
            )
        VALUES (
                @PersonID,
                @ItemID,
                @ItemListTypeID,
                1,
                NOW(),
                NOW()
            );
        END $$

DELIMITER ;
