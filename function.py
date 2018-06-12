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
 
