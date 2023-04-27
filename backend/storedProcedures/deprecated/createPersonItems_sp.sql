DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CreatePersonItems`
(
    IN _PersonID INT,
    IN _ItemID INT,
    IN _ItemListTypeID INT
)
BEGIN
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
            _PersonID,
            _ItemID,
            _ItemListTypeID,
            1,
            NOW(),
            NOW()
        );
END $$

DELIMITER ;
