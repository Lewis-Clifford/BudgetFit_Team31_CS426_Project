CREATE DEFINER =`CLIFF`@`%` PROCEDURE `GETUSERLIST`
(IN _USERID INT, IN _LISTNAME VARCHAR(100)) BEGIN 
	START TRANSACTION;

SELECT
    products.item_name,
    products.productsID,
    products.item_category,
    products.brand_name,
    products.item_price,
    products.images_front_full_url,
    products.nf_ingredient_statement,
    products.nf_calories,
    products.nf_calories_from_fat,
    products.nf_total_fat,
    products.nf_saturated_fat,
    products.nf_trans_fatty_acid,
    products.nf_polyunsaturated_fat,
    products.nf_monounsaturated_fat,
    products.nf_cholesterol,
    products.nf_sodium,
    products.nf_total_carbohydrate,
    products.nf_dietary_fiber,
    products.nf_sugars,
    products.nf_protein,
    products.nf_vitamin_a_dv,
    products.nf_vitamin_c_dv,
    products.nf_calcium_dv,
    products.nf_iron_dv,
    products.nf_potassium,
    products.nf_servings_per_container,
    products.nf_serving_size_qty,
    products.nf_serving_size_unit,
    products.nf_serving_weight_grams,
    products.metric_qty,
    products.metric_uom,
    l.priority,
    l.description,
    l.listName,
l.quantity, l.allergy, l.diet 
FROM lists l
    INNER JOIN products ON l.productsID = products.productsID
WHERE
    l.listName = _listName
    AND l.userID = _userID
    AND l.quantity > 0;

COMMIT;
END 