from exclude import filter_bites


def test_filter_bites_default_arguments():
    actual = filter_bites()
    expected = {
        7: "Parsing dates from logs",
        9: "Palindromes",
        11: "Enrich a class with dunder methods",
        12: "Write a user validation function",
        13: "Convert dict in namedtuple/json",
        14: "Generate a table of n sequences",
        15: "Enumerate 2 sequences",
        17: "Form teams from a group of friends",
        19: "Write a simple property",
        20: "Write a context manager",
    }
    assert actual == expected


def test_filter_bites_different_outputs():
    bites = {
        26: "Dictionary comprehensions are awesome",
        15: "Enumerate 2 sequences",
        21: "Query a nested data structure",
        105: "Slice and dice",
    }
    excluded_bites = {21, 105}
    actual = filter_bites(bites, excluded_bites)
    expected = {
        26: "Dictionary comprehensions are awesome",
        15: "Enumerate 2 sequences",
    }
    assert actual == expected