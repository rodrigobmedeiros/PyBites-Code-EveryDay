IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names: list[str]):

    count_name = 0
    for name in names:

        if name.startswith(IGNORE_CHAR) or any(char.isdigit() for char in name):
            continue
        elif name.startswith(QUIT_CHAR):
            break
        
        if count_name < MAX_NAMES:
            count_name += 1
            yield name

