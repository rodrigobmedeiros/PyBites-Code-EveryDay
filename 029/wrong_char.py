ALPHANUMERICS_CHAR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def get_index_different_char(chars):
    
    is_alphanumeric = [(str(char) in ALPHANUMERICS_CHAR) if str(char) != '' else False for char in chars]
    alphanumeric_rate = sum(is_alphanumeric) / len(is_alphanumeric)

    print(is_alphanumeric)

    if alphanumeric_rate > 0.5:

        return is_alphanumeric.index(False)

    else:

        return is_alphanumeric.index(True)

import string

alphanumeric_chars = list(string.ascii_letters + string.digits)


def get_index_different_char(chars):
    matches, no_matches = [], []
    for i, char in enumerate(chars):
        if str(char).lower() in alphanumeric_chars:
            matches.append(i)
        else:
            no_matches.append(i)
    return matches[0] if len(matches) == 1 else no_matches[0]