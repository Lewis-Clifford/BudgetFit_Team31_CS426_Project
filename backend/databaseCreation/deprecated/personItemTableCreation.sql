CREATE TABLE
    db_budgetfit.personitems (
        personItemID int NOT NULL AUTO_INCREMENT,
        personID int DEFAULT NULL,
        itemID int DEFAULT NULL,
        itemListTypeID int DEFAULT NULL,
        isActive tinyint(1) DEFAULT NULL,
        createdDate datetime DEFAULT NULL,
        modifiedDate datetime DEFAULT NULL,
        PRIMARY KEY (personItemID)
) ENGINE = INNODB, CHARACTER SET utf8mb4, COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE
    db_budgetfit.personitems
ADD
    CONSTRAINT FK_personitems_itemID2 FOREIGN KEY (itemID) REFERENCES db_budgetfit.items (itemID);

ALTER TABLE
    db_budgetfit.personitems
ADD
    CONSTRAINT FK_personitems_itemListTypeID2 FOREIGN KEY (itemListTypeID) REFERENCES db_budgetfit.itemlisttype (itemListTypeID);

ALTER TABLE
    db_budgetfit.personitems
ADD
    CONSTRAINT FK_personitems_personID2 FOREIGN KEY (personID) REFERENCES db_budgetfit.person (personID);