-- list sll shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT tv_shows.title, tv_shows_genres.genre.id
FROM tv_shows
INNER JOIN tv_shows_genres
ON tv_shows.id=tv_shows_genres.show_id
0RDER BY tv_shows.title, tv_show_genres.genre_id;
