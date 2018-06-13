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


#some more functions#
def fullName(firstname,lastname):
	return "{} {}".format(firstname,lastname)


#for printing number with incremented form:#
def inc(n,n2=1):
	return n+n2



#for printing the details in list form of a employee:#
def empinfo(x):
	s=x.split('-')
	print('name',([0]))
	print('fullname',([1]))
	print('phonenumber',([2]))
	print('mailId',([3]))
empinfo('santosh-sjdfh-9876549-singh.santosh2702@gmail.com')
#output:#
name [0]
fullname [1]
phonenumber [2]
mailId [3]

#using conditional for printing the largest number:#
def max(a,b,c):
	if a>b and a>c:
		return b
	elif b>c:
		return b
	else:
		return c


#Nested function:#
>>>def greet(name):
	def get_message():
	    return "hello"
	result=get_message()+name
	return result

>>> print greet("john")	
SyntaxError: invalid syntax
>>> greet("john")
'hellojohn'

	
>>> max(2,4,7)
7
#some decorator functions#
>>>def p decorate(func):
        def func wrapper(name):
                Return “<p>{0}</p>”.format(func(name))
         Return func wrapper
>>>@p decorate
>>>def get text(name):
        Return “lorem ipsum,{0} dolor sit amet”.format(name)
>>>get text(“john”)






 
