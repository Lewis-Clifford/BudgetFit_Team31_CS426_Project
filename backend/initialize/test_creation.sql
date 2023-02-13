-- TEST initialization of schema login_schema1

-- (This is just a preliminary version that we have to change)
CREATE SCHEMA IF NOT EXISTS login_schema1;

-- stores accounts
CREATE TABLE IF NOT EXISTS login_schema1.user_login_table (
    user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL UNIQUE,
    user_pw_encrypted VARBINARY(100) NOT NULL,
    user_email VARCHAR(319) NOT NULL
    
);

-- stores the items in each user's shopping list
CREATE TABLE IF NOT EXISTS login_schema1.items_shopping_list (
    item_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, 
    items_list_id INT UNSIGNED NOT NULL,
    user_name VARCHAR(50) NOT NULL,
    shopping_item_id VARCHAR(255) NOT NULL
);

-- stores information about each existing shopping list
CREATE TABLE IF NOT EXISTS login_schema1.shopping_list_metadata (
    items_list_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    list_name VARCHAR(50) NOT NULL,
    list_length INT NOT NULL,
    list_done INT NOT NULL
);

