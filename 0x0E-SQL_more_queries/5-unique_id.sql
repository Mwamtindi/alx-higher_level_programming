-- creates table unique_id('id' INT value 1 unique, name VARCHAR(256))
CREATE TABLE IF NOT EXISTS `unique_id` (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
