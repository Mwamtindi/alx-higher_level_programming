-- script-lists all shows in hbtn_0d_tvshows without a genre linked
-- record display: tv_shows.title - tv_show_genres.genre_id sorted ASC
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
