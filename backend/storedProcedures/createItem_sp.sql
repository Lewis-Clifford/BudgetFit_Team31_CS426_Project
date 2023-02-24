DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CreateItem`
(
    IN @Name VARCHAR(100),
    IN @Price VARCHAR(20),
    IN @TypeID INT,
    IN @CaloricCount INT
)
BEGIN
    INSERT INTO
        Items (
            Name,
            Price,
            TypeID,
            CaloricCount,
            isActive,
            createdDate,
            modifiedDate
        )
        VALUES (
            @Name,
            @Price,
            @TypeID,
            @CaloricCount,
            1,
            NOW(),
            NOW()
        );
END $$

DELIMITER ;
