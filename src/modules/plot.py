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
	plt.plot(special_freqs,fit_data)
	plt.errorbar(spatial_freqs, y,fmt='s', yerr = y_err)
	plt.show()

def fit(x,y,y_err,model):
	"""
	This function uses a scipy method to fit the parameters to the given x,y data.
	"""
	fitted_output = curve_fit(model,x,y,p0=4,sigma=y_err)
	a,b = fitted_output[0]
	a_covariance = fitted_output[1]
	return a,b,a_covariance

def model(x,a,b):
	# SOD and SDD in µm
	source_object_dist = 15.819*1000
	source_detector_dist = 1067.1*1000

	d_2 = source_detector_dist - source_object_dist
	d_1 = source_object_dist

	r = d_2/d_1

	return ((np.sin(np.pi*x*a*r))/(np.pi*x*a*r))+b
