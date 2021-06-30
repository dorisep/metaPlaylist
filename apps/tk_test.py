from tkinter import *
from meta_scrape import metaScorePages
from playlist_app import create_playlist
import csv
import matplotlib

root = Tk()
# label widget
def myClick():
    metaScorePages()
  

def myClick2():
    create_playlist()
   

myLabel1 = Label(root, text='hello world')
myLabel2 = Label(root, text='sup dude')
# button
myButton = Button(root, text='Run metaScrape', command=myClick)
myButton2 = Button(root,text='Run create_playlist', command=myClick2)
#  grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myButton.grid(row=2, column=0)
myButton2.grid(row=3, column=0)
# event loop
root.mainloop()

