#!/usr/bin/env python

from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import sys
from processor import data_processor as proc
from processor import data_retriever as retr
from processor import plot as plot

def run():
  MainFrame().mainloop()

class MainFrame(Tk):
  
  def __init__(self):
    super().__init__()
    self.title("microCT image processor")
    self.minsize(width=400, height=450)

    self.top_frame = TopFrame(self)
    self.top_frame.pack(side=TOP,expand=YES)

    self.middle_frame = MiddleFrame(self)
    self.middle_frame.pack(expand=YES)

    self.bottom_frame = BottomFrame(self)
    self.bottom_frame.pack(side=BOTTOM,expand=YES)
  
  def start(self):
    # Start the progressbar
    self.middle_frame.start_bar()
    # Retrieve the filepaths from the entry boxes
    images_map = self.top_frame.image_entry.get()
    position_file = self.top_frame.position_entry.get()
    # Check.get() returns 0 if the checkbox is off and 1 if on.
    check = self.top_frame.check.get()
    # Using the retrieve_data module we gain the images and positions variables
    # needed to run the dagta_processing module.
    images, positions = retr.retrieve_data(images_map, position_file,is_jima=check)
    # Create the data_dictionary.
    main_dict = create_data_dictionary(images, positions)


class TopFrame(Frame):
  
  def __init__(self, parent = None, **args):
    super().__init__(parent,**args)
    
    self.check = IntVar()

    jima_check = Checkbutton(self, text="Using JIMA pattern", variable=self.check)
    jima_check.pack(side=BOTTOM)
    
    left_frame = Frame(self)
    left_frame.pack(side=LEFT)
    
    right_frame = Frame(self)
    right_frame.pack(side=RIGHT)

    self.position_entry = Entry(left_frame)
    self.position_entry.pack(side=TOP)
    self.image_entry = Entry(left_frame)
    self.image_entry.pack(side=BOTTOM)

    self.pos_browse_btn = Button(right_frame, text="Browse", command=self.set_position_entry)
    self.pos_browse_btn.pack(side=TOP)

    self.image_browse_btn = Button(right_frame, text="Browse", command=self.set_image_entry)
    self.image_browse_btn.pack(side=BOTTOM)
    
  def set_position_entry(self):
    filename = filedialog.askopenfilename()
    self.position_entry.delete(0, 'end')
    self.position_entry.insert(0,filename)

  def set_image_entry(self):
    filename = filedialog.askdirectory()
    self.image_entry.delete(0,'end')
    self.image_entry.insert(0,filename)
    
class MiddleFrame(Frame):
  
  def __init__(self, parent = None, **args):
    super().__init__(parent, **args)
    
    self.progressbar = ttk.Progressbar(self,length=200,mode="indeterminate")
    self.progressbar.pack()
  
  def start_bar(self):
    self.progressbar.start()


class BottomFrame(Frame):
  def __init__(self, parent = None, **args):
    super().__init__(parent, args)

    Button(self,text="Start", command=parent.start).pack(side=LEFT)
    Button(self,text="Quit", command=sys.exit).pack(side=RIGHT)
