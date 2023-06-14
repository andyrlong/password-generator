import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0, END)

    length = var.get

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
            return password

    elif var.get == 0:
        for i in range(0, upper):
            password = password + random.choice(upper)
            return password
    elif var.get == 3:
        for i in range(0, chars):
            password = password + random.choice(chars)
            return password
    else:
        print("Please choose and option.")

def generate_password():
    generated_password = low()
    entry.insert(10, generate_password)

def copy_password():
    random_password = entry.get
    pyperclip.copy(random_password)


# Create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()
 
# Title 
root.title("Andrew's Password Generator")
 
# Create label and entry to show
# Password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
 
# Create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)
 
# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Copy", command=copy_password)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate_password)
generate_button.grid(row=0, column=3)
 
# Radio Buttons 
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)
 
# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
 
# start the GUI
root.mainloop()
