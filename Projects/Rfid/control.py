arduino=serial.serial('C0M5',9600,timeout=.1)
data=''
x=1
while x:
    data=arduino.readline()
    if data:
        x=0
        print(type(data))
        testdata=data.decode()
        print('your card no. is: ,testdata)
              df=pd.read_csv('student.csv')
              d=df['card no']
              i=0
              for n in d:
              if n==testdata:
              print(df.['name'][i])
              i+=1
