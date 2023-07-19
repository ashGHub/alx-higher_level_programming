-- list all shows without the genre Comedy
SELECT s.title
FROM tv_show_genres tg
INNER JOIN tv_shows s ON tg.show_id = s.id
INNER JOIN tv_genres g ON tg.genre_id = g.id
WHERE g.name <> 'Comedy'
ORDER BY s.title
