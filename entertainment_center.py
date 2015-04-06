# Full Stack ND P1: Movie Trailer Website
# by Mario Nuevo
# main file
# It creates Movie class instances and call to web creator open_movies_page

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
					"http://upload.wikipedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					"http://www.youtube.com/watch?v=-9ceBgWV8io")

intouchables = media.Movie("Intouchables",
						"http://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
						"https://www.youtube.com/watch?v=R8wUIez--WE")

moviesList = [toy_story, avatar, intouchables]
# , vietnam, interestellar, asgood

fresh_tomatoes.open_movies_page(moviesList)