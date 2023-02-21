CREATE TABLE
    db_budgetfit.user (
        userID int NOT NULL AUTO_INCREMENT,
        userName varchar(100) DEFAULT NULL,
        email varchar(100) DEFAULT NULL,
        password varbinary(100) DEFAULT NULL,
        activeUser tinyint(1) DEFAULT NULL,
        modifiedDate datetime DEFAULT NULL,
        createdDate datetime DEFAULT NULL,
        PRIMARY KEY (userID),
        UNIQUE INDEX id (userID)
) ENGINE = INNODB,
AUTO_INCREMENT = 2,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE db_budgetfit.user ADD UNIQUE INDEX email (email);

ALTER TABLE db_budgetfit.user ADD UNIQUE INDEX userName (userName);