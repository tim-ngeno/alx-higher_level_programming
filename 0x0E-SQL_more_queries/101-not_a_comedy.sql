-- Lists all shows without the genre comedy
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
SELECT ts1.id
FROM tv_shows ts1
INNER JOIN tv_show_genres tsg
ON ts1.id = tsg.show_id

LEFT JOIN tv_genres tg
ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy' )
ORDER BY ts.title ASC;
