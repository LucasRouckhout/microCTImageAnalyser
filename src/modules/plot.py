#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import re

def plot_data_dict(main_dict, spatial_freqs, power_setting):
	data = []
	ordered_images = sorted([image for image in main_dict])
	for image in ordered_images:
		modulations = main_dict[image]

		y = [modulation[0] for modulation in modulations]
		y_err = [modulation[1] for modulation in modulations]

		a,b,cov = fit(spatial_freqs, y, y_err,model)
		data.append([image,[a,cov[0][0]]])

	voltages = [point[0] for point in data]
	a = [point[1][0] for point in data]
	a_err = [point[1][1] for point in data]
	
	plt.figure()
	plt.xlabel("Voltages")
	plt.ylabel("Focal spotsize (µm)")
	plt.title("Focal spotsizes at {}W".format(power_setting))
	plt.errorbar(voltages,a,yerr = a_err, fmt='ro')
	plt.show()
	
def get_voltage(image):
	print(image)
	result = re.search('r"(?i)\d\dkV',str(image))
	return int(result.group(0))

def plot_modulation_transfer(image, modulations, spatial_freqs):
	# Make the figure and set all the text for the axis and title.
	plt.figure()
	plt.xlabel("Spatial Frequency")
	plt.ylabel("Modulation")
	plt.title("Modulation transfer function"\
	" of image: {}".format(os.path.basename(image)))

	# Create the y data and its errorbars given in modulations.
	y = [modulation[0] for modulation in modulations]
	y_err = [modulation[1] for modulation in modulations]
	
	# Create fitted function points.
	special_freqs = np.arange(0,spatial_freqs[len(spatial_freqs)-1],0.1)
	a,b,cov = fit(spatial_freqs,y,y_err,model)
	fit_data = [model(x,a,b) for x in special_freqs]

	# Plot and show.
	plt.plot(spatial_freqs, y,'co',special_freqs,fit_data)
	plt.text(1,1, 'Focal spotsize = {}'.format(a))
	plt.show()

def fit(x,y,y_err,model):
	"""
	This function uses a scipy method to fit the parameters to the given x,y data.
	"""
	fitted_output = curve_fit(model,x,y,sigma=y_err)
	a,b = fitted_output[0]
	covariance = fitted_output[1]
	return a,b,covariance

def model(x,a,b):
	return b*np.exp(-(x**2)/(2*a**2))
