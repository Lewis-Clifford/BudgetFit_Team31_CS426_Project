-- person1 goes shopping again
-- person1 marks off both items on the 1-item list
UPDATE login_schema1.shopping_list_metadata
SET list_done = 1
WHERE items_list_id = 12340002;

