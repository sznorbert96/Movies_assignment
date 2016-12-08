# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

inception = media.Movie("Inception", "https://judgebyitscover.files.wordpress.com/2011/04/inception-poster-2.jpg", "https://www.youtube.com/watch?v=8hP9D6kZseM")

shutter_island = media.Movie("Shutter Island", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg@@._V1_UY1200_CR83,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=lhBTlYQcBC0")

southpaw = media.Movie("Southpaw", "http://pad.mymovies.it/filmclub/2015/03/252/locandina.jpg", "https://www.youtube.com/watch?v=Mh2ebPxhoLs")

movies = [inception, shutter_island, southpaw]
fresh_tomatoes.open_movies_page(movies)
