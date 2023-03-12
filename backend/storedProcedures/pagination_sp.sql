#Needs to be tested -Cliff 

CREATE DEFINER =`CLIFF`@`%` PROCEDURE `PAGINATION`(
IN offset_value INT, IN records_per_page INT) BEGIN 
	SELECT
item_name,
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
	LIMIT records_per_page
	OFFSET offset_value;
	END 
