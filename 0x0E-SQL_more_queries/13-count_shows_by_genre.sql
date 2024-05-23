-- script-lists all genres from hbtn_0d_tvshows displays number of shows
-- record display:<TV Show genre> - <Number of shows linked to this genre>
-- 1st clmn must be called genre, 2nd clmn must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked sorted DESC
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
