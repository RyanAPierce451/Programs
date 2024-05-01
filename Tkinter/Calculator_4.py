from tkinter import *

#9 buttons
root = Tk() 
root.title("lklkl")

e = Entry(root, width=11, borderwidth=2, font=('Arial 30'))
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

def button_click(number):
    current_num = e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(number))

def button_clears():
    e.delete(0, END)

def button_adds():
    first_num = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def button_subtracts():
    first_num = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def button_multiplies():
    first_num = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def button_divides():
    first_num = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def button_equals():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_num))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_num))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_num))
    elif math == "division":
        e.insert(0, f_num / int(second_num))

# Defines the Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_adds)
button_equal = Button(root, text="=", padx=86, pady=20, command=button_equals)
button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clears)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtracts)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiplies)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divides)

# Put the Buttons on the Screen

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
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop() 