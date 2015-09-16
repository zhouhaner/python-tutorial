Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in reversed(xrange(1,10,2)):
	print i

	
9
7
5
3
1
>>> basket = ['apple', 'orange', ' apple', 'pear', 'orange']
>>> for f in sorted(set(basket)):
	print f

	
 apple
apple
orange
pear
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.iteritems():
	print k, v

	
gallahad the pure
robin the brave
>>> words = {'cat', 'window', 'defenestrate'}
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    for w in words[:]:
TypeError: 'set' object has no attribute '__getitem__'
>>> for w in words[ : ]:
	if len(w) > 6:
		words.insert(0, w)

		

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for w in words[ : ]:
TypeError: 'set' object has no attribute '__getitem__'
>>> for w in words:
	if len(w) > 6:
		words.insert(0, w)

		

Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    words.insert(0, w)
AttributeError: 'set' object has no attribute 'insert'
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[ : ]:
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> 
