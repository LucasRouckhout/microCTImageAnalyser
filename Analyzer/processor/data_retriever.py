#!/usr/bin/env python3

import glob

def retrieve_data(images_map, position_file,is_jima, file_glob = "normalised_*.tif"):
  """
  This functions returns a list of image paths and a list of positions.
  """
  images = glob.glob(images_map+"/"+file_glob)
  positions = retrieve_positions(str(position_file))
  
  return images, positions

def retrieve_positions(position_file):
  position_lines = open(position_file, 'r').readlines()
  positions = [list(map(float,line.split())) for line in position_lines]
  return positions

