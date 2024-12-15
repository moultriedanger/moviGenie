DROP TABLE IF EXISTS all_movies;
DROP TABLE IF EXISTS all_reviews;

CREATE TABLE all_movies (movie_id INTEGER NOT NULL PRIMARY KEY, title TEXT NOT NULL, overview TEXT NOT NULL, poster TEXT NOT NULL, vote FLOAT NOT NULL, release_date TEXT NOT NULL);

CREATE TABLE all_reviews (movie_id INTEGER NOT NULL, username TEXT NOT NULL,  rating FLOAT NOT NULL, review TEXT NOT NULL);