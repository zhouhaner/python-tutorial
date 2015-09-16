Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True：
SyntaxError: invalid syntax
>>> while True:
	try:
		x = int(raw_input("please enter a number:"))
		break
	except ValueError:
		print "Oops! that was no valid number. try again...."

		
please enter a number:3
>>> import sys
>>> try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except IOError as e:
	print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
	print "could not convert data to an integer."
except:
	print "unexcepted error:", sys.exc_info()[0]
	raise

I/O error(2): No such file or directory
>>> try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print type(inst)
	print inst.args
	print inst

	
<type 'exceptions.Exception'>
('spam', 'eggs')
('spam', 'eggs')
>>> def this_fails():
	x = 1/0

	
>>> try:
	this_fails()
except ZeroDivisionError as drtail:
	print 'handling run-time error:', detail

	
handling run-time error:

Traceback (most recent call last):
  File "<pyshell#36>", line 4, in <module>
    print 'handling run-time error:', detail
NameError: name 'detail' is not defined
>>>  try:
	this_fails()
except ZeroDivisionError as detail:
	print 'handling run-time error:', detail
	
  File "<pyshell#37>", line 1
    try:
    ^
IndentationError: unexpected indent
>>> raise NameError('hithere')

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    raise NameError('hithere')
NameError: hithere
>>> try:
	raise NameError('hithere')
except NameError:
	print 'an exception flew by!'
	raise

an exception flew by!

Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    raise NameError('hithere')
NameError: hithere
>>>  class MyError(Exception):
	 
  File "<pyshell#45>", line 1
    class MyError(Exception):
    ^
IndentationError: unexpected indent
>>> class myerror(Exception):
	def __init__(self, value):
		self.value= value
	def __str__(self):
		return repr(self.value)

	
>>> try:
	raise MyError(2*2)
except myerror as e;'
SyntaxError: invalid syntax
>>>  try:
	raise MyError(2*2)
except myerror as e:
	
  File "<pyshell#55>", line 1
    try:
    ^
IndentationError: unexpected indent
>>> try:
	raise myerror(2*2)
except myerror as e:
	print ' my exception occurred, value:', e.value

	
 my exception occurred, value: 4
>>> raise myerror('oops!')

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    raise myerror('oops!')
myerror: 'oops!'
>>> divide(2, 1)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    divide(2, 1)
NameError: name 'divide' is not defined
>>> class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

		
>>> x = Complex(3.0, -4.5)
>>> x.r
3.0
>>> x.i
-4.5
>>> s = 'abc;
SyntaxError: EOL while scanning string literal
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x0000000002EC85F8>
>>> next(it)
'a'
>>> ================================ RESTART ================================
>>> 
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse instance at 0x0000000002DB3E48>
>>> for char in rev:
	print char

	

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    for char in rev:
TypeError: instance has no next() method
>>> print rev
<__main__.Reverse instance at 0x0000000002DB3E48>
>>> for char in rev:
	print(char)

	

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    for char in rev:
TypeError: instance has no next() method
>>> def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

		
>>> for char in reverse('golf')
SyntaxError: invalid syntax
>>> for char in reverse('golf'):
	print char

	
f
l
o
g
>>> sum(i*i for i in range(10))
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x, y in zip(xvec, yvec))
260
>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
>>> print sine_table
{0: 0.0, 1: 0.01745240643728351, 2: 0.03489949670250097, 3: 0.05233595624294383, 4: 0.0697564737441253, 5: 0.08715574274765817, 6: 0.10452846326765346, 7: 0.12186934340514748, 8: 0.13917310096006544, 9: 0.15643446504023087, 10: 0.17364817766693033, 11: 0.1908089953765448, 12: 0.20791169081775931, 13: 0.224951054343865, 14: 0.24192189559966773, 15: 0.25881904510252074, 16: 0.27563735581699916, 17: 0.29237170472273677, 18: 0.3090169943749474, 19: 0.32556815445715664, 20: 0.3420201433256687, 21: 0.35836794954530027, 22: 0.374606593415912, 23: 0.3907311284892737, 24: 0.40673664307580015, 25: 0.42261826174069944, 26: 0.4383711467890774, 27: 0.45399049973954675, 28: 0.4694715627858908, 29: 0.48480962024633706, 30: 0.49999999999999994, 31: 0.5150380749100542, 32: 0.5299192642332049, 33: 0.5446390350150271, 34: 0.5591929034707469, 35: 0.573576436351046, 36: 0.5877852522924731, 37: 0.6018150231520483, 38: 0.6156614753256582, 39: 0.6293203910498374, 40: 0.6427876096865393, 41: 0.6560590289905072, 42: 0.6691306063588582, 43: 0.6819983600624985, 44: 0.6946583704589973, 45: 0.7071067811865475, 46: 0.7193398003386511, 47: 0.7313537016191705, 48: 0.7431448254773941, 49: 0.754709580222772, 50: 0.766044443118978, 51: 0.7771459614569708, 52: 0.788010753606722, 53: 0.7986355100472928, 54: 0.8090169943749475, 55: 0.8191520442889918, 56: 0.8290375725550417, 57: 0.8386705679454239, 58: 0.8480480961564261, 59: 0.8571673007021122, 60: 0.8660254037844386, 61: 0.8746197071393957, 62: 0.8829475928589269, 63: 0.8910065241883678, 64: 0.898794046299167, 65: 0.9063077870366499, 66: 0.9135454576426009, 67: 0.9205048534524403, 68: 0.9271838545667874, 69: 0.9335804264972017, 70: 0.9396926207859083, 71: 0.9455185755993167, 72: 0.9510565162951535, 73: 0.9563047559630354, 74: 0.9612616959383189, 75: 0.9659258262890683, 76: 0.9702957262759965, 77: 0.9743700647852352, 78: 0.9781476007338056, 79: 0.981627183447664, 80: 0.984807753012208, 81: 0.9876883405951378, 82: 0.9902680687415703, 83: 0.992546151641322, 84: 0.9945218953682733, 85: 0.9961946980917455, 86: 0.9975640502598242, 87: 0.9986295347545738, 88: 0.9993908270190958, 89: 0.9998476951563913, 90: 1.0}
>>> unique_words = set(word for line in page for word in line.spilt())

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    unique_words = set(word for line in page for word in line.spilt())
NameError: name 'page' is not defined
>>> import os
>>> os.getcwd()
'E:\\web study\\python\\python tutorial'
>>> import os
>>> dir(os)
['F_OK', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'UserDict', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_copy_reg', '_execvpe', '_exists', '_exit', '_get_exports_list', '_make_stat_result', '_make_statvfs_result', '_pickle_stat_result', '_pickle_statvfs_result', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'curdir', 'defpath', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fstat', 'fsync', 'getcwd', 'getcwdu', 'getenv', 'getpid', 'isatty', 'kill', 'linesep', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'popen2', 'popen3', 'popen4', 'putenv', 'read', 'remove', 'removedirs', 'rename', 'renames', 'rmdir', 'sep', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'startfile', 'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', 'sys', 'system', 'tempnam', 'times', 'tmpfile', 'tmpnam', 'umask', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'walk', 'write']
>>> 
