#!/usr/bin/env python

from tkinter import *
import sys

def run():
  root = Tk()
  root.title("microCT image processor")
  browse_btn_pos = Button(root, text="Browse", command=browse_position)
  browse_btn_pos.pack(side=LEFT, expand=YES)
  
  quit_btn = Button(root, text="Quit", command=quit)
  quit_btn.pack(side=RIGHT, expand=YES)

  root.mainloop()
  
def quit():
  sys.exit()

def browse_position():
  pass
