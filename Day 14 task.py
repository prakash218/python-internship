from Coffee_Machine import *
from tkinter import *
from tkinter import messagebox
root = Tk()

def Submit():
	value = option.get()
	print(value)
	Object.get_input(value)

#Constants
bgcolor = '#79cef2'
option = StringVar()

Object = Coffee_Machine()



root.geometry('500x500+300+300')
root.title('Coffee Machine')
root.configure(bg = bgcolor)

#to get input
Label(root, text = 'Moon Bucks',bg = bgcolor, fg = '#0000ff', font = ('Helvetica',22)).grid(row = 1, column= 2, padx = 20)

Label(root, text = 'Enter Your Order:', bg = bgcolor).grid(row = 2, column = 1, padx = 30,pady = 20)

value = Entry(root, textvariable = option, bd = 3)
value.grid(row = 2, column = 2, ipadx = 50)

submit = Button(root, text = 'Submit', command = Submit).grid(row = 4, column = 2 , pady = 300)


root.mainloop()



