Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> dict={'Name':'sam','class':'what'}
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
>>> 
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
>>> 
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
