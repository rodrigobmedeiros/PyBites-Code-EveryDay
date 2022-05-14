from cars import (
    get_all_jeeps, 
    get_first_model_each_manufacturer,
    get_all_matching_models,
    sort_car_models
)

def test_get_all_jeeps():
    expected = "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"
    actual = get_all_jeeps()
    assert type(actual) == str 
    assert actual == expected 

def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected 

def test_get_all_matching_models_default_grep():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected

def test_get_all_matching_models_different_grep():
    expected = ['Accord', 'Commodore', 'Falcon']
    assert get_all_matching_models(grep='CO') == expected 

def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Here, is commented that to compare dicts, the order of keys doen't matter
    # the order of values in case of iterables must be the same
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected