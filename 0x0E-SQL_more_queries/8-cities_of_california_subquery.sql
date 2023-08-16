-- Lists all the cities of California State
SELECT cities.id, cities.name
       FROM cities
       WHERE state_id IN (
       	     SELECT states.id
	     FROM states
	     WHERE name = 'California')
	ORDER BY cities.id;
