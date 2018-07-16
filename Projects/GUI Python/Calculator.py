from tkinter import *
import math
 
window = Tk()
 
window.title("Calculator")
 
window.geometry('200x200')
 

 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
txt1 = Entry(window,width=10)
 
txt1.grid(column=2, row=0)
lbl = Label(window, text="=")
 
lbl.grid(column=0, row=0)

res=0
res1=0
res2=0
res3=0
res4=0
res5=0
res6=0
 
def clicked():
    global res,res1,res2,res3,res4,res5,res6
 
    res =  int(txt.get())+ int(txt1.get())
 
    lbl = Label(window, text=res)
 
    lbl.grid(column=0, row=7)

    res1 =  int(txt.get())* int(txt1.get())
 
    lbl = Label(window, text=res1)
 
    lbl.grid(column=1, row=7)
    res2 =  int(txt.get())- int(txt1.get())
 
    lbl = Label(window, text=res2)
 
    lbl.grid(column=2, row=7)

    res3 =  int(txt.get())/ int(txt1.get())
 
    lbl = Label(window, text=res3)
 
    lbl.grid(column=3, row=7)

    res4 =  int(txt.get())^ int(txt1.get())
 
    lbl = Label(window, text=res4)
 
    lbl.grid(column=0, row=8)

    res3 =  int(txt.get())/ int(txt1.get())
 
    lbl = Label(window, text=res3)
 
    lbl.grid(column=3, row=7)

    res6 =  int(txt.get())% int(txt1.get())
 
    lbl = Label(window, text=res6)
 
    lbl.grid(column=3, row=8)





btn = Button(window, text="+",width=3, command=clicked)
btn.grid(column=0, row=5)
btn = Button(window, text="x",width=3, command=clicked)
btn.grid(column=1, row=5)
btn = Button(window, text="-",width=3, command=clicked)
btn.grid(column=2, row=5)
btn = Button(window, text="÷",width=3, command=clicked)
btn.grid(column=3, row=5)

btn=Button(window,text='C',width=3,command=clicked)
btn.grid(row=4, column=1)
btn=Button(window,text='AC',width=3,command=clicked)
btn.grid(row=4, column=2)
btn=Button(window,text=".",width=3,command=clicked)
btn.grid(row=4, column=1)
btn=Button(window,text="(",width=3,command=clicked)
btn.grid(row=6, column=0)
btn=Button(window,text=")",width=3,command=clicked)
btn.grid(row=6, column=1)
btn=Button(window,text="√",width=3,command=clicked)
btn.grid(row=6, column=2)
btn=Button(window,text="x²",width=3,command=clicked)
btn.grid(row=6, column=3)
btn=Button(window,text="7",width=3,command=clicked)
btn.grid(row=1, column=0)
btn=Button(window,text="8",width=3,command=clicked)
btn.grid(row=1, column=1)
btn=Button(window,text="9",width=3,command=clicked)
btn.grid(row=1, column=2)
btn=Button(window,text="4",width=3,command=clicked)
btn.grid(row=2, column=0)
btn=Button(window,text="5",width=3,command=clicked)
btn.grid(row=2, column=1)
btn=Button(window,text="6",width=3,command=clicked)
btn.grid(row=2, column=2)
btn=Button(window,text="1",width=3,command=clicked)
btn.grid(row=3, column=0)
btn=Button(window,text="2",width=3,command=clicked)
btn.grid(row=3, column=1)
btn=Button(window,text="3",width=3,command=clicked)
btn.grid(row=3, column=2)
btn=Button(window,text="0",width=3,command=clicked)
btn.grid(row=4, column=0)
 
window.mainloop()

