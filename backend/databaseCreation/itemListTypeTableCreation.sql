CREATE TABLE
    db_budgetfit.itemlisttype (
        itemListTypeID int NOT NULL,
        listType varchar(100) DEFAULT NULL,
        PRIMARY KEY (itemListTypeID)
    ) ENGINE = INNODB,
    CHARACTER SET utf8mb4,
    COLLATE utf8mb4_0900_ai_ci,
    COMMENT = 'Reference Table: Getters Only';