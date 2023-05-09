-- person2 can delete only one particular shopping list
DELETE FROM login_schema1.items_shopping_list
WHERE items_list_id = 77770001
;
DELETE FROM login_schema1.shopping_list_metadata
WHERE items_list_id = 77770001;

