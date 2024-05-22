-- Use hbtn_0d_tvshows db to list all genres not link to the show Dexter
-- table contains only one record where title = Dexter
-- Each record should display: tv_genres.name sorted ASC.
SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT genre_id FROM tv_show_genres
	WHERE show_id = (
		SELECT id FROM tv_shows WHERE title = 'Dexter'
	)
)
ORDER BY tv_genres.name ASC;
