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
        
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper(), None)
    
    @staticmethod
    def hex2rgb(hex_format):
        """Class method that converts a hex value into an rgb one"""
        rgb_format = (int(hex_format[1:3], base=16), int(hex_format[3:5], base=16),
        int(hex_format[5:7], base=16))
        
        return rgb_format
    
    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        
        test_limits = [True if x in range(0,256) else False for x in rgb]

        if not all(test_limits):
    
            raise ValueError
        
        hex_list = [hex(x) for x in rgb]
        num_list = [x[2:] if len(x[2:]) == 2 else '0' + x[2:] for x in hex_list]
        hex_format = '#{}{}{}'.format(num_list[0], num_list[1], num_list[2])
        
        return hex_format

    def __repr__(self):
        """Returns the repl of the object"""
        
        str_repr = "Color('{}')".format(self.color)
        return str_repr

    def __str__(self):
        """Returns the string value of the color object"""
        
        str_color = 'None' if self.rgb == None else str(self.rgb)
        return str_color
    
    
    
    
    
    
    
    