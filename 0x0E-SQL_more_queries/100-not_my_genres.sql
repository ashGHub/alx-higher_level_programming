-- list all genres not linked to show Dexter
SELECT g.name
FROM tv_show_genres tg
INNER JOIN tv_shows s ON tg.show_id = s.id
LEFT JOIN tv_genres g ON tg.genre_id = g.id
WHERE s.title <> 'Dexter'
ORDER BY g.name
