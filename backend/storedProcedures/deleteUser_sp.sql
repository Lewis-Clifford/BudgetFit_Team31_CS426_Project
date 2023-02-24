DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `DeleteUser`
(
    IN @userName VARCHAR(100)
)
BEGIN
    UPDATE
    USER
        SET
            isActive = 0,
            modifiedDate = NOW()
        WHERE
            userName = @userName;
END $$

DELIMITER ;
