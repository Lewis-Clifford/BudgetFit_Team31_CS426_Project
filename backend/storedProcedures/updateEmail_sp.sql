DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `UpdateEmail`(
IN @userName VARCHAR(100), IN @email VARCHAR(100)) BEGIN
        UPDATE
        USER
            SET
                email = @email,
                modifiedDate = NOW()
            WHERE
                userName = @userName;
        END $$

DELIMITER ;
