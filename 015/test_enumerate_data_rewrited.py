import pytest

from enumerate_data import enumerate_names_countries

expected_lines = [
    '1. Julian     Australia',
    '2. Bob        Spain',
    '3. PyBites    Global',
    '4. Dante      Argentina',
    '5. Martin     USA',
    '6. Rodolfo    Mexico'
]

# @pytest.mark.parametrize seems to be a decorator that calls the test function
# multiple times based on a list of inputs.
# In this case each element in the list is allocated into line variable
# This variable is passed to the test function
# Here I can see another interesting point the parameter capfd
# this parameter is passed to the test function and is responsible
# for read outputs printed on the command line.
# Here to read, I used the method readoutter()[0] (Why index zero?)
@pytest.mark.parametrize("line", expected_lines)
def test_enumerate_names_countres(capfd, line):
    enumerate_names_countries()
    output = capfd.readouterr()[0]
    assert line in output, f'{line} not in output'