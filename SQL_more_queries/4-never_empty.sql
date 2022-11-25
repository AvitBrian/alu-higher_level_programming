-- creates a table as well
CREATE TABLE id_not_null IF NOT EXISTS(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
