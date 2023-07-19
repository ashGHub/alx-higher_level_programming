-- lists all genres from database and displays number of shows
SELECT g.name
FROM tv_show_genres tg
INNER JOIN tv_shows s ON tg.show_id = s.id
INNER JOIN tv_genres g ON tg.genre_id = g.id
WHERE s.title = 'Dexter'
GROUP BY g.name
ORDER BY name
