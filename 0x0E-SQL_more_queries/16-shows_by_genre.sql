-- lists all genres from database and displays number of shows
SELECT s.title, g.name
FROM tv_show_genres tg
INNER JOIN tv_shows s ON tg.show_id = s.id
LEFT JOIN tv_genres g ON tg.genre_id = g.id
ORDER BY s.title, g.name
