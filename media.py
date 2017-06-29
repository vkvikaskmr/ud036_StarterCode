
class Movie():
    
    """This class is used to store and display Movie related informations"""
    
    VALID_RATINGS = {"General":"G","Parental_Guidance":"PG","Parents_Strongly_Cautioned":"PG-13","Restricted":"R"}
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
