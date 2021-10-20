from os import initgroups
from tkinter import *
import csv
import numpy as np
from more_itertools import unique_everseen
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from meta_scrape import metaScorePages
from playlist_app import get_week_num
from credentials.config import scrape_path, clean_path


#set instance of tk
window = tk.Tk()
#set title
window.title('Create Playlist from meta_scrape')
#set window size
window.geometry('800x800')
week_num = get_week_num()
scrape_path = scrape_path
clean_path = clean_path
class MetaGUI:

    def __init__(self, master):
        self.myFrame = Frame(master)
        # create button for scrape
        self.scraperButton = tk.Button(window,text='Run Scrape for week number:',command=self.scrape, height=1,width=25,state='normal')
        self.scraperButton.place(x=12, y=20)
        # create ffield for week num variable
        self.weekField = Entry(window, textvariable=week_num, width=2)
        self.weekField.place(x=270, y=22)
        # create_depuped_csv
        self.cleanerButton = tk.Button(window,text=' dedup csv',command=self.dedup, height=1,width=25,state='normal')
        self.cleanerButton.place(x=12, y=45)
        # create button for plot and table
        self.plotterButton = tk.Button(window,text='plot',command=self.plot, height=1,width=25,state='normal')
        self.plotterButton.place(x=12, y=70)

        # # set week_num variable to current week
    def weekNum(self):
        self.week_value = IntVar(window, value = week_num)

        # # import scrape module and set to week_num variable to value in week field
    def scrape(self):
        self.metaScorePages(week_num.get())

    def getData(self):
        scrape_dict = {
            'datalst': [],
            'albumlst': [],
            'artistlst': []
        }
        file_path = os.path.join('..', 'data', 'clean_meta_scrape.csv')
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if int(row['week_num']) == week_num.get():
                    scrape_dict['datalst'].append(row['meta_score'])
                    scrape_dict['albumlst'].append(row['album'])
                    scrape_dict['artistlst'].append(row['artist']) 
        return scrape_dict

    def dedup(self, scrape_path, clean_path):
        with open(scrape_path,'r') as f, open(clean_path,'w') as out_file:
            out_file.writelines(unique_everseen(f))
    

    def createTable(self):
       
        # Create an object of Style widget
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Add a Treeview widget
        self.tree = ttk.Treeview(window, column=("FName", "LName", "Roll No"), show='headings', height=5)
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="FName")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="LName")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Roll No")

        # Insert the data in Treeview widget
        self.tree.insert('', 'end', text="1", values=(meta_dict['artistlst']))
        self.tree.insert('', 'end', text="1", values=(meta_dict['albumlst']))
        self.tree.insert('', 'end', text="1", values=(meta_dict['datalst']))
        self.tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
        self.tree.place(x=12, y=600)
    # from meta_db import *

    # matplotlib.use('TkAgg')

    # # window.state('zoomed')
    # set week_num variable to current week
    week_num = IntVar(window, value = get_week_num())
    # import meta_scrape data for plot


 



   
    # created fig in tkinter
    fig = Figure(figsize=(6,6), dpi=100)
    chart = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=window)

gui = MetaGUI(window)

window.mainloop()

