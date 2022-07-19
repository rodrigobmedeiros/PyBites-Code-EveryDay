# PyBites - Code Every Day Project

This repo will be used to solve pybites from [Py bites Challenges](https://codechalleng.es). There are more the 270 python challenges and the idea is solve at least one a day. I will include the resolved pybites daily.

# Bite 019 - Write a simple property - 28/05/2020

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

# Bite 025 - No promo twice, keep state in a class - 31/05/2020

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
  
# Bite 071 - Keep state in a class + make its instance callable - 03/06/2020

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

# Bite 095 - Subclass the dict built-in - 05/06/2020

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
- One of the best insights until now: If you want to make a object sortable when into a collection, just define the magic methods of the class: `__eq__`, `__gt__`, `__ge__`, `__lt__` and `__le__`.

# Bite 166 - Complete a tox ini file parser class - 16/06/2020

The INI file format is an informal standard for configuration files for some platforms or software. ([Wikipedia](https://en.wikipedia.org/wiki/INI_file)).

In this Bite you will use `configparser` to parse a [tox](https://tox.readthedocs.io/en/latest/) _ini file_.

Complete the `ToxIniParser` class, completing the stub properties making the tests happy.

Eh properties? No worries, [we got your back](https://pybit.es/property-decorator.html)!

See the TESTS tab. There is a lot of ini file data, so scroll down to the actual tests ...

Additionally here is how it would work in the Python REPL using [a copy of Django's tox ini file](https://bites-data.s3.us-east-2.amazonaws.com/django-tox.ini) saved to my local /tmp folder:

```python
  from ini import ToxIniParser
  tox = ToxIniParser('/tmp/django-tox.ini')
  tox.number_of_sections
  7
  tox.environments
  ['py3', 'flake8', 'docs', 'isort']
  tox.base_python_versions
  ['python3']
```

Good luck and keep calm and code in Python!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/166/ini.py) 

Insights:

- Use the module configparser to work with .ini files.
- Use set() to create a collection withoud repeated elements.

# Bite 199 - Multiple inheritance (__mro__) - 18/06/2020

Implement the following class structure: print(Child.__mro__):
```
(<class '__main__.Child'>,
 <class '__main__.Father'>,
 <class '__main__.Mother'>,
 <class '__main__.Person'>,
 <class 'object'>)
 ```
 
Each class has the following string representation:

```
person = Person()
dad = Father()
mom = Mother()
child = Child()

print(person)
print(dad)
print(mom)
print(child)
```

Output:

```
I am a person
I am a person and cool daddy
I am a person and awesome mom
I am the coolest kid
```

You should use inheritance here, so the I am a person substring should only occur in the Person base class.

Good luck and keep calm and code in Python!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/199/person.py) 

Insights:

- Use super() to get the mother class method `__str__`.
- Use `__mro__` to consult an object inheritance

# Bite 011 - Enrich a class with dunder methods - 29/06/2020

Let's enrich an Account class by adding dunder (aka special) methods to support the following:

length of the object: `len(acc)` returns the number of transactions
account comparison: `acc1 >,<,>=.<=,== acc2` returns a boolean comparing account balances
indexing: `acc[n]` shows the nth transaction onaccount (0 based)
iteration: `list(acc)` returns a sequence of account transactions
operator overloading: `acc + int` and `acc - int` can be used to add/subtract money
string representation: `str(acc)` returns NAME account - balance: INT
The provided template already does some setup for you.
Check out the tests for more specifics. Good luck!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/011/account.py) 

Insights:

- Use the class decorator @total_ordering and just define `__eq__` and `__lt__` to define all other ordering methods.
- `__getitem__` -> Used to return a value when you access the object with a index.
- `__len__` -> Return a value when use len() built-in function.
- `__add__` -> Define operation when add two objects, in this case return a sum between an object and an integer.
- `__sub__` -> Same thing of `__add__` but with subtraction.
- `__list__` -> Define what will be returned when use list() built-in function.

# Bite 020 - Write a context manager - 30/06/2020

Write a context manager to roll back a transaction on the given `Account` class.

There are two special (aka dunder) methods you need to define to create a context manager (there is also a convenient decorator - see Bite 88).

The purpose of the context manager is to roll back any transaction that will make the balance go below 0 (debt != cool). The rest of the class is already defined so you can focus on the context manager part.

See the tests for more detail. Good luck and keep calm and code in Python!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/020/account.py) 

Insights:

- Use `__enter__` and `__exit__` dunder methods to use the object into a context (with statment).
- In case of copy a list, use the built-in function list() in order to really create a new object.
- The `__enter__` method return the object itself and in this case all transations was copied into a new variable.
- If everything is ok I can consider the transations without context if not we just rollback to transations before the context.
- It's possible to create variables to the class out of `__init__` method.

# Bite 024 - ABC's and class inheritance - 04/07/2020

`ABC`'s or `Abstract Base Classes` are great to enforce a common API for your subclasses.

You define one or more methods and/or properties as abstract in the base class, and if the subclass does not implement them it raises a `TypeError`. In this bite you will use this concept as follows:

Define a Challenge base class that inherits from `ABC` (given), its constructor receives a `number` and a `title` attribute.
On Challenge define an `abstractmethod` called verify and an `property` (< 3.3 it would be an `abstractproperty`) called `pretty_title`.
Create the `BlogChallenge` and `BiteChallenge` classes which both inherit from `Challenge`. _Note that they would raise a `TypeError` at this point, exactly what you want: enforcing the use of the abstract method/ property_.
`BlogChallenge` and `BiteChallenge`'s constructors call the parent constructor (don't worry it's supercool, remember: we use Python3 so adjust your syntax), and both receive an extra argument in the constructor: `merged_prs` for `BlogChallenge` and `result` for `BiteChallenge`.
Implement the required methods and properties, refer to the tests what they need to return.
Get coding, learn more about classes, and have fun!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/024/challenge.py) 

Insights:

- Use _ABC_ metaclass to define abstract classes.
- Use decorator _@abstractmethod_ to define methods that must be defined into child classes.
- Use _@property_ + _@abstractmethod_ to define properties that must be define into child classes.
- How to use it in python: 
```python
from abc import ABC, abstractmethod

# ABC - Abstract Base Class
# abstractmethod - Function to be used as decorator.
```

# Bite 031 - Matrix Multiplication / @ operator - 04/07/2020

Since 3.5 Python has a binary operator to be used for matrix multiplication: `@`, see [PEP 465 -- A dedicated infix operator for matrix multiplication](https://legacy.python.org/dev/peps/pep-0465/).

The @ sign can now be used on types implementing the `__matmul__` special/magic/dunder method.

It is important to note that whilst this feature shipped in 3.5, none of the standard library builtin types have matrix multiplication implementations. So let's try to implement it on a custom type for this Bite.

Implement a simple class called `Matrix` that takes a list of lists in its constructor.

Implement the `__matmul__`, `__rmatmul__` (reversed) and `__imatmul__` (in place) dunder methods.

Yes, using `numpy` a `np.dot(self, other)` would suffice, but the point is to get you thinking about implementing @ yourself!

Here is a how matrix multiplication works:
```python
A = [[1, 2],  [3, 4]]
B = [[11, 12], [13, 14]]
```
Doing A @ B would do the following multiplications:

```python
[[1 * 11 + 2 * 13,   1 * 12 + 2 * 14],
[3 * 11 + 4 * 13,   3 * 12 + 4 * 14]]
```

See the tests for more info. Good luck!

Check the solution -> [click here](https://github.com/rodrigobmedeiros/PyBites-Code-EveryDay/blob/master/031/matmul.py) 

Insights:

- Use `__matmul__`, `__rmatmul__` and `__imatmul__` to define @ operations.
- If you want to convert a multidimensional array to list, use method `tolist()` instead of the built-in funcion `list()`.

# Bite 038

## Difference between ElementTree and Element:


XML tree and elements

XML is an inherently hierarchical data format, and the most natural way to represent it is with a tree. ET has two classes for this purpose - ElementTree represents the whole XML document as a tree, and Element represents a single node in this tree. Interactions with the whole document (reading and writing to/from files) are usually done on the ElementTree level. Interactions with a single XML element and its sub-elements are done on the Element level.

## Generator Functions instead generator objects

In this part Bob and Julian developed the get movies function with `yield` keyword. I my case I used a function returning a generator object. This approach was very good. Actually I've just checked that It's the same but I think use `yield` better than return the complete iterator.

## Use of .attrib instead of .get()

.attrib is a dict containing all attributes of a tag. 
.get() is a method to get the information from a attribute.

# Bite 043

## * to avoid positional arguments

I've just learned that we can use * to avoid positional arguments. I can use it like the example below:

```python
def no_positional_args(*, key_1='key_1', key_2='key_2'):
  pass
```

With this if I call the function passing a positional argument, I'll got an TypeError. Example: 

```python
no_positional_argument('rodrigo')
no_positional_argument('rodrigo', key_1='key_1', key_2='key_2')
no_positional_argument('rodrigo', key_2='key_2')
no_positional_argument('rodrigo', key_1='key_1')
```

All tries showed before will raise an error.

Take look at PEP570 for reference. [link](https://peps.python.org/pep-0570/)

# Bite 044

## string digits and ascii_uppercase

natively I have these two lists from string built-in module. 
- digits: All digits from 0-9
- ascii_uppercase: All letters from A-Z in uppercase

## random.choices

Using random built-in module and funcion choices, I can create a random combination from a original list.

# Bite 045

## A little deque

queu is a FIFO structure and save a lot of work while coding. In this bite, I only had to define maxlen to control the append operation. With this value defined, the length is controlled internally keeping the FIFO mechanism.

## pytest.mark.parametrize

with this decorator, we can parametrize test function with inumerous inputs, running as many tests we want.


# Bite 046

No extra learning but the bite was solved.

# Bite 054

- use splitlines() to analize each line.
- multiply string instead of repeat char.

# Bite 055

- Use feedparser module to parse RSS info.
- Don't forget to use comprehensions.

# Bite 056

- Use argparse module to develop a command line application based on bmic calculator function.
- [argparse link to read](https://docs.python.org/3/library/argparse.html)
- Nice to know about this library because become very easy to write a command line application. 
- Remembering what i've done working for radix, I could do something like that.
- About tests, I used again the context manager to test raise errors.
- Use `capfd` parameter to access command line output (like prints).