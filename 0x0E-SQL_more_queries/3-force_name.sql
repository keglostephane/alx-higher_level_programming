-- creates the table `force_name` on MySQL server.
-- force_name description:
-- id INT
-- name VARCHAR(256) can't be null
-- database name will passed as an argument to mysql command
-- if the table `force_name` already exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
)
