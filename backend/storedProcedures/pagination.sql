--Author: Kaden Nesch
-- This stored procedure deals with the master search as well as pagination in the program.
-- The master search includes sorting things by asc/desc price, min/max price, categories, user search, and items dislayed per page.
-- This also allows the pagination to work properly do display every item in seperate pages.

CREATE DEFINER=`root`@`localhost` PROCEDURE `pagination`(
    IN sort_order VARCHAR(10), 
    IN records_per_page INT, 
    IN page_number INT, 
    IN min_price DECIMAL(10,2), 
    IN max_price DECIMAL(10,2), 
    IN categories_list TEXT,
    IN search_term VARCHAR(255)
)
BEGIN
    DECLARE offset_value INT DEFAULT 0;
    SET offset_value = (page_number - 1) * records_per_page;

    SELECT COUNT(*) INTO @total_records 
FROM products 
WHERE item_price >= min_price 
    AND item_price <= max_price 
    AND (FIND_IN_SET(item_category, categories_list) > 0 OR categories_list = '')
    AND (item_name LIKE CONCAT('%', search_term, '%') OR brand_name LIKE CONCAT('%', search_term, '%'));

SELECT item_name,
       productsID,
       item_category,
       brand_name,
       item_price,
       images_front_full_url,
       nf_ingredient_statement,
       nf_calories,
       nf_calories_from_fat,
       nf_total_fat,
       nf_saturated_fat,
       nf_trans_fatty_acid,
       nf_polyunsaturated_fat,
       nf_monounsaturated_fat,
       nf_cholesterol,
       nf_sodium,
       nf_total_carbohydrate,
       nf_dietary_fiber,
       nf_sugars,
       nf_protein,
       nf_vitamin_a_dv,
       nf_vitamin_c_dv,
       nf_calcium_dv,
       nf_iron_dv,
       nf_potassium,
       nf_servings_per_container,
       nf_serving_size_qty,
       nf_serving_size_unit,
       nf_serving_weight_grams,
       metric_qty,
       metric_uom
FROM products 
WHERE item_price >= min_price 
    AND item_price <= max_price 
    AND (FIND_IN_SET(item_category, categories_list) > 0 OR categories_list = '')
    AND (item_name LIKE CONCAT('%', search_term, '%') OR brand_name LIKE CONCAT('%', search_term, '%'))
ORDER BY 
    CASE WHEN sort_order = 'asc' THEN item_price END ASC,
    CASE WHEN sort_order = 'desc' THEN item_price END DESC,
    CASE WHEN sort_order = 'def' THEN productsID END ASC
LIMIT records_per_page
OFFSET offset_value;

END