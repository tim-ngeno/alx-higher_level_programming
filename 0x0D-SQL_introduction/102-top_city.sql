-- Displays top 3 cities' temperatures in month 7 and 8
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR MONTH = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
