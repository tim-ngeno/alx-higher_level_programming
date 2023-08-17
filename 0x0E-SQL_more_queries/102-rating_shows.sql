-- List all shows by their rating
SELECT ts.title, SUM(tr.rate) AS rating
FROM
    tv_shows AS ts
JOIN
    tv_show_ratings AS tr ON ts.id = tr.show_id
GROUP BY
    ts.title
ORDER BY
    rating DESC;
