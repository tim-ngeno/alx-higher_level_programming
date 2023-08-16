-- Lists all the cities of California State
SELECT cities.id, cities.name
       FROM cities
       WHERE id = (
       	     SELECT states.id
	     FROM states
	     WHERE name = 'California')
	ORDER BY cities.id;
