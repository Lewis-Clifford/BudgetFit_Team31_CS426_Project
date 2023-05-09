CREATE TABLE
    db_budgetfit.person (
        personID int NOT NULL AUTO_INCREMENT,
        userID int NOT NULL COMMENT 'Foreign Key',
        isActive tinyint(1) DEFAULT NULL,
        createdDate date DEFAULT NULL,
        modifiedDate date DEFAULT NULL,
        PRIMARY KEY (personID)
) ENGINE = INNODB, CHARACTER SET utf8mb4, COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE
    db_budgetfit.person
ADD
    CONSTRAINT FK_person_userID FOREIGN KEY (userID) REFERENCES db_budgetfit.user (userID);