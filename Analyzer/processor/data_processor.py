#!/usr/bin/env python3

import numpy as np

def create_data_dictionary(images, positions):
  """
  This function generates a dictionary using the voltage at which an image is
  taken as keywords. Each keyword is connected to a list containg tuples of 
  the modulation at a given spatial frequency and the corresponding standard
  deviation on that modulation. As we wish to plot these values later on the 
  list of modulations is order in the same way as the spatial frequencies.

  Args:
    images (list of str): A list of strings representing the path to the image
      files.
    positions (list): A list of lists formatted in a specific way which contains
      all the information on the positions and the spatial frequency at these 
      positions. See help(get_modulations()) for specifics on the used format.

  Returns:
    main_dict (dict): The dictionary described in the main body of this docstring.
  """
  main_dict = {}

  for image in images:
    
    modulations = []
    for position in positions:
      modulations.append(get_modulation(image, position))

    main_dict[get_voltage(image)] = modulations
  
  return main_dict

def get_modulation(image, position, spacing = 10):
  """
  This function calculates the intensity modulation at a specific position
  on the image. 

  Args: 
    image (str): path the image file.
    position (list): a list containing all the information on a specifc position.
      formatted as such [linepairs/distance, x_initial, x_final, y]

  Returns:
    A list containing the average modulation at that position and the standard 
      deviation.
  """
  lines = []
  for count in range(5):
    lines.append(afb.Read_Image(image, position[1], position[2],
    position[3]+count*spacing))
  
  def modulation(line):
    return (max(line)-min(line))/(max(line)+min(line))
  
  modulation = map(modulation, lines)
  return [np.average(modulation), np.std(modulation)]

  
def get_voltage(image):
  """
  Given an image path this functions returns the value for the voltage
  at which this image was taken. 

  Args:
    image (str): A string representing the path to the image file.

  Returns:
    voltage (int): An integer representing the voltage.
  """
  return 5
