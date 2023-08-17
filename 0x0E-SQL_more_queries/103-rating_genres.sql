-- List all genres by their rating
SELECT tg.name, SUM(tr.rate) AS rating
FROM
    tv_genres AS tg
INNER JOIN
    tv_show_genres AS tsg ON tg.id = tsg.genre_id
INNER JOIN
    tv_show_ratings AS tr ON tsg.show_id = tr.show_id
GROUP BY
    tg.name
ORDER BY
    rating DESC;
