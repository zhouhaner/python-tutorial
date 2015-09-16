Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = "hello world."
>>> str(s)
'hello world.'
>>> repe(s)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    repe(s)
NameError: name 'repe' is not defined
>>> repr(s)
"'hello world.'"
>>> str(1/7)
'0'
>>> str(1.0/7)
'0.142857142857'
>>> x =10 * 3.25
>>> y = 200*200
>>> s = 'the value of x is ' + repr(x) + ', and y is' + repr(y) + '...'
>>> print s
the value of x is 32.5, and y is40000...
>>> # the repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print hellos
'hello, world\n'
>>> for x in range(1, 11):
	print repr(x).rjust(2), repr(x*x).rjust(3)
	print repr(x*x*x).rjust(4)

	
 1   1
   1
 2   4
   8
 3   9
  27
 4  16
  64
 5  25
 125
 6  36
 216
 7  49
 343
 8  64
 512
 9  81
 729
10 100
1000
>>> 
