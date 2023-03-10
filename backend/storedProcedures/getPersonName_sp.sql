DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetPersonName`
(
    IN _PersonId INT,
    OUT _Name VARCHAR(100)
)
BEGIN
    SELECT
    Name
        FROM
            Person
        INTO
            _Name
        WHERE
            PersonId = _PersonID,
            isActive = 1
        FOR SHARE;
END $$

DELIMITER ;
