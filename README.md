# PyBites - Code Every Day Project

This repo will be used to solve pybites from [Py bites Challenges](https://codechalleng.es). There are more the 270 python challenges and the idea is solve at least one a day. I will include the resolved pybites daily.

# Bite 19 - Write a simple property - 28/05/2020

Write a simple Promo class. Its constructor receives a name `str` and expires `datetime`.

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/19/simple_property.py) 

Insight: Use @property to create a get method that will be called instead of acess the attribute directly.

# Bite 19 - Complete a User class: properties and representation dunder methods - 29/05/2020

In this Bite you are presented with another class, `User` this time.

Like last Bite you are asked to complete it, see the `TODO`s in the code below:

Complete the `get_full_name` property (more on properties here) that prints first and last name separated by a space.
Complete the `username` property following its docstring.
Complete the special representation dunder methods: `__str__` and `__repr__`. Look at the tests what they should return. Brace yourself for some bonus learning for a twist we added in `__repr__` (but as it's a Beginner Bite we give you a hint!)
