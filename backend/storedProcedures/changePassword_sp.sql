DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `ChangePassword`
(
    IN _userName VARCHAR(100),
    IN _password VARBINARY(100),
    IN _email VARCHAR(100)
)
BEGIN
    UPDATE
    USER
        SET
            password = _password,
            modifiedDate = NOW()
        WHERE
            userName = _userName
            AND
            email = _email;
END $$

DELIMITER ;
