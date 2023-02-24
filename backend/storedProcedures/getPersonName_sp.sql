DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetPersonName`
(
    IN @PersonId INT,
    OUT @Name VARCHAR(100)
)
BEGIN
    SELECT
    Name
        FROM
            Person
        INTO
            @Name
        WHERE
            PersonId = @PersonID,
            isActive = 1
        FOR SHARE;
END $$

DELIMITER ;
