-- listing all id with california
SELECT id, name
FROM cities
WHERE state_id IN (
	SELECT id FROM states
	WHERE state_id = 'California')
ORDER BY id;
