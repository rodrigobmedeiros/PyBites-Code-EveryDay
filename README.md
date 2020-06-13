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

# Bite 95 - Subclass the dict built-in - 05/06/2020

In this Bite you will subclass the dict built-in to support a birthday dictionary.

This dictionary takes names as keys and birthday dates as values. Implement the __setitem__ dunder method to print a message every time somebody gets added with a birthday that is already in the dictionary. It should work like this when running it in the REPL:

```python
  >>> from datetime import date
  >>> from bdaydict import BirthdayDict
  >>> bd = BirthdayDict()
  >>> bd['bob'] = date(1987, 6, 15)
  >>> bd['tim'] = date(1984, 7, 15)
  >>> bd['mary'] = date(1987, 6, 15)  # whole date match
  Hey mary, there are more people with your birthday!
  >>> bd['sara'] = date(1987, 6, 14)
  >>> bd['mike'] = date(1981, 7, 15)  # day + month match
  Hey mike, there are more people with your birthday!
```

So if day and month are the same, you have a match, the year can be different. Use MSG to print the message, string replacing it with the name key of the newly added person.

Note that this exercise is to get you thinking about subclasses and extending built-in behavior. There is a caveat though: the code of the built-ins (written in C) does not call special methods overriden by user-defined classes (source: Fluent Python), so use this with caution.

Good luck and have fun!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/edit/master/95/bdaydict.py) 

Insight:
- Use of any() and all() to return True or False when analyze information into lists.
- User os super() to access a method from parent class. It was nice because I just complement the original implementation.
- Use of date.strftime() to converte data info into strings. For example: birthday = date(2000, 5, 30) birthday.strftime('%d') returns a string '30'.
- Use criativity to create a new class based on a built-in class, in this case the dict class.

# Bite 114 - Implement a Color class with staticmethod - 08/06/2020

As the new junior developer, you have been charged with enhancing the Color class.

Your task will be to implement the following:

add self.rgb to the `__init__` method that gets its value from the provided `COLOR_NAMES` dictionary (k, v = color_name, rgb tuple = e.g.: `"ALICEBLUE"`: (240, 248, 255)). If the value does not exist, just assume it is None.
Convert `hex2rgb` and `rgb2hex` into `@staticmethods`.
Validate the values being passed to each of these staticmethods and raise a ValueError if called with bad data.
Add a `__repr__` method whose value is in the form of Color('white'), with white being the inital value that it was initialized with.
Add a `__str__` method whose value is the RGB value of the color if it is found in `COLOR_NAMES`, else return Unknown.
Take a look at the tests for a better understanding of the values expected.

Good luck!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/114/color.py) 

Insights: 
1) Use method ```dict.get()``` to set a default value if the key you are looking for does not yet exist.
2) ```from string import hxdigits``` use hexdigits to import all hexadecimal digits into a string.
3) ```string.startswith()``` use this method to verify the first character (or a set of initial characters) of a string.
4) ```isinstance()``` use this built-in function to verify if an object belongs to a certain class.
5) ```@staticmethod``` class method that can be used without necessarily instantiating an object.

# Bite 138 - Write a simple property - 12/06/2020

Finish the `Animal` class below adding one or more class variables and a `classmethod` so that the following code:

```python
dog = Animal('dog')
cat = Animal('cat')
fish = Animal('fish')
lion = Animal('lion')
mouse = Animal('mouse')
print(Animal.zoo())
```

produces the following output:

```
10001. Dog
10002. Cat
10003. Fish
10004. Lion
10005. Mouse
```

Few things to note here:

The sequencing starts at 10000,
Each animal gets title cased,
An individual animal should print the sequence+name string as well, so best to implement the `__str__` method on the class.
So making another animal at this point, the following should work:

```python
horse = Animal('horse')
assert str(horse) == "10006. Horse"
```

As usual this is what the `pytest` code tests when you submit your code.

Have fun and code more Python! Join our thriving Slack Community under Settings to learn together with other passionate Pythonistas ...

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/138/zoo.py) 

Insights:
- Class attributes to define variables common to all instances.
- `@classmethod` to define methods that can be used without instantiating a class object.
- Use _ to define attributes that should not be used externally. This definition is good practice but does not effectively prevent the attribute from being used.
- `import itertools` can be used to define an infinite counter. Define `it = itertool.count(start= , step= )` and use `next(it)` to jump into next number in iterator.

# Bite 154 - Write your own data class - 13/06/2020

As you might have noticed we are now on Python 3.7 so time for a Bite on data classes which were introduced with [PEP 557](https://www.python.org/dev/peps/pep-0557/).

What are they? Raymond Hettinger summarized it nicely [in his great talk](https://www.youtube.com/watch?v=T-TwcmT6Rcw): a mutible named tuple with defaults.

One advantage is the code it saves you typing so they might become an essential part of your Python toolkit!

In this Bite we have you write a data class called `Bite` that managed 3 attributes: number, title, and level. Their types are `int`, `str` and `str` respectively.

There are 3 more requirements:

1) title needs to be capitalized upon instantiation (you get a hint in the tests for this one :) - make sure to read the tests for additonal specs, including some of the differences between `data classes` and `namedtuples`!)
2) level takes a default argument of Beginner.
3) A collection of Bite instances needs to be orderable (using `sort` / `sorted` - this is not by default but configurable ...)
Good luck and keep up with the language, exciting new things are getting added!
On that note feel free to make us more Bite requests via our Bites homepage (you'll find a form per Bite level at the bottom of the page ...)

For more resources on data classes we recommned watching [Hettinger's talk](https://codechalleng.es/bites/) as well as reading through Anthony Shaw's [A brief tour of Python 3.7 data classes](https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517). Have fun!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/154/dc.py) 

Insights:

- Learn about `data classes`, we can use it to start a new class with some magic methods pre-defined. 
- In the default setting, any dataclass will implement `__init__`, `__repr__`, `__str__` and `__eq__`.
- One of the best insights until now: If you want to make a object sortable when into a collection, just define the magic methods of the class: `__eq__`, `__gt__`, `__ge__`, `__lt__` and `__le__´.
