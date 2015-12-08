class Movie():
    """
    Represents a movie object

    Attributes:
        title: A string with the movie title.
        poster_image_url: Url of the movie's image to display in the page.
        trailer_youtube_url: Url of the movie's youtube trailer.
        release_year: An integer that represents the movie's release year.
        genres: A string with the movie's genres separated wtih commas.
        imdb_rating: A string with the movie's rating given by imdb.com.
        imdb_url: Url of the movie's site in imdb.com
    """
    def __init__(self,
                 title,
                 poster_image_url,
                 trailer_youtube_url,
                 release_year,
                 genres,
                 imdb_rating,
                 imdb_url):
        """ Inits Movie class """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year
        self.genres = genres
        self.imdb_rating = imdb_rating
        self.imdb_url = imdb_url
