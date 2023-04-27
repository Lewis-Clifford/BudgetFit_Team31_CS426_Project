DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateEmail`
(
    IN _userName VARCHAR(100),
    IN _email VARCHAR(100)
)
BEGIN
    UPDATE
    USER
        SET
            email = _email,
            modifiedDate = NOW()
        WHERE
            userName = _userName;
END $$

DELIMITER ;
