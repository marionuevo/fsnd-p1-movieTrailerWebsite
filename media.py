# Full Stack ND P1: Movie Trailer Website
# by Mario Nuevo
# media module
# It contains Movie class definition

import webbrowser

class Movie():
    """This class defines the properties and methods that Movie instances will have.

    No attributes.
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)