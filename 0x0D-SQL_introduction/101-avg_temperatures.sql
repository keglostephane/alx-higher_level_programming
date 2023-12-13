-- Displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending).
-- Database name will be passed as an argument of mysql command.

SELECT city, AVG(value) AS avg_temp FROM temperatures
       GROUP BY city
       ORDER BY avg_temp DESC
