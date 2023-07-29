from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content: str):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    
    words_per_char = defaultdict(Counter)

    for line in content.split('\n')[1:]:

        if not line:
            continue 

        if line == '"':
            continue
        
        if not line[0].isnumeric():
            words_per_char[char].update({episode: len(line.split())})
            continue
        
        season, episode, char, phrase = line.split(',', 3)
        words_per_char[char].update({episode: len(phrase.split())})

    return words_per_char

result = get_num_words_spoken_by_character_per_episode(get_season_csv_file(1))
print(result['Cartman'].most_common()[-3:])


