-- the dummy users create shopping lists

-- person1 creates 2 lists
INSERT INTO login_schema1.shopping_list_metadata (
    items_list_id, user_name, list_name, list_length, list_done
)
VALUES (12340001, 'person1', 'vegetables', 0, 0);

INSERT INTO login_schema1.shopping_list_metadata (
    items_list_id, user_name, list_name, list_length, list_done
)
VALUES (12340002, 'person1', 'drinks', 0, 0);

