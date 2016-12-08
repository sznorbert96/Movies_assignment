# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
        # initialize instance of class Movie
	self.title = movie_title
	self.poster_image_url = movie_poster_url
	self.trailer_youtube_url = movie_trailer_url
    def open_trailer(self):
	webbrowser.open(self.trailer_youtube_url)
    

