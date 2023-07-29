from collections import defaultdict

import pytest

from directors import (get_movies_by_director, get_average_scores,
                       calc_mean_score, Movie)


@pytest.fixture(scope="module")
def movies():
    return get_movies_by_director()


@pytest.fixture(scope="module")
def scores(movies):
    return get_average_scores(movies)


def test_get_movies_by_director(movies):
    assert 'Sergio Leone' in movies
    assert len(movies['Sergio Leone']) == 4
    assert len(movies['Peter Jackson']) == 12


def test_director_movies_data_structure(movies):
    assert type(movies) in (dict, defaultdict)
    assert type(movies['Peter Jackson']) == list
    assert type(movies['Peter Jackson'][0]) == Movie


def test_calc_mean_score(movies):
    movies_sergio = movies['Sergio Leone']
    movies_nolan = movies['Christopher Nolan']
    assert calc_mean_score(movies_sergio) == 8.5
    assert calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores_top_directors(scores):
    expected = [('Sergio Leone', 8.5),
                ('Christopher Nolan', 8.4),
                ('Quentin Tarantino', 8.2),
                ('Hayao Miyazaki', 8.2),
                ('Frank Darabont', 8.0),
                ('Stanley Kubrick', 8.0),
                ('James Cameron', 7.9),
                ('Joss Whedon', 7.9)]
    assert scores[0:8] == expected


@pytest.mark.parametrize("director", [
    'Quentin Tarantino', 'Hayao Miyazaki',
    'Frank Darabont', 'Stanley Kubrick',
    'James Cameron', 'Joss Whedon',
    'Alejandro G. Iñárritu',
])
def test_director_in_top_scores(director, scores):
    # order / score might slightly change depending the way the mean
    # is calculated so only test director names in top scores
    top_scores = scores[2:13]
    directors = {score[0] for score in top_scores}
    assert director in directors


def test_ignore_older_movies(movies):
    """Lowell Sherman's Black and White is from 1933 and should
       be skipped"""
    assert len(movies["Lowell Sherman"]) == 0