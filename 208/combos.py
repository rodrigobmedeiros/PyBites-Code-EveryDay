import itertools

def find_number_pairs(numbers, N=10):
    possible_combinations = itertools.combinations(numbers, 2)
    return [pair for pair in possible_combinations if pair[0] + pair[1] == N]

