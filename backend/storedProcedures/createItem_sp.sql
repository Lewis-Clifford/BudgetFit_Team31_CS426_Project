DELIMITER $$

CREATE DEFINER =`CLIFF`@`%` PROCEDURE IF NOT EXISTS `CreateItem`
(
    IN _Name VARCHAR(100),
    IN _Price VARCHAR(20),
    IN _TypeID INT,
    IN _CaloricCount INT
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
            _Name,
            _Price,
            _TypeID,
            _CaloricCount,
            1,
            NOW(),
            NOW()
        );
END $$

DELIMITER ;
