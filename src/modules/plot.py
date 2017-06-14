#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def plot_data_dict(main_dict, spatial_freq):
	pass

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
