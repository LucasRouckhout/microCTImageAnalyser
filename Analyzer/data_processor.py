#!/usr/bin/env python3

import afbeeldingen.py as afb
import pandas as pd
import numpy as np

def create_data_frame(images, positions):
  
  main_dict = {}

  for image in images:

    modulations = []
    for position in positions:
      modulations.append(get_modulation(image, position)

    main_dict[get_voltage(image)] = modulations
  
  return pd.DataFrame(main_dict)

def get_modulation(image, position, spacing = 10):
  
  lines = []
  for count in range(5):
    lines.append(afb.Read_Image(image, position[1], position[2],
    position[3]+count*spacing))
  
  def modulation(line):
    return (max(line)-min(line))/(max(line)+min(line))
  
  return map(modulation, lines)

  
def get_voltage(image):
  """
  Given an image path this functions returns the value for the voltage
  at which this image was taken. 

  Args:
    image (str): A string representing the path to the image file.

  Returns:
    voltage (int): An integer representing the voltage.
  """
  pass
