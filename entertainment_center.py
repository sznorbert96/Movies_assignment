# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes
import urllib
import json


movies = []

titles_and_links = [("Inception", "https://www.youtube.com/watch?v=8hP9D6kZseM"),("Shutter Island", "https://www.youtube.com/watch?v=lhBTlYQcBC0"),("Southpaw", "https://www.youtube.com/watch?v=Mh2ebPxhoLs")]

for title, link in titles_and_links :
	response = urllib.urlopen("http://www.omdbapi.com/?t="+ title + "&y=&plot=short&r=json")
	content = json.loads(response.read())
	poster_url = content["Poster"]
	rating = content["imdbRating"]
	movies.append(media.Movie(title, poster_url, link,rating))
 	

#print(json_file)
fresh_tomatoes.open_movies_page(movies)
