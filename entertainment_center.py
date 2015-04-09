# Full Stack ND P1: Movie Trailer Website
# by Mario Nuevo
# main file
# It creates Movie class instances and call to web creator open_movies_page

import media
import fresh_tomatoes

# lets create Movie instances
toy_story = media.Movie(
	"Toy Story",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "http://www.youtube.com/watch?v=KYz2wyBy3kc",
    "1995",
    "John Lasseter")

avatar = media.Movie(
	"Avatar",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=5PSNL1qE6VY",
    "2009",
    "James Cameron")

intouchables = media.Movie(
	"The Intouchables",
    "http://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
    "http://www.youtube.com/watch?v=R8wUIez--WE",
    "2011",
    "Eric Toledano, Olivier Nakache")

vietnam = media.Movie(
	"Good Morning Vietnam",
	"http://upload.wikimedia.org/wikipedia/en/d/d0/Good_Morning%2C_Vietnam.jpg",
	"http://www.youtube.com/watch?v=_V-O6nq92wY",
	"1987",
	"Barry Levinson")

interestellar = media.Movie(
	"Interestellar",
	"http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"http://www.youtube.com/watch?v=zSWdZVtXT7E",
	"2014",
	"Christopher Nolan")

asgood = media.Movie(
	"As Good As It Gets",
	"https://www.movieposter.com/posters/archive/main/88/MPW-44162",
	"http://www.youtube.com/watch?v=rrRl2QQKkI8",
	"1997",
	"James L. Brooks")

moviesList = [avatar, intouchables, vietnam, interestellar, asgood, toy_story]

# finally, build webpage
fresh_tomatoes.open_movies_page(moviesList)