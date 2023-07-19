-- lists all cities contained
SELECT c.id, c.name, s.name
FROM cities c
INNER JOIN states s ON s.id = c.state_id;
