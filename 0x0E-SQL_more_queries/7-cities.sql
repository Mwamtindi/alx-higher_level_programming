--  creates db hbtn_0d_usa and the table cities('id' INT unique auto 
-- generated notnull PK,'state_id' INT notnull FK, 'name' VARCHAR(256))
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.`cities` (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (`state_id`)
	REFERENCES hbtn_0d_usa.`states`(`id`)

);
