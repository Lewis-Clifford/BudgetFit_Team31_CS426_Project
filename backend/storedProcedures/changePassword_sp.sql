DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `ChangePassword`
(
    IN @userName VARCHAR(100),
    IN @password VARBINARY(100),
    IN @email VARCHAR(100)
)
BEGIN
    UPDATE
    USER
        SET
            password = @password,
            modifiedDate = NOW()
        WHERE
            userName = @userName
            AND
            email = @email;
END $$

DELIMITER ;
