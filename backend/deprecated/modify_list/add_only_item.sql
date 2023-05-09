-- person2 fills in an item in their only list
INSERT INTO login_schema1.items_shopping_list (
    items_list_id, user_name, shopping_item_id
)
VALUES (12340002, 'person1', 'Dr Pepper 2L')
;
UPDATE login_schema1.shopping_list_metadata
SET list_length = list_length + 1
WHERE items_list_id = 77770001;

