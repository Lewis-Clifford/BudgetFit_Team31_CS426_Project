DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CreatePersonFormData`
(
    IN _PersonID INT
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
            _PersonID,
            1,
            NOW(),
            NOW()
        );
END $$

DELIMITER ;
