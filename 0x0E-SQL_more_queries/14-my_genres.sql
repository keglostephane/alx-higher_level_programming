-- List all genres of the show `Dexter` using `hbtn_0d_tvshows` database

-- Each record shoud display: <tv_genres.name>
-- Results must be sorted in ascending order by the genre name
-- The database name will be passed as an argument

SELECT tv_genres.name
       FROM tv_shows
       INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
       INNER JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
       WHERE tv_shows.title = 'Dexter';
