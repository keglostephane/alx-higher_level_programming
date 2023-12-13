-- Creates the table `id_not_null` on MySQL server.
-- `id_not_null` description:
-- id INT with default value 1
-- name VARCHAR(256)
-- database name will be passed as an argument to mysql command
-- if `id_not_null` already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT default 1,
       name VARCHAR(256)
)
