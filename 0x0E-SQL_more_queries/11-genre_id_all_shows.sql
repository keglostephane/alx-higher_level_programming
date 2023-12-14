-- List all shows contained in the database `hbtn_0d_tvshows`

-- Each record display `tv_shows.title` - `tv_show_genres.genre_id`.
-- Results are sorted in ascending order by `tv_shows.title` and
-- `tv_show_genres.genre_id`.
-- If a show doesn't have a genre, display NULL.
-- Database name will be passed as argument.

SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_shows LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       ORDER BY tv_shows.title, tv_show_genres.genre_id;
