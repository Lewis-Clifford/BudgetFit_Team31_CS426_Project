CREATE TABLE
    db_budgetfit.items (
        itemID int NOT NULL AUTO_INCREMENT,
        name varchar(100) DEFAULT NULL,
        price decimal(2, 2) DEFAULT NULL,
        typeID int DEFAULT NULL COMMENT 'Foreign Key',
        isActive tinyint(1) DEFAULT NULL,
        createdDate datetime DEFAULT NULL,
        modifiedDate datetime DEFAULT NULL,
        calorieCount int DEFAULT NULL,
        PRIMARY KEY (itemID)
) ENGINE = INNODB, CHARACTER SET utf8mb4, COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE db_budgetfit.items
ADD
    CONSTRAINT FK_items_typeID2 FOREIGN KEY (typeID) REFERENCES db_budgetfit.types (typeID);