from pygame import mixer
##from tkinter.filedialog import  askdirectory
##file = 'g.mp3'
##pygame.init()
##pygame.mixer.init()
##pygame.mixer.music.load(file)
##pygame.mixer.music.play()
##


from tkinter import *
from pygame import mixer
import tkinter
var_play = ""




def select():
    global var_play
    window.filename = tkFileDialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    print (type(window.filename.decode()))
    var_play=str(window.filename)
    print(var_play)

    
def play_():
  

   mixer.init()                               
   mixer.music.load('Dynamite Vs I Will Be Here (Progressive Edit) - Dj A Sen (DJJOhAL.Com).mp3') 
   mixer.music.play()
    
def stop_():
    mixer.music.stop()
window = Tk()
 
window.title("Musify")
 
##lbl = Label(window, text="Hello")
##lbl = Label(window, text="Hello", font=("Arial Bold", 50)).grid(column=0, row=0)
##lbl.grid(column=0, row=0)

btn = Button(window, text="Play",bg='#0ff',fg='red',bd=8,command = play_)
btn.grid(column=1, row=0)
Button(window, text="stop",bg='#0ff',fg='red',bd=8,command = stop_).grid(column=2, row=0)
Button(window, text="open",bg='#0ff',fg='red',bd=8,command = select).grid(column=3, row=0)


window.mainloop()


##from Tkinter import filedialog
##from Tkinter import *
## 
##root = Tk()
##root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
##print (root.filename)


##from Tkinter import *
##import Tkinter, Tkconstants, tkFileDialog
## 
##root = Tk()
##root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
##print (root.filename)
