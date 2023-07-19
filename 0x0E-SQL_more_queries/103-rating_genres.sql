-- list all genres by rating
SELECT g.name, SUM(r.rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings r ON r.show_id = s.id
INNER JOIN tv_show_genres tg ON tg.show_Id = s.id
INNER JOIN tv_genres g ON tg.genre_id = g.id
GROUP BY g.name
ORDER BY rating
