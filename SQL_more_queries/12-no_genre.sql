-- lists all shows contained
SELECT t.title, tg.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tg
ON t.id = tg.show_id
WHERE tg.genre_id IS NULL
ORDER BY t.title, tg.genre_id;

