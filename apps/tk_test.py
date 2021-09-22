from tkinter import *
from PIL import ImageTk, Image
from meta_scrape import metaScorePages
from playlist_app import get_week_num
import numpy as np
import matplotlib.pyplot as plt
# set instance of tkinter
root = Tk()
# set title
root.title('Create Playlist from meta_scrape')
# set window size
root.geometry('800x800')
# create variable for weeknum and default input for 
week_num = IntVar(root, value = get_week_num())
# label widget
def myClick():
    metaScorePages(week_num.get())
    print(week_num)

def myClick2():
    # create_playlist()
    print()
e = Entry(root, textvariable=week_num, width=2)

# button
myButton = Button(root, text='Run app for week: ', command=myClick)
myButton2 = Button(root,text='Run create_playlist', command=myClick2)
#  grid
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
e.grid(row=2, column=1)
myButton.grid(row=2, column=0)
myButton2.grid(row=3, column=0)
# event loop
root.mainloop()

