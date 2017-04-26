#!/usr/bin/env python3

import glob

def retrieve_data(images_map, positon_file, file_names = "normalised_*.tif"):
  """
  This functions returns a list of image paths and a list of positions.
  """
  images = glob.glob(images_map+file_names)
  positions = retrieve_positions(position_file)
  
  return images, positions

def retrieve_positions(position_file):
  try:
    position_lines = open(position_file, 'r').readlines()
    positions = [line.split() for line in position_lines]
    return positions

  except(IOError, e):
    raise e
