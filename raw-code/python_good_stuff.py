# -*- coding: utf-8 -*-

help(5)
# Help on int object:
# (etc etc)

dir(5)
# ['__abs__', '__add__', ...]

abs.__doc__
# 'abs(number) -> number
# Return the absolute value of the argument.

num = 13
num.__add__(2)
dir(num)

func.__code__.co_code

import dis
dis.dis(func)

dis.dis(compile("(10, 'abc')", '', 'eval'))
dis.dis(compile("[10, 'abc']", '', 'eval'))

a = ()
b = ()
a is b
# True
id(a)
# 4409020488
id(b)
# 4409020488

a = []
b = []
a is b
# False
id(a)
# 4465566920
id(b)
# 4465370632

a = (1, 2, 3)
id(a)
# 4427578104
del a
b = (1, 2, 4)
id(b)
# 4427578104

a = []
id(a)
# 4465566792
del a
b = []
id(b)
# 4465566792

dir(sys)
sys.argv
sys.executable
sys.exit
sys.exit(0)
sys.path
sys.platform
sys.modules




import sys
import array
import numpy as np

sys.getrefcount

sys.getsizeof(range(10))
# 48
sys.getsizeof(_ for _ in range(10))
# 88
sys.getsizeof(array.array('i', range(10)))
# 128
sys.getsizeof(tuple(range(10)))
# 128
sys.getsizeof(np.array(range(10), dtype='i'))
# 136
sys.getsizeof(list(range(10)))
# 200
sys.getsizeof({i: None for i in range(10)})
# 368
sys.getsizeof(set(range(10)))
# 736


from pympler import asizeof
asizeof.flatsize  # == sys.getsizeof

asizeof.asizeof(_ for _ in range(10))
# 0
asizeof.asizeof(range(10))
# 48
asizeof.asizeof(array.array('i', range(10)))
# 128
asizeof.asizeof(np.array(range(10), dtype='i'))
# 136
asizeof.asizeof(tuple(range(10)))
# 440
asizeof.asizeof(list(range(10)))
# 512
asizeof.asizeof({i: None for i in range(10)})
# 696
asizeof.asizeof(set(range(10)))
# 1048





hash(tuple())

class SameHash():
    def __hash__(self):
        return 1

a = SameHash()
b = SameHash()
a == b    # False
hash(a), hash(b)    # (1, 1)


# Python Riddle: 👻 it is a mystery
# What will this expression evaluate to?
{True: 'yes', 1: 'no', 1.0: 'maybe'}
# {True: 'maybe'}
True == 1 == 1.0    # True
hash(True), hash(1), hash(1.0)    # (1, 1, 1)

print(id(False), id(True))
print(id(1 != 1), id(1 == 1))
print(id(bool()), id(bool(1)))

from copy import deepcopy
x = [[0, 0], [1, 1]]
y = deepcopy(x)
print('x', x, id(x), id(x[0]), id(x[1]))
print('y', y, id(y), id(y[0]), id(y[1]))







bool(bool)    # True
bool(12)    # True
bool('asdsa')    # True
bool(0)    # False
bool('')    # False
bool(None)    # False
answer = None    # if not answer: (True), if answer is None:







import ast
expr = "[1, 2, 3]"
my_list = ast.literal_eval(expr)


import pdb
pdb.set_trace()

if n in [1, 4, 5, 6]:
    pass

a = [1, 2, 3, 4]
a[::-1]









a, b, c = range(3)
values = range(5)
a, b, _, _, _ = values
a, b, *rest = values
a, *rest, b = range(5)
*rest, a, b = range(5)


# Since Python 3.5
[1, 2, *[3, 4]]
# [1, 2, 3, 4]



# [expression]?[on_true]:[on_false]
[on_true] if [expression] else [on_false]

result = process(x) if is_valid(x) else print('invalid item: ', x)

score_1, score_2 = 5, 0
winner = "Argentina" if score_1 > score_2 else "Jamaica"    # Ternary operator

number = count if count % 2 else count - 1
name = user.name() if user is not None else 'Guest'

xP == hP and text[:m] == P and print(0, end=' ')











db = MySQLdb.connect("localhost", "username", "password", "dbname")
cursor = db.cursor()
sql = "SELECT `name`, `age` FROM `ursers` ORDER BY `age` DESC"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row[0] + row[1])
db.close()




import array
a = array.array('c', s)
print(a)
# array('c', 'Hello, world')
a[0] = 'y'
print(a)
# array('c', 'yello, world')
a.tostring()
# 'yello, world'









python -m timeit -s 'a = (10, 20, 30)' 'a[1]'
# 10000000 loops, best of 3: 0.0304 usec per loop
python -m timeit -s 'a = [10, 20, 30]' 'a[1]'
# 10000000 loops, best of 3: 0.0309 usec per loop

python -m timeit -s 'a = (10, 20, 30)' 'x, y, z = a'
# 10000000 loops, best of 3: 0.0249 usec per loop
python -m timeit -s 'a = [10, 20, 30]' 'x, y, z = a'
# 10000000 loops, best of 3: 0.0251 usec per loop

python -m timeit -n 100 -s "s = 'A'*10000; import textwrap; textwrap.fill(s)"
# 100 loops, best of 5: 12.3 nsec per loop
python -m timeit -s "s = 'A'*10000; import textwrap; textwrap.fill(s)"
# 20000000 loops, best of 5: 11.8 nsec per loop


import timeit
print(timeit.timeit("a and b", globals=globals()))

print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))

print(timeit.timeit("gcd(*rand())", number=100000, globals=globals()))

# The "timeit" module lets you measure the execution
# time of small bits of Python code
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 0.3412662749997253

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 0.2996307989997149

timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# 0.24581470699922647


# fastest reversing string in Python
timeit.timeit('"asdfg"[::-1]', number=1000000)

arr = [str(d) for d in range(101)]
timeit.timeit('sorted(map(int, set(arr)))', number=10000, globals=globals())
# 0.33720446200004517
timeit.timeit('sorted(int(s) for s in set(arr))', number=10000, globals=globals())
# 0.45892249400003493

arr = (str(d) for d in range(101))
timeit.timeit('sorted(map(int, set(arr)))', number=1000000, globals=globals())
# 0.8356489219995638
timeit.timeit('sorted(int(s) for s in set(arr))', number=1000000, globals=globals())
# 0.9175120390000302






assert issubclass(bool, int)
assert isinstance(lst, list)
assert isinstance(lst, tuple), 'TypeError'
assert id(obj1) == id(obj2) # obj1 is obj2
assert el in seq


# amount different mutable/immutable elements
objects = [1, [2], 1, [2], 3]
len({id(el) for el in objects})  # len(set(id(el) for el in objects))
# 4

tuple(filter(lambda x: x.isdigit(), ['d', '1', 'f', '5']))
tuple(x for x in ['d', '1', 'f', '5'] if x.isdigit())
# ('1', '5')


pi: float = 3.142
deq: Deque = collections.deque()


hasattr(a, 'attr')

getattr(d, cmd)(*args)
tuple(getattr(deq, el[0])() if len(el) == 1 else getattr(deq, el[0])(el[1])
      for el in raw_commands)


func.__closure__.cell_contents

__all__ = []









[*iterable]
(*iterable,)



for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")



class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

point = Bunch(datum=y, squared=y*y, coord=x)


# s = ''
# for x in list:
#     s += some_function(x)
slist = [some_function(elt) for elt in somelist]
s = ''.join(slist)



# if x == 0 or x == 1
# if x <= 1
if x in {0, 1}: ...

# if t in s:
#     print(pattern_in_string(t, s))
# else:
#     print(0)
print(pattern_in_string(t, s) if t in s else 0)




# res = 0
# if a > 0:
#     res += 1
# if b > 0:
#     res += 1
# if c > 0:
#     res += 1
res = (a > 0) + (b > 0) + (c > 0)




# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtup1e('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color
'red'
my_car.mileage
3812.4

# We get a nice string repr for free:
my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'
AttributeError: "can't set attribute"




# When To Use __repr__ vs __str__?
# Emulate what the std lib does:
import datetime
today = datetime.date.today()

# Result of __str__ should be readable:
str(today)
'2017-02-02'

# Result of __repr__ should be unambiguous:
repr(today)
'datetime.date(2017, 2, 2)'

# Python interpreter sessions use
# __repr__ to inspect objects:
today
datetime.date(2017, 2, 2)

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))










# "is" vs "=="
# • "==" evaluates to True if the objects
#   referred to by the variables are equal
# • "is" expressions evaluate to True if two
#   variables point to the same object
a = [1, 2, 3]
b = a

a is b
True
a == b
True

c = list(a)

a == c
True

a is c
False







# Functions are first-class citizens in Python.
# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.
def myfunc(a, b):
    return a + b

funcs = [myfunc]
funcs[0]
<function myfunc at 0x107012230>
funcs[0](2, 3)
5




# Python's list slice syntax can be used without indices
# for a few fun and useful things:
# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
lst
# []

# You can replace all elements of a list
# without creating a new list object:
a = lst
lst[:] = [7, 8, 9]
lst
# [7, 8, 9]
a
# [7, 8, 9]
a is lst
# True

# You can also create a (shallow) copy of a list:
b = lst[:]
b
# [7, 8, 9]
b is lst
# False

args = [3, 6]
list(range(*args))
# [3, 4, 5]




# collections.Counter lets you find the most common
# elements in an iterable:
import collections
c = collections.Counter('helloworld')
c
# Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

c.most_common(3)
# [('l', 3), ('o', 2), ('e', 1)]

collections.Counter(list).most_common(3)    # from collection import Counter
collections.Counter(a).most_common(1)[0][1]





# Python 3.3+ has a std
# lib module for displaying
# tracebacks even when Python
# "dies", e.g with a segfault:
import faulthandler
faulthandler.enable()

# Can also be enabled with
# "python -X faulthandler"
# from the command line.

# Learn more here:
# https://docs.python.org/3/library/faulthandler.html



# Pythonic ways of checking if all
# items in a list are equal:
lst = ['a', 'a', 'a']
# I ordered those from "most Pythonic" to "least Pythonic"
# and  "least efficient" to "most efficient".
# The len(set()) solution is idiomatic,  but constructing
# a set is less efficient memory and speed-wise.
len(set(lst)) == 1
# True
all(x == lst[0] for x in lst)
# True
lst.count(lst[0]) == len(lst)
# True




# In Python 3.4+ you can use
# contextlib.suppress() to selectively
# ignore specific exceptions:
import contextlib
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')

# This is equivalent to:
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass
# contextlib.suppress docstring:
#
# "Return a context manager that suppresses any
#  of the specified exceptions if they occur in the body
#  of a with statement and then resumes execution with
#  the first statement following the end of
#  the with statement."

from contextlib import contextmanager
@contextmanager
def tag(name):
    print("[%s]" % name)
    yield
    print("[/%s]" % name)



# In Python 3 you can use a bare "*" asterisk
# in function parameter lists to force the
# caller to use keyword arguments for certain
# parameters:
def f(a, b, *, c='x', d='y', e='z'):
    return 'Hello'

# To pass the value for c, d, and e you
# will need to explicitly pass it as
# "key=value" named arguments:
f(1, 2, 'p', 'q', 'v')
# TypeError: "f() takes 2 positional arguments but 5 were given"

f(1, 2, c='p', d='q',e='v')
# 'Hello'



# Python 3.5+ allows passing multiple sets
# of keyword arguments ("kwargs") to a
# function within a single call, using
# the "**" syntax:
def process_data(a, b, c, d):
    print(a, b, c, d)

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}

process_data(**x, **y)
# 1 2 3 4
process_data(**x, c=23, d=42)
# 1 2 23 42