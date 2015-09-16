Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 50-5*6
20
>>> 17/3
5
>>> 17/3.0
5.666666666666667
>>> 17%3
2
>>> 5**6
15625
>>> n

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 3**5
243
>>> 5//3
1
>>> 500//3
166
>>> round(_,2)
166.0
>>> round(1211, 131)
1211.0
>>> "span eggs"
'span eggs'
>>> "span \ eggs"
'span \\ eggs'
>>> doesn\'t'
SyntaxError: unexpected character after line continuation character
>>> 'doesn\'t'
"doesn't"
>>> print 'c:\some\name'
c:\some
ame
>>> print r'c:\some\name'
c:\some\name
>>> print """\
"""

>>> print """\
usage: thingy [options]
    -h
    -H hostname
""'
"""
usage: thingy [options]
    -h
    -H hostname
""'

>>> # 3 times 'un', followed by 'ium'
>>> 3* 'uu' +'ium'
'uuuuuuium'
>>> 'py' 'thon'
'python'
>>> prefix + 'thon'

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    prefix + 'thon'
NameError: name 'prefix' is not defined
>>> prefix = 'py'
>>> prefix +'thon'
'python'
>>> word = 'oython'
>>> word[0]
'o'
>>> for i in word
SyntaxError: invalid syntax
>>> word
'oython'
>>> word[5]
'n'
>>> word[-5]
'y'
>>> word[-6]
'o'
>>> word[0:4]
'oyth'
>>> word[0:4]+word[1:3]
'oythyt'
>>> word[-5:]
'ython'
>>> word[-2:]
'on'
>>> word[3:100]
'hon'
>>> word[22:]
''
>>> word[0] = 'j'

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    word[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> s = 'dadqdafqwfvdsvfgrtwhbnshsfgasfgSRFAVARTFAF'
>>> len(s)
42
>>> u 'hello world'
SyntaxError: invalid syntax
>>> u 'hello world'
SyntaxError: invalid syntax
>>> u'hello world !'
u'hello world !'
>>> u "abc"
SyntaxError: invalid syntax
>>> u"abc"
u'abc'
>>> str(u"abdcdsg")
'abdcdsg'
>>> unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')
u'\xe4\xf6\xfc'
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cubes = [1, 8, 27, 65, 81, 100[
	]
	 
SyntaxError: invalid syntax
>>> cubes = [1, 8, 27, 65, 81, 100]
>>> 4**3
64
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 81, 100]
>>> cubes.append(216)
>>> cubes.append(7**3)
>>> cubes
[1, 8, 27, 64, 81, 100, 216, 343]
>>> 8***2
SyntaxError: invalid syntax
>>> 8**2
64
>>> cubes.append(8**3)
>>> cubes
[1, 8, 27, 64, 81, 100, 216, 343, 512]
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> len(letters)
7
>>> while b <10:
	print b
	a, b =b, a+b

	

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    while b <10:
NameError: name 'b' is not defined
>>> a, b = 0, 1
>>> while b <10
SyntaxError: invalid syntax
>>> while b <10:
	print b
	a, b =b ,a+b

	
1
1
2
3
5
8
>>> a , b = 0, 1
>>> while b < 100:
	print b ,
	a, b = b, a+b

	
1 1 2 3 5 8 13 21 34 55 89
>>> x =30
>>> if x<0:
	x =0
    elif x == 0:
	    
  File "<pyshell#96>", line 3
    elif x == 0:
               ^
IndentationError: unindent does not match any outer indentation level
>>> if x < 0:
	x = 0
        elif x == 0:
		
SyntaxError: invalid syntax
>>> if x < 0:
	x = 0
        else x ==0:
		
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
please enter an integer: 1
single
>>> 220
220
>>> # measure some strings:
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
	print w, len(w)

	
cat 3
window 6
defenestrate 12
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range95,10)
SyntaxError: invalid syntax
>>> range(5,10)
[5, 6, 7, 8, 9]
>>> range(0,10,3)
[0, 3, 6, 9]
>>> range(-10,1000,2)
[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 458, 460, 462, 464, 466, 468, 470, 472, 474, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 512, 514, 516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556, 558, 560, 562, 564, 566, 568, 570, 572, 574, 576, 578, 580, 582, 584, 586, 588, 590, 592, 594, 596, 598, 600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638, 640, 642, 644, 646, 648, 650, 652, 654, 656, 658, 660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688, 690, 692, 694, 696, 698, 700, 702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728, 730, 732, 734, 736, 738, 740, 742, 744, 746, 748, 750, 752, 754, 756, 758, 760, 762, 764, 766, 768, 770, 772, 774, 776, 778, 780, 782, 784, 786, 788, 790, 792, 794, 796, 798, 800, 802, 804, 806, 808, 810, 812, 814, 816, 818, 820, 822, 824, 826, 828, 830, 832, 834, 836, 838, 840, 842, 844, 846, 848, 850, 852, 854, 856, 858, 860, 862, 864, 866, 868, 870, 872, 874, 876, 878, 880, 882, 884, 886, 888, 890, 892, 894, 896, 898, 900, 902, 904, 906, 908, 910, 912, 914, 916, 918, 920, 922, 924, 926, 928, 930, 932, 934, 936, 938, 940, 942, 944, 946, 948, 950, 952, 954, 956, 958, 960, 962, 964, 966, 968, 970, 972, 974, 976, 978, 980, 982, 984, 986, 988, 990, 992, 994, 996, 998]
>>> a = ['mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
	print i, a[i]

	
0 mary
1 had
2 a
3 little
4 lamb
>>> for n in range(2, 10):
	for x in range(2, n ):
		if n%x ==0:
			print n , 'equals', x, '*', n/x
			break
		else:
			# loop fell through without finding a
			print n, 'is a prime number'

			
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
>>> for num in range(2, 10):
	if num%2 == 0:
		print "found a even number", num
		coutinue
	print "found a number", num

	
found a even number 2

Traceback (most recent call last):
  File "<pyshell#138>", line 4, in <module>
    coutinue
NameError: name 'coutinue' is not defined
>>> for num in range(2, 10):
	if num%2 == 0:
		print "found a even number", num
		continue
	print "found a number", num

	
found a even number 2
found a number 3
found a even number 4
found a number 5
found a even number 6
found a number 7
found a even number 8
found a number 9
>>> while True
SyntaxError: invalid syntax
>>> while True:
	pass


Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    while True:
KeyboardInterrupt


>>> clear

Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> class MyEmptyclass:
	pass
KeyboardInterrupt
>>> def fib(n):
	"""print a fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b

		
>>> fib(200)
0 1 1 2 3 5 8 13 21 34 55 89 144
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
>>> fib
<function fib at 0x0000000002E6E438>
>>> fib(0)
>>> print fib(0)
None
>>> def fib2(n):
	"""return a list containing the fibonacci series"""
	result = []
	a, b = 0, 1
	while a <n:
		result.append(a)
		a, b = b, a+b
	return result

>>> f100 = fib2(100)
>>> f100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> 
