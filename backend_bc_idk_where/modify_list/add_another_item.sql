-- person1 adds an item to the first list
INSERT INTO login_schema1.items_shopping_list (
    items_list_id, user_name, shopping_item_id
)
VALUES (12340001, 'person1', 'Tomato')
;
UPDATE login_schema1.shopping_list_metadata
SET list_length = list_length + 1
WHERE items_list_id = 12340001;

