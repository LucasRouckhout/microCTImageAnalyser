#!/usr/bin/env python3

import glob

def retrieve_data(images_map, position_file,is_jima, file_glob = "normalised_*.tif"):
  """
  This functions returns a list of image paths and a list of positions.
  """
  images = glob.glob(images_map+"/"+file_glob)
  positions = retrieve_positions(position_file)
  
  return images, positions

def retrieve_positions(position_file):
  """
  This function returns a list of strings in the right format representing
  the positions that will be read out. [spatialfrequency,xi,xf,y].

  Args: 
    position_file (str): The path of the position file.

  Returns:
    positions (list,str): List representing the positions that will be read.
  """
  position_lines = open(position_file, 'r').readlines()
  positions = [line.split() for line in position_lines]
  return positions

