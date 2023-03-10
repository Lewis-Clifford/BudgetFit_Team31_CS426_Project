DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetUserName`
(
    IN _UID INT,
    OUT _userName VARCHAR(100)
)
BEGIN
    -- assert that there are no duplicate rows
    SELECT DISTINCT
    userName
        FROM
            User
        INTO
            _userName
        WHERE
            UID = _UID,
            isActive = 1
        FOR UPDATE;
END $$

DELIMITER ;
