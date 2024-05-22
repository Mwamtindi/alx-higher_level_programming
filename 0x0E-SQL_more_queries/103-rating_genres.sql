-- a script-lists all genres in db hbtn_0d_tvshows_rate by their rating
-- each record should display: tv_genres.name - rating sum sorted in desc
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
