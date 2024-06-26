-- script-lists all Comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy
-- each record should display: tv_shows.title sorted ASC
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
