-- person1 can delete all of their shopping lists at once
DELETE FROM login_schema1.items_shopping_list
WHERE items_list_id = 12340001
;
DELETE FROM login_schema1.shopping_list_metadata
WHERE items_list_id = 12340001;

DELETE FROM login_schema1.items_shopping_list
WHERE items_list_id = 12340002
;
DELETE FROM login_schema1.shopping_list_metadata
WHERE items_list_id = 12340002;

