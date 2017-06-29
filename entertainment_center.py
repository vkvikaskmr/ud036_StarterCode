import media
import fresh_tomatoes

# Following are the movies that will be present on the Movie Trailer website

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come alive",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        media.Movie.VALID_RATINGS["General"])

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     media.Movie.VALID_RATINGS["Parental_Guidance"])


the_dark_knight = media.Movie("The dark Knight",
                              "Power and determination of Batman will be tested",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                              media.Movie.VALID_RATINGS["Parental_Guidance"])


inception = media.Movie("Inception",
                        "A Dream within a dream",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        media.Movie.VALID_RATINGS["General"])

memento = media.Movie("Memento",
                      "Story of a man having short term memory loss trying to avenge his wife's death",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0",
                      media.Movie.VALID_RATINGS["Restricted"])

big_hero_6 = media.Movie("Big Hero Six",
                         "Story of an intelligent kid interested in robots",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=bT8qmoCgxZg",
                         media.Movie.VALID_RATINGS["General"])

movies = [toy_story, avatar, the_dark_knight, inception, memento, big_hero_6]
fresh_tomatoes.open_movies_page(movies)
