>>> dict={'Name':'sam','class':'what'}
>>> print(dict)
{'Name': 'sam', 'class': 'what'}
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

>>> for n in dict.items():
        print(n)        
('Name', 'sam')
('class', 'what')
