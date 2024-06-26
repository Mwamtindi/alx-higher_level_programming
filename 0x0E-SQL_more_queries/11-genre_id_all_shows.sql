-- script-lists all shows contained in the db hbtn_0d_tvshows
-- Record display: tv_shows.title - tv_show_genres.genre_id sorted ASC
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
