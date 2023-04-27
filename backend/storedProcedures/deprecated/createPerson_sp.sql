DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CreatePerson`
(
    IN @UID INT,
    IN @Name VARCHAR(100),
    IN @AddStuffHereFromKadensForm VARCHAR(100)
)
BEGIN
    INSERT INTO
        Person (
            UID,
            Name,
            AddStuffHereFromKadensForm,
            isActive,
            createdDate,
            modifiedDate
        )
        VALUES (
            @UID,
            @Name,
            @AddStuffHereFromKadensForm,
            1,
            NOW(),
            NOW()
        );
END $$

DELIMITER ;
