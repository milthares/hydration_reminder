# pyinstaller --onefile hydration_reminder.py --noconsole --hidden-import plyer.platforms.win.notification
# Imports
from tkinter import *
from datetime import datetime
from time import *
from plyer import *
from PIL import *
import pytz
# Globals
class globals():
  is_reminding = False
  is_mute = False
  is_mute_next = False
  empty = False
  half = False
  full = False
# WindowSettings
root = Tk()
root.title("Hydration Reminder")
root.geometry("250x250")
# BakcgroundImage
bg_logo = PhotoImage(file="assets\HydrationApp_logo_PH.png")
bg_empty = PhotoImage(file="assets\HydrationApp_empty_PH.png")
bg_half = PhotoImage(file="assets\HydrationApp_half_PH.png")
bg_full = PhotoImage(file="assets\HydrationApp_full_PH.png")
# Canvas
canvas = Canvas(root, width=250, height=250)
canvas.pack(fill="both", expand=True)
# DisplayImage
background_image = canvas.create_image(0, 0, image=bg_logo, anchor="nw")
# Text
text_id = canvas.create_text(125, 50, text = "Loading...")
# Radios
reminder_timer = IntVar()
time_one = Radiobutton(root, text="15", variable=reminder_timer, value=15)
time_two = Radiobutton(root, text="30", variable=reminder_timer, value=30)
time_three = Radiobutton(root, text="60", variable=reminder_timer, value=60)
time_one.select()
# DisplayRadios
radio_one_canvas = canvas.create_window(40, 200, anchor="nw", window=time_one)
radio_two_canvas = canvas.create_window(110, 200, anchor="nw", window=time_two)
radio_three_canvas = canvas.create_window(190, 200, anchor="nw", window=time_three)
# update function
def update_app():
  timezone = datetime.now(pytz.timezone('Europe/Rome'))
  time = timezone.strftime('%H:%M')
  canvas.itemconfig(text_id, text=time)
  match reminder_timer.get():
    case 15:
      if (timezone.minute % reminder_timer.get()) > 0 and (timezone.minute % reminder_timer.get()) < 5 and not globals.empty:
        canvas.itemconfig(background_image, image=bg_empty)
        print("EMPTY")
        globals.empty = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) >= 5 and (timezone.minute % reminder_timer.get()) < 10 and not globals.half:
        canvas.itemconfig(background_image, image=bg_half)
        print("HALF")
        globals.half = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) >= 10 and (timezone.minute % reminder_timer.get()) < 15 and not globals.full:
        canvas.itemconfig(background_image, image=bg_full)
        print("FULL")
        globals.full = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) == 0 or timezone.minute == 0:
        globals.empty = False
        globals.half = False
        globals.full = False
        reminder()
    case 30:
      if (timezone.minute % reminder_timer.get()) > 0 and (timezone.minute % reminder_timer.get()) < 10 and not globals.empty:
        canvas.itemconfig(background_image, image=bg_empty)
        globals.empty = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) >= 10 and (timezone.minute % reminder_timer.get()) < 20 and not globals.half:
        canvas.itemconfig(background_image, image=bg_half)
        globals.half = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) >= 20 and (timezone.minute % reminder_timer.get()) < 30 and not globals.full:
        canvas.itemconfig(background_image, image=bg_full)
        globals.full = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) == 0 or timezone.minute == 0:
        reminder()
    case 60:
      if (timezone.minute % reminder_timer.get()) > 0 and (timezone.minute % reminder_timer.get()) < 20 and not globals.empty:
        canvas.itemconfig(background_image, image=bg_empty)
        globals.empty = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) >= 20 and (timezone.minute % reminder_timer.get()) < 40 and not globals.half:
        canvas.itemconfig(background_image, image=bg_half)
        globals.half = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) >= 40 and (timezone.minute % reminder_timer.get()) <= 59 and not globals.full:
        canvas.itemconfig(background_image, image=bg_full)
        globals.full = True
        globals.is_reminding = False
        globals.is_mute_next = False
      elif (timezone.minute % reminder_timer.get()) == 0 or timezone.minute == 0:
        reminder()
  root.after(1000, update_app)
# reminder
def reminder():
  if not globals.is_reminding:
    globals.is_reminding = True
    notification.notify(
      title = 'Hydration App',
      message = "It's time to drink!",
      app_icon = None,
      timeout = 5,
    )
update_app()
mainloop()