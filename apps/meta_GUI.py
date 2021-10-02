from tkinter import *
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from meta_scrape import metaScorePages
from playlist_app import get_week_num
from meta_db import *

matplotlib.use('TkAgg')
#set instance of tk
window = tk.Tk()
#set title
window.title('Create Playlist from meta_scrape')
#set window size
window.geometry('800x800')
# window.state('zoomed')
# set week_num variable to current week
week_num = IntVar(window, value = get_week_num())
# meta_db connection
def dbconnection(week_num):
    connection = sqlite3.connect('../data/historical_data/meta_music.db')
    cursor = connection.cursor()
    select_query = """SELECT artist, album, meta_score FROM albums WHERE """
    cursor.execute()
# import scrape module and set to week_num variable to value in week field
def scrape():
    metaScorePages(week_num.get())
# set plotting function

def plot():
    datalst = [31, 41, 59, 26, 53, 58, 97, 96, 36]
    ff = Figure(figsize=(6,6), dpi=100)
    xx = ff.add_subplot(111)
    ind = np.arange(len(datalst))
    rects1 = xx.bar(ind, datalst, 0.8)
    canvas = FigureCanvasTkAgg(ff, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT)
# create button for scrape
scraper = tk.Button(window,text='Run Scrape for week number:',command=scrape, height=1,width=25,state='normal')
scraper.place(x=12, y=20)
# create field for week num variable
week_field = Entry(window, textvariable=week_num, width=2)
week_field.place(x=270, y=22)
# create button for plot
plotter = tk.Button(window,text='plot',command=plot, height=1,width=25,state='normal')
plotter.place(x=12, y=45)

window.mainloop()

