-- Displays the max temperatures of each states ordered by state name
-- database name will be passed as argument to mysql command.

SELECT state,
       MAX(value) AS max_temp FROM temperatures
       GROUP BY state
       ORDER BY state
