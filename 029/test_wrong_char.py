import pytest

from wrong_char import get_index_different_char


@pytest.mark.parametrize("arg, expected", [
    (['A', 'f', '.', 'Q', 2], 2),
    (['.', '{', ' ^', '%', 'a'], 4),
    ([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'], 1),
    (['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'], 5),
    (list(range(1, 9)) + ['}'] + list('abcde'), 8),
    ([2, '.', ',', '!'], 0),
])
def test_wrong_char(arg, expected):
    error = (f"get_index_different_char({arg}) should "
             f"return index {expected}")
    assert get_index_different_char(arg) == expected, error