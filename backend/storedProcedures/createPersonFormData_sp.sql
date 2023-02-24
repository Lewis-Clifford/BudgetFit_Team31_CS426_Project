DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CreatePersonFormData`
(
    IN @PersonID INT
)
BEGIN
    INSERT INTO
        PersonFormData (
            PersonID,
            isActive,
            createdDate,
            modifiedDate
        )
        VALUES (
            @PersonID,
            1,
            NOW(),
            NOW()
        );
END $$

DELIMITER ;
