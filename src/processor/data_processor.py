#!/usr/bin/env python3

import sys
import numpy as np
from modules import afbeeldingen as afb
import random as rnd
from modules import inp as inp
from modules import plot as plot
import os

def create_data_dictionary(images, positions, main_frame):
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
	"""
	# First close the gui.
	main_frame.destroy()
	# Initialise the needed variables.
	run = False
	main_dict = {}
	spatial_freqs = [pos[0] for pos in positions]

	# Start looping over all the images.
	for image in images:

	# Reset the modulations list.
	modulations = []

	# Get the modulation for each position on the image.
	for position in positions:
		modulations.append(get_modulation(image, position))

	# Add these modulations to the main dictionary.
	main_dict[get_voltage(image)] = modulations

	# Ask the user for input if run is False.
	if not run:
		print(":: Processed image {}\n:: What would you like to"\
				" do?".format(os.path.basename(image)))
		reply = inp.ask()
		run = execute_user_input(reply, spatial_freqs, modulations, image)
	else:
		print(":: Processed image {}".format(os.path.basename(image)))

	# When the loop is done with all the images ask what to do with the
	# main_dict.
	print(":: Processed all the images!\n:: Finalize or quit?")
	reply = inp.ask()
	finalize(main_dict)

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
		lines.append(afb.Read_Image(image,True,int(position[1]), int(position[2]),
			int(position[3])+count*spacing))

	def modulation(line):
		return (max(line)-min(line))/(max(line)+min(line))

	modulation = [modulation(line) for line in lines]
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
	name = os.path.basename(image)

	return int(name[:2])

def execute_user_input(reply, spatial_freqs, modulations, image):
	"""
	This function controls the execution of commandline inputs from the user. 
	It returns the boolean value for the run variable.

	Args:
		reply (str): A string containing the command from the user
		spatial_freqs (list):
	"""
	if reply == 'p':
		plot.plot_modulation_transfer(image, modulations, spatial_freqs)    
		print(":: Processing next image...")
		return False

	elif reply == "r":
		print(":: Processing next image...")
		return True

	else:
		print(":: Processing next image...")
		return False

def finalize(main_dict):

	print(":: Completed! If you see this we still need to implement finalize()")



