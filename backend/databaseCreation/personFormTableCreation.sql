CREATE TABLE
    db_budgetfit.personform (
        personFormID INT NOT NULL AUTO_INCREMENT,
        userID INT DEFAULT NULL COMMENT 'Foreign Key',
        heightFeet INT DEFAULT NULL,
        heightInches INT DEFAULT NULL,
        birthday DATE DEFAULT NULL,
        phoneNumber VARCHAR(20) DEFAULT NULL,
        gender VARCHAR(100) DEFAULT NULL,
        weight DECIMAL(8, 2) DEFAULT NULL,
        workoutExp INT DEFAULT NULL,
        fitnessLevel INT DEFAULT NULL,
        createdDate DATETIME DEFAULT NULL,
        modifiedDate DATETIME DEFAULT NULL,
        isActive TINYINT(1) DEFAULT NULL,
        name VARCHAR(100) DEFAULT NULL,
        allergy VARCHAR(255) DEFAULT NULL,
        diet VARCHAR(255) DEFAULT NULL,
        profileImage VARCHAR(255) DEFAULT NULL,
        lastName VARCHAR(100) DEFAULT NULL,
        userAllergy VARCHAR(100) DEFAULT NULL, 
PRIMARY KEY (personFormID) 
) ENGINE = INNODB, AUTO_INCREMENT = 3, 
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci,
COMMENT = 'Reference Table: Getters Only';

ALTER TABLE
    db_budgetfit.personform
ADD
    CONSTRAINT FK_personform_userID FOREIGN KEY (userID) REFERENCES db_budgetfit.user(userID);