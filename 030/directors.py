import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    movies_per_directors = defaultdict(list)

    with open(MOVIE_DATA, mode='r', newline='', encoding='utf-8', errors='ignore') as csvfile:
        movies = csv.DictReader(csvfile)

        for movie in movies:

            title = movie['movie_title']
            year = int(movie['title_year']) if movie['title_year'].isnumeric() else 0
            score = float(movie['imdb_score'])

            if year >= MIN_YEAR:
                movies_per_directors[movie['director_name']].append(
                    Movie(
                        title, 
                        year, 
                        score
                    )
                )

    return movies_per_directors


def calc_mean_score(movies: list[Movie]):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    
    n_movies = len(movies)
    total_score = sum(movie.score for movie in movies)
    return round(total_score / n_movies, 1)


def get_average_scores(directors: dict[str, list[Movie]]):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    
    directors_scores = list()

    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            directors_scores.append(
                tuple([
                    director,
                    calc_mean_score(movies)
                ])
            )

    return sorted(directors_scores, key=lambda x: x[1], reverse=True)
