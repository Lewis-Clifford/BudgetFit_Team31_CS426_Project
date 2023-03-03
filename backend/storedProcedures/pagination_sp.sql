--Needs to be tested -Cliff

CREATE DEFINER =`CLIFF`@`%` PROCEDURE `PAGINATION`(
IN PG_NUMBER INT, IN RECORDS_PER_PAGE INT) BEGIN 
	DECLARE offset_value int;
	SET offset_value = records_per_page * pg_number;
	SELECT
	    i.name,
	    i.price,
	    i.calorieCount,
	    i.typeID
	FROM items i
	    INNER JOIN types t ON i.typeID = t.typeID
	LIMIT records_per_page
	OFFSET offset_value;
	END 
