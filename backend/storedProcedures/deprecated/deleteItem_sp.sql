DELIMITER $$

CREATE DEFINER = `CLIFF`@`%` PROCEDURE IF NOT EXISTS `DeleteItem`
(
    IN _ItemId INT
)
BEGIN
    -- 2 tables will be modified

    -- Query server clock for time point
    DECLARE
        currentTime DATETIME;
    SET
        currentTime = NOW();

    -- Commence scope
    START TRANSACTION;

    -- Query 1
    UPDATE
    Items
        SET
            isActive = 0,
            modifiedDate = currentTime
        WHERE
            ItemId = _ItemId;

    -- Query 2
    UPDATE
    PersonItems
        SET
            isActive = 0,
            modifiedDate = currentTime
        WHERE
            ItemId = _ItemId;

    -- Attempt synchronous execution
    DECLARE
        EXIT HANDLER FOR SQLEXCEPTION;

    -- Catch: Condition classified as SQLEXCEPTION
    BEGIN
        ROLLBACK;
        EXIT PROCEDURE;
    END;

    -- Adjourn scope
    COMMIT;

END $$

DELIMITER ;
        


