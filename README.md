# Full Stack ND P1: Movie Trailer Website

This is the 1st project of the FullStack Web Developer Nanodegree at Udacity.

The goal for this project was to build a Movie Trailer Website where users can see my favorite movies and watch the trailers. I wrote the server side code to store a list of movie titles, poster images, and movie trailer URLs. Additionally, I added release year and directors name.

## Content

- `media.py`: Class Movie definitions.
- `entertainment_center.py`: This is the main file. It creates several instances of Movie.
- `fresh_tomatoes`: Additional resource file used to build the HTML page.

## Quick start

Several quick start options are available:

- [Download the latest release](https://github.com/marionuevo/fsnd-p1-movieTrailerWebsite/archive/master.zip).
- Clone the repo: `git clone https://github.com/marionuevo/fsnd-p1-movieTrailerWebsite.git`.

Then, run `python entertainment_center.py` and a browser will be launched contaning the Website containing generated index.html file.

Alternatively, you could view a live demo of this project [here]().

## Usage

Browse the different movies and click over a movie in order to watch its trailer.

### Custom changes done beyond requested features

- Added modal fade.
- Added radial gradient background.
- Added transparent (rgba) hover effect.
- Changed to Open Sans font, loaded using javascript to not block content loading.
- Added extra Movie fields: director, year.
- Changed generated HTML file to `index.html`.