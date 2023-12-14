-- List all cities of California that can be found in the database `hbtn_0d_usa`
-- Results must be sorted in ascending order by cities.id
-- database name will be passed as an argument to mysql command

SELECT id, name FROM cities
       WHERE cities.state_id = (
       	     SELECT id FROM states WHERE name = 'California')
	     ORDER BY cities.id ASC
