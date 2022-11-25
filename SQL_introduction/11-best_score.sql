-- lists scores and names
SELECT score,name FROM second_table
WHERE score > 10 OR score = 10
ORDER BY score DESC;
