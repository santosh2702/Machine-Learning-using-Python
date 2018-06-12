>>> dict={'Name':'sam','class':'what'}
>>> print(dict)
{'Name': 'sam', 'class': 'what'}
>>> del(class)
SyntaxError: invalid syntax
>>> del dict{'Name'};
SyntaxError: invalid syntax
>>> del dict['Name'];
>>> dict.clear();
>>> del dict;
>>> print(dict)
<class 'dict'>
>>> len(dict)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    len(dict)
TypeError: object of type 'type' has no len()
>>> dict={'Name':'sam','class':'what'}
>>> print(dict)
{'Name': 'sam', 'class': 'what'}
>>> len(dict)
2
>>> dict.keys()
dict_keys(['Name', 'class'])
>>> x=dict.keys()
>>> x
dict_keys(['Name', 'class'])
>>> dict.get('class')
'what'
>>> dict.get('Name')
'sam'
>>> dict.get('Name','ok')
'sam'
>>> dict.item()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict.item()
AttributeError: 'dict' object has no attribute 'item'
>>> dict.items()
dict_items([('Name', 'sam'), ('class', 'what')])
>>> for n,m in dict.items():
	print(n,m)

	
Name sam
class what
>>> for n in dict.items()
SyntaxError: invalid syntax
>>> for n in dict.items():
        print(n)        
('Name', 'sam')
('class', 'what')
>>> import time
>>> time.time()
1528803016.488397
>>> time.localtime()
time.struct_time(tm_year=2018, tm_mon=6, tm_mday=12, tm_hour=17, tm_min=2, tm_sec=4, tm_wday=1, tm_yday=163, tm_isdst=0)
>>> time.localtime().tm_year
2018
>>> time.localtime(time.time())
time.struct_time(tm_year=2018, tm_mon=6, tm_mday=12, tm_hour=17, tm_min=4, tm_sec=34, tm_wday=1, tm_yday=163, tm_isdst=0)
>>> time.ctime()
'Tue Jun 12 17:04:44 2018'
>>> time.localtime().tm_isdst
0
>>> import calendar
>>> print(calendar.month(2018,6))
     June 2018
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

>>> import time
>>> for n in range(5):
	print(n)
	time.sleep(2)	
0
1
2
3
4

>>> def add(a,b):
	return(a+b)

>>> add(4,8)
12
>>> def add(a=0,b=0):
        print('a:',a)
        print('b:',b)
        return(a+b)

>>> add(8,4)
a: 8
b: 4
12
>>> def add(*data):
	result=0
	for n in data:
	    result+=n
	return result

>>> x=add(1,2,3,4,5,6,7)
>>> print(x)
28
 
