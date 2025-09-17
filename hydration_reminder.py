# Import tkinter
from tkinter import *
# Import PIL
from PIL import *
# Import time
from datetime import datetime
from time import *

import pytz

root = Tk()

# root window title
root.title("Hydration Reminder")

drink_remainder = 100
drink_timer = False
# root geometry
# root.geometry('800x600')
# update function
def update_app():
        global drink_timer
        global drink_remainder
        italy_timezone = datetime.now(pytz.timezone('Europe/Rome'))
        philippines_timezone = datetime.now(pytz.timezone('Asia/Manila'))
        italy_time = italy_timezone.strftime('%H:%M:%S')
        philippines_time = philippines_timezone.strftime('%H:%M:%S')
        italy_lbl.config(text=italy_time)
        philippines_lbl.config(text=philippines_time)
        if drink_timer and drink_remainder > 0:
                drink_remainder -= 1
        elif drink_timer and drink_remainder == 0:
                drink_warning()
        print(drink_remainder)
        root.after(1000, update_app)
# function drink
def drink():
        global drink_timer
        global drink_remainder
        print("Drinkin! Time start")
        drink_timer = True
        if drink_remainder < 100:
                drink_remainder = 100
def drink_warning():
        global drink_timer
        drink_timer = False
        print("DONE!")
# adding label
italy_lbl = Label(root)
philippines_lbl = Label(root)
italy_lbl.grid(column=0, row=0)
philippines_lbl.grid(column=2, row=0)
# button for drink
drink_btn = Button(root, text="Drink!", command=drink)
drink_btn.grid(column=1, row=1)
update_app()
mainloop()