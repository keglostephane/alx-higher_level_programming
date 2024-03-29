-- List all shows without the genre Comedy in the database `hbtn_0d_tvshows`

-- Each record should display: <tv_shows.title>
-- Results must be sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command

SELECT title FROM tv_shows
       WHERE id NOT IN
       	     ( SELECT tv_shows.id FROM tv_shows
	       	      LEFT JOIN tv_show_genres
		      ON tv_shows.id = tv_show_genres.show_id
	       	      LEFT JOIN tv_genres
		      ON tv_show_genres.genre_id = tv_genres.id
	     	      WHERE tv_genres.name = 'Comedy')
	ORDER BY title ASC;
