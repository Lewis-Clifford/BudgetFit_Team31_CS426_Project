-- print out a list of everyone's shopping lists
SELECT * FROM login_schema1.shopping_list_metadata;

-- print out person1's shopping lists
SELECT * FROM login_schema1.items_shopping_list
WHERE user_name = 'person1';

-- print out person2's shopping lists
SELECT * FROM login_schema1.items_shopping_list
WHERE user_name = 'person2';

