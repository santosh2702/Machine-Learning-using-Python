Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> import time
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
