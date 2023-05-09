-- person1 fills in the other list
INSERT INTO login_schema1.items_shopping_list (
    items_list_id, user_name, shopping_item_id
)
VALUES (77770001, 'person2', 'one singular piece of frosted flakes')
;
UPDATE login_schema1.shopping_list_metadata
SET list_length = list_length + 1
WHERE items_list_id = 12340002;

