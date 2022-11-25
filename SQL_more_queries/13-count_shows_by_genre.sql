-- list all genres from the database
SELECT g.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tg
ON g.id = tg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
