DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `GetUserName`
(
    IN @UID INT,
    OUT @userName VARCHAR(100)
)
BEGIN
    -- assert that there are no duplicate rows
    SELECT DISTINCT
    userName
        FROM
            User
        INTO
            @userName
        WHERE
            UID = @UID,
            isActive = 1
        FOR UPDATE;
END $$

DELIMITER ;
