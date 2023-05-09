
#Author: Cliff Lewis
#Purpose: This table is a join table combining product numbers with the list they are assigned to.
#   It has a many-to-one relationship from the lists table to the products table and 
#   a many-to-one relationship from the lists table to the user table
CREATE TABLE
    db_budgetfit.lists (
        listID INT NOT NULL AUTO_INCREMENT,
        userID INT DEFAULT NULL,
        productsID INT DEFAULT NULL,
listName VARCHAR(100) DEFAULT NULL,
createdDate DATETIME DEFAULT NULL,
modifiedDate DATETIME DEFAULT NULL,
priority VARCHAR(20) DEFAULT NULL,
description VARCHAR(255) DEFAULT NULL,
quantity INT DEFAULT NULL,
allergy TINYINT DEFAULT NULL, diet TINYINT DEFAULT NULL, 
PRIMARY KEY (listID) 
) ENGINE = INNODB, AUTO_INCREMENT = 13, AVG_ROW_LENGTH = 2340, 
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