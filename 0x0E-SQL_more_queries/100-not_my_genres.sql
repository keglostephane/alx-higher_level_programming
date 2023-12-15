-- List all genres not linked to the show `dexter`
-- from `hbtn_0d_tvshows` database

-- Each record should display: <tv_genres.name>
-- Results must be sorted in ascending order by the genre name
-- the database name will be passed as an argument of the mysql command

SELECT name FROM tv_genres
       WHERE id NOT IN
       	     ( SELECT tv_genres.id FROM tv_shows
	       	      INNER JOIN tv_show_genres
	       	      ON tv_shows.id = tv_show_genres.show_id
	       	      INNER JOIN tv_genres
	       	      ON tv_show_genres.genre_id = tv_genres.id
	       	      WHERE tv_shows.title = 'Dexter'
		      ORDER BY tv_genres.name ASC);
