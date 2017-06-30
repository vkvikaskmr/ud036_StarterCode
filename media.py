
class Movie():
    """This class is used to store and display Movie related informations"""

    VALID_RATINGS = {
        "General": "G",
        "Parental_Guidance": "PG",
        "Parents_Strongly_Cautioned": "PG-13",
        "Restricted": "R"
        }

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            rating):
        """:param movie_title: title of the movie
        :param movie_storyline: a small description about the movie
        :param poster_image: url of the movie poster
        :param trailer_youtube: youtuble link to the movie trailer
        :param rating: preferred audience of the movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
