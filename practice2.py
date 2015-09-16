Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ask_ok(promot, retries=4, complaint='yes or no ,please select!'):
      while True:
        ok = raw_input(promot)
        if ok in ('n', 'no', 'nop', 'nope'):
          return False
        if ok in ('y', 'ye', 'yes'):
          return True
        retries = retries -1
        if retries < 0:
          raise IOError('refusenik user')
        print complaint

        
>>> 
>>> 
>>> i = 5
>>> def f(arg=i):
	print arg

	
>>> i = 6
>>> f()
5
>>> def parrot(voltage, state='a stiff', action = 'voom', type = 'norwegian blue'):
	print "-- this parrot wouldn't", action,
	print "if you put", voltage, "volts through it."
	print "--lovely plumage, the", type
	print "--it's", state, "!"

	
>>> parrort(1000)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    parrort(1000)
NameError: name 'parrort' is not defined
>>> parrot(1000)
-- this parrot wouldn't voom if you put 1000 volts through it.
--lovely plumage, the norwegian blue
--it's a stiff !
>>> parrot(voltage = 1000)
-- this parrot wouldn't voom if you put 1000 volts through it.
--lovely plumage, the norwegian blue
--it's a stiff !
>>> parrot('a million', 'berefit of life', 'jump')
-- this parrot wouldn't jump if you put a million volts through it.
--lovely plumage, the norwegian blue
--it's berefit of life !
>>> def cheeseshop(kind, *arguments, ** keywords):
	print ""--do you have any ", kind, "?"
	
SyntaxError: invalid syntax
>>> def cheeseshop(kind, *arguments, ** keywords):
	print "--do you have any ", kind , "?"
	print "-- i'm sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print "-" * 40
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]

		
>>> cheeseshop("limurber", "it's very runny, sir.",
	   "it's really very, very runny, sir.",
	   shopkeeper='micheal palin',
	   client="john clease",
	   sketch = "cheese shop sketch")
--do you have any  limurber ?
-- i'm sorry, we're all out of limurber
it's very runny, sir.
it's really very, very runny, sir.
----------------------------------------
client : john clease
shopkeeper : micheal palin
sketch : cheese shop sketch
>>> print -*40
SyntaxError: invalid syntax
>>> print "-" * 40
----------------------------------------
>>> def write_mutiple_items(file, separator, *args):
	file.write(separator.join(args))

	
>>> range(3,6)
[3, 4, 5]
>>> args = [3, 6]
>>> range(args)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    range(args)
TypeError: range() integer end argument expected, got list.
>>> range(*args)
[3, 4, 5]
>>> parrot
<function parrot at 0x0000000002F77898>
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action":"voom"}
>>> parrot(**d)
-- this parrot wouldn't voom if you put four million volts through it.
--lovely plumage, the norwegian blue
--it's bleedin' demised !
>>> def make_incrementor(n):
	return lambda x : x + n

>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
>>> f(2)
44
>>> f(42)
84
>>> f(43)
85
>>> f(1000)
1042
>>> paris = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5 'five')]
SyntaxError: invalid syntax
>>> paris = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
>>> paris.sort(key=lambda paris: paris[1])
>>> paris
[(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> def my_function():
	"""do nothing, but doucument it.
                 No, really, it doesn't do anything.
                 """
	pass

>>> print my_function.__doc__
do nothing, but doucument it.
                 No, really, it doesn't do anything.
                 
>>> paris.pop([2])

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    paris.pop([2])
TypeError: an integer is required
>>> pop

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    pop
NameError: name 'pop' is not defined
>>> paris
[(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list = range[1:100]

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    list = range[1:100]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> list = range(1,100)
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> list.pop([2])

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    list.pop([2])
TypeError: an integer is required
>>> list.append("short number")
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 'short number']
>>> l = range(2, 50)
>>> list.extend(l)
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 'short number', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list.remove(2)
>>> list
[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 'short number', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list.insert(33, 100)
>>> list
[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 100, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 'short number', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list.pop()
49
>>> list
[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 100, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 'short number', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
>>> list.index(44)
43
>>> list.count(4)
2
>>> list.sort()
>>> list
[1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 'short number']
>>> list.reverse()
>>> list
['short number', 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 48, 47, 47, 46, 46, 45, 45, 44, 44, 43, 43, 42, 42, 41, 41, 40, 40, 39, 39, 38, 38, 37, 37, 36, 36, 35, 35, 34, 34, 33, 33, 32, 32, 31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 19, 19, 18, 18, 17, 17, 16, 16, 15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 1]
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
\
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> from collections import deque
>>> queue = deque(["eric", "john", "michael"])
>>> queue.append("terry")
>>> queue.append("graham")
>>> queue.popleft()
'eric'
>>> queue.popleft()
'john'
>>> queue
deque(['michael', 'terry', 'graham'])
>>> def f(x): return x % 3 == 0 or x % 5 == 0

>>> filter(f, range(2, 25))
[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
>>> def cube(x): return x*x*x

>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> filter(cube, range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> seq = range(8)
>>> def add(x, y): return x+y

>>> map(add, seq, seq)
[0, 2, 4, 6, 8, 10, 12, 14]
>>> reduce(add, range(1, 11))
55
>>> def sum(seq):
	def add(x, y): return x + y
	return reduce(add, seq, 0)

>>> sum(range(1, 11))
55
>>> sum([])
0
>>> squares = []
>>> for x in range(10):
	squares.append(x**2)

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [(x, y) for x in [1,2,3] for y in[1,2,3,4] if x!=y]
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4)]
>>> combs = []
>>> for x in [1,2,3]
SyntaxError: invalid syntax
>>> for x in [1,2,3]:
	for y in [3,1,4]:
		if x!=y:
			combs.append((x,y))

			
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> vec = [-4, -2, 0, 2, 4]
>>> [x*2 for in vec]
SyntaxError: invalid syntax
>>>  [x*2 for x in vec]
 
  File "<pyshell#147>", line 1
    [x*2 for x in vec]
    ^
IndentationError: unexpected indent
>>> vec
[-4, -2, 0, 2, 4]
>>> for x in vec:
	b = x*2

	
>>> b
8
>>> for x in vec:
	b = x*2
	print b

	
-8
-4
0
4
8
>>> [ x for x in vec if x >=0]
[0, 2, 4]
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> freshfruit = [ 'banana', 'loganberry', 'passion fruit']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> [x, x**2 for x in range(6)]
SyntaxError: invalid syntax
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
>>> matrix = [
	[1, 2, 3, 4],
	[2,3,4,5],
	[3, 4, 5, 6],
]
>>> maxtrix

Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    maxtrix
NameError: name 'maxtrix' is not defined
>>> matrix
[[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
>>>  transposed = []
 
  File "<pyshell#176>", line 1
    transposed = []
    ^
IndentationError: unexpected indent
>>> transposed = []
>>> for i in range(4):
	transposed.append([row[i] for row in matrix])

	
>>> transposed
[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
>>> zip(*matrix)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
>>> a = [-1, 1, 2, 3, 4, 5, 6, 7]
>>> del a[10]

Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    del a[10]
IndexError: list assignment index out of range
>>> del a[0]
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> del a[1:3]
>>> a
[1, 4, 5, 6, 7]
>>> del a[:]
>>> a
[]
>>> del a
>>> a

Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> t = 12345, 45678, "adwdad"
>>> t
(12345, 45678, 'adwdad')
>>> t[0]
12345
>>> u = t, (1, 2, 3, 4, 5), 1, 2, 3, 4
>>> u
((12345, 45678, 'adwdad'), (1, 2, 3, 4, 5), 1, 2, 3, 4)
>>> t[0]
12345
>>> t[0] = 8888

Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    t[0] = 8888
TypeError: 'tuple' object does not support item assignment
>>> v = ([1, 2, 3], [4, 5, 6])
>>> v
([1, 2, 3], [4, 5, 6])
>>> empty= （）
SyntaxError: invalid syntax

>>> empty = ()

>>> kong = []

>>> kong
[]

>>> empty
()

>>> singleton = 'hello'

>>> len(empty)
0

>>> len(kong)
0

>>> singleton
'hello'

>>> x, y ,z = t

>>> x
12345

>>> t
(12345, 45678, 'adwdad')

>>> a = set()

>>> a
set([])

>>> basket = ['apple', 'orange',  'apple', 'pear', 'orange', 'banana']

>>> fruit = set(basket)

>>> fruit
set(['orange', 'pear', 'apple', 'banana'])
>>> 'orange' in fruit
True

>>> 'crabgrass' in fruit
False

>>> a = set('abracadabra')

>>> b = sed('alacazam')

Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    b = sed('alacazam')
NameError: name 'sed' is not defined

>>> b = set('alacazam')

>>> a
set(['a', 'r', 'b', 'c', 'd'])

>>> a -b
set(['r', 'b', 'd'])

>>> a | b
set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])
>>> a & b
set(['a', 'c'])

>>> a ^ b
set(['b', 'd', 'm', 'l', 'r', 'z'])
>>> a = { x for x in a if x not in 'abc'}

>>> a
set(['r', 'd'])
>>> tel = {"jack": "10086", "rose": "10010"}
>>> tel
{'rose': '10010', 'jack': '10086'}

>>> tel['jim'] = 10010

>>> tel
{'rose': '10010', 'jim': 10010, 'jack': '10086'}

>>> del tel['jim']

>>> tel
{'rose': '10010', 'jack': '10086'}
>>> tel['zhouhan'] = "adasfsafwef"

>>> tel
{'zhouhan': 'adasfsafwef', 'rose': '10010', 'jack': '10086'}

>>> tel.keys()
['zhouhan', 'rose', 'jack']

>>> 'rose' in tel
True

>>> dict([('pace', 23123), ('sssss', "dasdad"), ('dasdawdw', "sadw")])
{'pace': 23123, 'sssss': 'dasdad', 'dasdawdw': 'sadw'}

>>> [x: x**2 for x in (2,4,6)]
SyntaxError: invalid syntax

>>> {x: x**2 for x in (2,4,6)}
{2: 4, 4: 16, 6: 36}

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v
	
  File "<pyshell#245>", line 3
    print i, v
        ^
IndentationError: expected an indented block
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	print i,  v
	
  File "<pyshell#246>", line 3
    print i,  v
        ^
IndentationError: expected an indented block
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	print i
	
  File "<pyshell#248>", line 3
    print i
        ^
IndentationError: expected an indented block
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i,  v)
	
  File "<pyshell#249>", line 3
    print(i,  v)
        ^
IndentationError: expected an indented block
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v
	
  File "<pyshell#250>", line 3
    print i, v
        ^
IndentationError: expected an indented block
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	
	print 1
	
  File "<pyshell#255>", line 4
    print 1
        ^
IndentationError: expected an indented block
>>> ================================ RESTART ================================
>>> 
0 tic
1 tac
2 toe
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
			print i, v
	
	
0 tic
1 tac
2 toe
>>> 
