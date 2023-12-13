-- List all records of the table `second_table` of database `hbtn_0c_0`

-- Don't list rows without a `name` value
-- Display the score and the name
-- Lists records by descending score
-- database name will be passed as an argument to mysql command

SELECT score, name FROM second_table
       WHERE name IS NOT NULL
       ORDER BY score DESC
