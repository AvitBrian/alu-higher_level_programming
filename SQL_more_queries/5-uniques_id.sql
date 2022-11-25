-- create a table too
CREATE TABLE unique_id IF NOT EXISTS(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
