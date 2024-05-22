-- creates the database hbtn_0d_usa and the table states on your mysql server
-- states description: id INT unique, auto generated, cant be NULL and is a primary key
--                      name VARCHAR(256) cant be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
