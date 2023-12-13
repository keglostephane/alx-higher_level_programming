-- List all records with a score >= 10 in the `second_table`
-- of database `hbtn_0c_0`

-- display both the score and the name
-- results are ordered by score (top first)
-- database name will be passed as ann argument of mysql command

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
