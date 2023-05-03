CREATE DEFINER=`cliff`@`%` PROCEDURE `allergyQuery`(IN _userID INT, IN _productsID INT)
BEGIN
  DECLARE allergy VARCHAR(255);
  DECLARE diet VARCHAR(255);
  DECLARE ingredients TEXT;
  DECLARE productName VARCHAR(100);
  DECLARE userAllergy VARCHAR(100);
  DECLARE flag TINYINT;
  SET flag = 0; #flag for setting to zero if allergy or diet removed from form
    SELECT p.allergy, p.diet, p.userAllergy FROM personform p WHERE p.userID = _userID INTO allergy, diet, userAllergy;
    SELECT pd.item_name, pd.nf_ingredient_statement FROM products pd WHERE pd.productsID = _productsID INTO productName, ingredients;
    SELECT userAllergy;
#Allergy Checks
    IF LOCATE('Peanut', allergy) > 0 THEN
      IF productName RLIKE ('peanut') OR ingredients RLIKE ('peanut') THEN
        UPDATE lists SET lists.allergy =  1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Dairy', allergy) > 0 THEN
      IF productName RLIKE ('cheese|yogurt|milk|cream|smoothie|shake|chocolate|butter') OR ingredients RLIKE ('cheese|yogurt|milk|cream|smoothie|shake|chocolate|butter') THEN
        UPDATE lists SET lists.allergy =  1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Gluten', allergy) > 0 THEN
      IF productName RLIKE ('rolls|toaster|bagel|bread|flour|pie|cake') OR ingredients RLIKE ('rolls|toaster|bagel|bread|flour|pie|cake') THEN
        UPDATE lists SET lists.allergy = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE ('Eggs', allergy) > 0 THEN
      IF productName RLIKE ('egg') OR ingredients RLIKE ('egg') THEN
        UPDATE lists SET lists.allergy = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Soy', allergy) > 0 THEN
      IF productName RLIKE ('soy') OR ingredients RLIKE ('soy') THEN
        UPDATE lists SET lists.allergy = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Fish', allergy) > 0 THEN
      IF productName RLIKE ('fish|salmon|halibut|tuna') OR ingredients RLIKE ('fish|salmon|halibut|tuna') THEN
        UPDATE lists SET lists.allergy = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Crustaceans', allergy) > 0 THEN
      IF productName RLIKE ('crab|lobster|clam|mussel|scallop|shellfish') OR ingredients RLIKE ('crab|lobster|clam|mussel|scallop|shellfish') THEN
        UPDATE lists SET lists.allergy = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF userAllergy IS NOT NULL THEN
      IF productName RLIKE (TRIM(userAllergy)) OR ingredients RLIKE (TRIM(userAllergy)) THEN
        UPDATE lists SET lists.allergy = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF flag = 0 THEN
     UPDATE lists SET lists.allergy = 0 WHERE lists.userID = _userID AND lists.productsID = _productsID;
    END IF;
#Diet Checks
    SET flag = 0;
    IF LOCATE('Keto', diet) > 0 THEN
      SELECT products.nf_total_carbohydrate FROM products WHERE products.productsID = _productsID INTO @carbs;
      IF @carbs > 20 THEN
        UPDATE lists SET lists.diet =  1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Vegetarian', diet) > 0 THEN
      IF productName RLIKE ('beef|chicken|steak|sausage|pancetta|meat|ham|pork|salmon|halibut|tuna|fish') OR ingredients RLIKE ('beef|chicken|steak|sausage|pancetta|meat|ham|pork|salmon|halibut|tuna|fish') THEN
        UPDATE lists SET lists.diet = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Vegan', diet) > 0 THEN
      IF productName RLIKE ('beef|chicken|steak|sausage|pancetta|meat|ham|pork|salmon|halibut|tuna|fish|cheese|yogurt|milk|cream|smoothie|shake|chocolate|butter')
      OR ingredients RLIKE ('beef|chicken|steak|sausage|pancetta|meat|ham|pork|salmon|halibut|tuna|fish|cheese|yogurt|milk|cream|smoothie|shake|chocolate|butter') THEN
        UPDATE lists SET lists.diet = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Pescatarian', diet) > 0 THEN
      IF productName RLIKE ('beef|chicken|steak|sausage|pancetta|meat|ham|pork|cheese|yogurt|milk|cream|smoothie|shake|chocolate|butter')
      OR ingredients RLIKE ('beef|chicken|steak|sausage|pancetta|meat|ham|pork|cheese|yogurt|milk|cream|smoothie|shake|chocolate|butter') THEN
        UPDATE lists SET lists.diet = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;
    IF LOCATE('Low Sodium', diet) > 0 THEN
      SELECT products.nf_sodium FROM products WHERE products.productsID = _productsID INTO @sodium;
      IF @sodium > 200 THEN
        UPDATE lists SET lists.diet = 1 WHERE lists.userID = _userID AND lists.productsID = _productsID;
        SET flag = 1;
      END IF;
    END IF;

    IF flag = 0 THEN
     UPDATE lists SET lists.diet = 0 WHERE lists.userID = _userID AND lists.productsID = _productsID;
    END IF;
END