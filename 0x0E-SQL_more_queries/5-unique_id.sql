-- Creates the table `unique_id` on MySQl server
-- `unique_id` description:
-- id INT with default value 1 and must be unique
-- name VARCHAR(256)
-- database name will be passed as an argument of mysql command
-- if table `unique_id` already exists, script should fail

CREATE TABLE IF NOT EXISTS unique_id (
       id INT default 1 UNIQUE,
       name VARCHAR(256)
)
