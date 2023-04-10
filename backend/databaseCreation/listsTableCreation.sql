CREATE TABLE
    db_budgetfit.lists (
        listID INT NOT NULL AUTO_INCREMENT,
        userID INT DEFAULT NULL,
        productsID INT DEFAULT NULL,
        listNUM INT DEFAULT NULL,
        listName VARCHAR(100) DEFAULT NULL,
        createdDate DATETIME DEFAULT NULL,
        modifiedDate DATETIME DEFAULT NULL,
        PRIMARY KEY (listID)
    ) ENGINE = INNODB,
    CHARACTER SET utf8mb4,
    COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE db_budgetfit.lists
ADD
    CONSTRAINT FK_lists_productsID FOREIGN KEY (productsID) REFERENCES db_budgetfit.products(productsID) ON DELETE
SET NULL;

ALTER TABLE db_budgetfit.lists
ADD
    CONSTRAINT FK_lists_userID FOREIGN KEY (userID) REFERENCES db_budgetfit.user(userID) ON DELETE
SET NULL;