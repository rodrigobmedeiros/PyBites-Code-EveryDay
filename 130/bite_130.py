from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""

    data = [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
            {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
            {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
            {"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":2002},
            {"id":2,"automaker":"Chrysler","model":"Town & Country","year":1999},
            {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
            {"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
            {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
            {"id":3,"automaker":"Porsche","model":"Cayenne","year":1999},
            ]

    data_filtered_by_year = [item for item in data if item['year'] == year]


    count_dict = {}

    for item in data_filtered_by_year:
        
        automaker = item['automaker']
        count_dict[automaker] = count_dict.setdefault(automaker, 0) + 1

        
    dict_items = count_dict.items()
    dict_items_sorted = sorted(dict_items, key=lambda x: x[1])

    return dict_items_sorted[-1][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""

    data = [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
            {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
            {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
            {"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":2002},
            {"id":2,"automaker":"Chrysler","model":"Town & Country","year":1999},
            {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
            {"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
            {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
            {"id":3,"automaker":"Porsche","model":"Cayenne","year":1999},
            ]

    data_filtered_by_year = [item for item in data if (item['year'] == year) & (item['automaker'] == automaker)]

    models = [item['model'] for item in data_filtered_by_year]

    return set(models)

count_dict = most_prolific_automaker(1999)

print(count_dict)

models = get_models('Porsche', 1999)

print(models)