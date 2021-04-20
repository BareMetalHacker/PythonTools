import tkinter
from tkinter import *

win = Tk()
def pr():
    print('Hi!')
win.geometry("400x400")
b = Button(win , text='myButton' , command=pr , padx=20 , pady=50 , activeforeground='red' , activebackground='blue')
b.place(x=200,y=150)


win.mainloop()
