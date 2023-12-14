-- List all comedy shows in the database `hbtn_0d_tvshows`

-- Each record display: <tv_shows.title>
-- Results are sorted in ascending order by the show title

SELECT tv_shows.title FROM tv_genres
       INNER JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
       INNER JOIN tv_shows
       ON tv_shows.id = tv_show_genres.show_id
       WHERE name = 'Comedy'
       ORDER BY tv_shows.title ASC
