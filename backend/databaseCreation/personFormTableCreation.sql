CREATE TABLE
    db_budgetfit.personform (
        personFormID int NOT NULL,
        personID int DEFAULT NULL COMMENT 'Foreign Key',
        name varchar(100) DEFAULT NULL,
        heightFeet int DEFAULT NULL,
        heightInches int DEFAULT NULL,
        birthday date DEFAULT NULL,
        phoneNumber varchar(20) DEFAULT NULL,
        gender varchar(100) DEFAULT NULL,
        weight decimal(8, 2) DEFAULT NULL,
        workoutExp int DEFAULT NULL,
        fitnessLevel int DEFAULT NULL,
        createDate datetime DEFAULT NULL,
        modifiedDate datetime DEFAULT NULL,
        PRIMARY KEY (personFormID)
    ) ENGINE = INNODB,
    CHARACTER SET utf8mb4,
    COLLATE utf8mb4_0900_ai_ci,
    COMMENT = 'Reference Table: Getters Only';

ALTER TABLE
    db_budgetfit.personform
ADD
    CONSTRAINT FK_personform_personID FOREIGN KEY (personID) REFERENCES db_budgetfit.person (personID);