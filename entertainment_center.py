from fresh_tomatoes import open_movies_page
from media import Movie

# Make a list of class Movie(s)
movieList = []
movieList.append(Movie(
    "Gladiator",
    "https://www.movieposter.com/posters/archive/main/42/MPW-21199",
    "https://www.youtube.com/watch?v=uwTKRz-WmHU",
    2000,
    "Action, Drama",
    "8.5",
    "http://www.imdb.com/title/tt0172495/"))
movieList.append(Movie(
    "Fight Club",
    "http://bit.ly/1NSGlhl",
    "https://www.movieposter.com/posters/archive/main/67/MPW-33589",
    1999,
    "Drama",
    "8.9",
    "http://www.imdb.com/title/tt0137523/"))
movieList.append(Movie(
    "Inception",
    "http://www.mattsmoviereviews.net/Images/inceptionposter03.jpg",
    "https://www.youtube.com/watch?v=8hP9D6kZseM",
    2010,
    "Action, Mystery, Sci-Fi",
    "8.8",
    "http://www.imdb.com/title/tt1375666/"))
movieList.append(Movie(
    "The Matrix",
    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",
    1999,
    "Action, Sci-Fi",
    "8.7",
    "http://www.imdb.com/title/tt0133093/"))
movieList.append(Movie(
    "The Dark Knight",
    "http://www.wildbluffmedia.com/wp-content/uploads/2008/04/dk_posters_03.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY",
    2008,
    "Action, Crime, Drama",
    "9.0",
    "http://www.imdb.com/title/tt0468569/"))

# Call open_movies_page function to launch the browser
open_movies_page(movieList)
