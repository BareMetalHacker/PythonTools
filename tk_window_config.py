import tkinter
from tkinter import *

win = Tk()

frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

lb = Listbox(win)
lb.insert(1,'python')
lb.insert(2,'rattler')
lb.insert(3,'asp')

rb = Button(frame,text='Red',fg='red')
rb.pack(side=LEFT)

gb = Button(frame2,text='Green',fg='green')
gb.pack(side=RIGHT)


blb = Button(frame,text='Blue',fg='blue')
blb.pack(side=RIGHT)


bb = Button(frame2,text='Black',fg='black')
bb.pack(side=LEFT)


win.mainloop()
