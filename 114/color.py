import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        pass

    def hex2rgb(...
        """Class method that converts a hex value into an rgb one"""
        pass

    def rgb2hex(...
        """Class method that converts an rgb value into a hex one"""
        pass

    def __repr__(self):
        """Returns the repl of the object"""
        pass

    def __str__(self):
        """Returns the string value of the color object"""
        pass