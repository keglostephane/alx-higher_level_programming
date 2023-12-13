-- Create a table called `first_table` in the current database
-- `first_table` description:
-- id INT
-- name VARCHAR(256)
-- the database name will be passed as an argument of the mysql command
-- if the table `first_table` already exists, don't fail.
CREATE TABLE IF NOT EXISTS first_table (
       id INT,
       name VARCHAR(256)
)
