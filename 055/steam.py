from collections import namedtuple
from webbrowser import get

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games = feedparser.parse(FEED_URL)
    games_collection = list()
    for game in  games['entries']:

        games_collection.append(
            Game(
                game['title'],
                game['link']
            )
        )

    return games_collection