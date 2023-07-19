-- list all shows frp, tv shows rates
SELECT s.title, SUM(r.rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings r ON r.show_id = s.id
GROUP BY s.title
ORDER BY rating
