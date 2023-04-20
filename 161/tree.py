import os
from pathlib import Path

def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    root = Path(directory)
    contents = root.iterdir()
    n_dir = 0
    n_files = 0

    for content in contents:

        if content.is_dir():
            inner_dir, inner_files = count_dirs_and_files(content)
            n_dir = n_dir + inner_dir + 1
            n_files += inner_files
        else:
            n_files += 1

    return (n_dir, n_files)
