-- lists all shows contained in hbtn_0d_tvshows
SELECT s.title, g.genre_id
FROM tv_show_genre tg
INNER JOIN tv_shows s ON tg.show_id = s.id
INNER JOIN tv_show_genres g ON tg.genre_id = g.id
ORDER BY s.title, g.genre_id;
