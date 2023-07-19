-- lists all genres from database and displays number of shows
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres tg
INNER JOIN tv_shows s ON tg.show_id = s.id
INNER JOIN tv_genre g ON tg.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows
