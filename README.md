# PyBites - Code Every Day Project

This repo will be used to solve pybites from [Py bites Challenges](https://codechalleng.es). There are more the 270 python challenges and the idea is solve at least one a day. I will include the resolved pybites daily.

# Bite 19 - Write a simple property - 28/05/2020

Write a simple Promo class. Its constructor receives a name `str` and expires `datetime`.

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/19/simple_property.py) 

Insight: Use @property to create a get method that will be called instead of acess the attribute directly.

# Bite 167 - Complete a User class: properties and representation dunder methods - 29/05/2020

In this Bite you are presented with another class, `User` this time.

Like last Bite you are asked to complete it, see the `TODO`s in the code below:

Complete the `get_full_name` property (more on properties here) that prints first and last name separated by a space.
Complete the `username` property following its docstring.
Complete the special representation dunder methods: `__str__` and `__repr__`. Look at the tests what they should return. Brace yourself for some bonus learning for a twist we added in `__repr__` (but as it's a Beginner Bite we give you a hint!)

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/167/user.py)

Insight: Finally, I understand what @property is although I've ever used this before. This decorator is used to create an method that will be viewed as a attribute by the user. So I'll protect my real attribute or just manipulate information with some logic implemented.

# Bite 25 - No promo twice, keep state in a class - 31/05/2020

In this bite a real world scenario: PyBites has a growing set of Bites and gives away promos. They choose a Bite randomly but don't want to choose the same one again.

Hence you are provided with a BITES constant and a bites_done set that gets passed into the class via its constructor. Complete the methods in the Promo class:

_pick_random_bite is a helper (_ here means private) that picks a randomly available Bite. When no more Bites are available raise a NoBitesAvailable (provided).
new_bite should use this helper and update self.bites_done (it keeps state, the reason we used a class here).

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/25/promo.py)

Insights:

- An empty list returns False when used as boolean, so if I need to verify if a list is empty can use "not list".
- Changing a dict into a list returns a list of keys.
- Using random module, there are two ways to get a random value from a sequence.
  - random.choice(seq) - return a single value from seq.
  - random.sample(seq, k) - return a list with k random values. We have to remember that if I want just one element, define k = 1 and use 0 index to get the value.
  - To finish, use again @property to define an attribute as a method.
  
  # Bite 71 - Keep state in a class + make its instance callable - 03/06/2020

In this Bite you write a small class to keep track of the max score in a game. When called as a function it receives a new score and returns the max score. Note it should work with negative numbers as well.

This is how it should work:
  
  
  from record import RecordScore

  record = RecordScore()  
  print(record(10))  
  10  
  print(record(9))  
  10  
  print(record(11))  # new max  
  11  

  record = RecordScore()  
  print(record(-5))  
  -5  
  print(record(-10))  
  -5  
  print(record(-2))  # new max  
  -2  
  
  
Use the `__call__` dunder ("special") method to make the RecordScore class callable.

Good luck and keep calm and code in Python!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/71/record.py)

Insights:

- `__call__` method is used to call an object as a function.
- To define the minimum number possible just make `var = float('-inf')`
- Get the hightest number between two options: `var = max(num1, num2)`
