# Full Stack ND P1: Movie Trailer Website
# by Mario Nuevo
# main file
# It creates Movie class instances and call to web creator open_movies_page

import media
import fresh_tomatoes

toy_story = media.Movie(
	"Toy Story",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
	"Avatar",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

intouchables = media.Movie(
	"Intouchables",
    "http://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
    "https://www.youtube.com/watch?v=R8wUIez--WE")

vietnam = media.Movie(
	"Good Morning Vietnam",
	"http://upload.wikimedia.org/wikipedia/en/d/d0/Good_Morning%2C_Vietnam.jpg",
	"https://www.youtube.com/watch?v=_V-O6nq92wY")

interestellar = media.Movie(
	"Interestellar",
	"http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=zSWdZVtXT7E")

asgood = media.Movie(
	"As Good As It Gets",
	"http://upload.wikimedia.org/wikipedia/en/d/dc/As_good_as_it_gets.jpg",
	"https://www.youtube.com/watch?v=rrRl2QQKkI8")

moviesList = [avatar, intouchables, vietnam, interestellar, asgood, toy_story]

fresh_tomatoes.open_movies_page(moviesList)