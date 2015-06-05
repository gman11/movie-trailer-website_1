# import fresh_tomatoes
import fresh_tomatoes
# import media class
import media


# Avatar movie
avatar = media.Movie(
    "Avatar",
    "images/Avatar.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Batman movie
batman = media.Movie(
    "Batman",
    "images/Dark_knight.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# Terminator
terminator = media.Movie(
    "Terminator",
    "images/Terminator-salvation.jpg",
    "https://www.youtube.com/watch?v=-Czz-TcWCkA")

# Planet of the Apes
apes = media.Movie(
    "Dawn of the Planet of the Apes",
    "images/Dawn_of_the_Planet_of_the_Apes.jpg",
    "https://www.youtube.com/watch?v=3sHMCRaS3ao")

# Interstellar
interstellar = media.Movie(
    "Interstellar",
    "images/Interstellar.jpg",
    "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

# Mad Max: Fury Road
madMax = media.Movie(
    "Mad Max: Fury Road",
    "images/MadMax.jpg",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8")


# array of movies
movies = [avatar, batman, terminator, apes, interstellar, madMax]

# send the list of movies to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
