from ast import Lambda
from binascii import b2a_uu
from dis import dis
from tkinter import *

root=Tk()
root.title("Calculator")

display=Entry(root, width=35, borderwidth=5, bg="black", fg="white")
display.grid(row=0,column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    
    current=display.get()
    display.delete(0,END)
    display.insert(0,str(current)+ str(number))
    
def button_clear():
    display.delete(0,END)
    
def button_add():
    return

#creating buttons

button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1),bg="white")
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2),bg="white")
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3),bg="white")
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4),bg="white")
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5),bg="white")
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6),bg="white")
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7),bg="white")
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8),bg="white")
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9),bg="white")
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0),bg="white")

button_add=Button(root,text="+",padx=39,pady=20,command=lambda:button_add,bg="#8367C7",fg="white")
button_equal=Button(root,text="=",padx=91,pady=20,command=lambda:button_click(),bg="#D81E5B",fg="white")
button_clear=Button(root,text="Clear",padx=79,pady=20,command=button_clear,bg="#49D49D",fg="white")

#display buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)


button_clear.grid(row=4, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

root.mainloop()
