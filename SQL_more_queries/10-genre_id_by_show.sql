-- lists all shows that have atleast one genre linked
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id;
