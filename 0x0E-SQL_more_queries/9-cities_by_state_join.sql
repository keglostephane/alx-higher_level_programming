-- List all cities in the database `hbtn_0d_usa`
-- Each record displays `cities.id` - `cities.name` - `states.name`
-- Results are sorted in ascending order by `cities.id`
-- Database name will be passed as an argument to mysql command

SELECT cities.id, cities.name, states.name
       FROM cities INNER JOIN states
       ON cities.state_id = states.id;
