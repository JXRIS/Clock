# Imports
from time import strftime
from tkinter import *

window = Tk()
window.title("Clock")
window.config(background='black')
window.attributes("-alpha", 0.5) # Makes window transparent
window.geometry('400x175')


# Gets current time
def currenttime():
    timestring = strftime('%H:%M:%S')
    lbl2.config(text=timestring)
    lbl2.after(1000, currenttime)

# Gets current date
def datetime():
    datestring = strftime('%Y-%m-%d')
    lbl3.config(text=datestring)
    lbl3.after(1000, datetime)

# Label configuration
lbl1 = Label(window, font=('San Francisco', 40, 'italic'), background='black',foreground='white', text="Time:")
lbl2 = Label(window, font=('San Francisco', 40, 'italic'),background='black', foreground='white')
lbl3 = Label(window, font=('San Francisco', 40, 'italic'),background='black', foreground='white')

# Finishing
lbl1.pack()
lbl2.pack()
lbl3.pack()
currenttime()
datetime()
window.mainloop()