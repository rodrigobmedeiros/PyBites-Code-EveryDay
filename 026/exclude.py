from typing import Dict, Set

DEFAULT_BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
EXCLUDE_BITES = {6, 10, 16, 18, 21}


def filter_bites(
    bites: Dict[int, str] = DEFAULT_BITES,
    bites_done: Set[int] = EXCLUDE_BITES
) -> Dict[int, str]:
    """
    Return the bites dict with bites_done filtered out.
    """
    
    return {
        bite: bite_name for bite, bite_name in bites.items()
        if bite not in bites_done 
    }