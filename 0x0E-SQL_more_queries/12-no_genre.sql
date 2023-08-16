-- Lists all shows without a genre linked
SELECT shows.title AS title, genres.genre_id AS genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
WHERE genres.genre_id IS NULL
ORDER BY shows.title, genres.genre_id;
