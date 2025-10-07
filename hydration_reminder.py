# pyinstaller --onefile hydration_reminder.py --noconsole --hidden-import plyer.platforms.win.notification
# Imports
from tkinter import *
from datetime import datetime
from time import *
from plyer import *
from PIL import *
import pytz
# Globals
is_reminding = False
# WindowSettings
root = Tk()
root.title("Hydration Reminder")
root.geometry("250x250")
# BakcgroundImage
bg = PhotoImage(file="assets\\HydrationApp_background.png")
# Canvas
canvas = Canvas(root, width=250, height=250)
canvas.pack(fill="both", expand=True)
# DisplayImage
canvas.create_image(0, 0, image=bg, anchor="nw")
# Text
text_id = canvas.create_text(125, 10, text = "Loading...")
# Radios
reminder_timer = IntVar()
time_one = Radiobutton(root, text="15", variable=reminder_timer, value=15)
time_two = Radiobutton(root, text="20", variable=reminder_timer, value=20)
time_three = Radiobutton(root, text="30", variable=reminder_timer, value=30)
# DisplayRadios
radio1_canvas = canvas.create_window(40, 50, anchor="nw", window=time_one)
radio2_canvas = canvas.create_window(80, 50, anchor="nw", window=time_two)
radio3_canvas = canvas.create_window(120, 50, anchor="nw", window=time_three)
# update function
def update_app():
  global is_reminding
  global reminder_timer
  timezone = datetime.now(pytz.timezone('Europe/Rome'))
  time = timezone.strftime('%H:%M:%S')
  # trigger notification based on time chosen
  # lbl.config(text=time)
  canvas.itemconfig(text_id, text=time)
  print(is_reminding, reminder_timer.get())
  match reminder_timer.get():
    case 15 | 20 | 30:
      if timezone.minute == 0 or (timezone.minute % reminder_timer.get()) == 0:
        reminder()
      else:
        is_reminding = False
  root.after(1000, update_app)
# reminder
def reminder():
  global is_reminding
  global toast
  if not is_reminding:
    is_reminding = True
    notification.notify(
      title = 'Test',
      message = 'Message',
      app_icon = None,
      timeout = 5,
    )
  else:
    pass
update_app()
mainloop()