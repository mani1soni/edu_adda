# Simple GUI
# Imports
from tkinter import *
from datetime import datetime, time
from pytz import timezone

# Launch TK Root
root = Tk()
# set the peramiters
clock = Label(root, font=(style, fsize, 'bold'), bg=bgcolour)
# set the GUI Frame
clock.pack(fill=BOTH, expand=0)
# set the fromat of our clock
format = ("%d/%m/%y  %H:%M:%S")

# now to make the clock get the time so we make a function called tick


def tick():
    # get the current time now
    now = datetime.now(timezone('Australia/Adelaide'))
    # get the fromat we want
    now = str(now.strftime(format))
    # add the above configeration to the frame
    clock.config(text=now, height=fheight, width=fwidth)
    # and last but not least call our clock function to update the timezone
    # after 200 secconds TK will call the tick function again and we now have a loop
    clock.after(200, tick)


# call the fucntion for the first time
tick()
# loop the TK window
root.mainloop()
