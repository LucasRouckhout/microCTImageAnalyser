#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt

def plot_data_dict(main_dict, spatial_freq):
	pass

def plot_modulation_transfer(image, modulations, spatial_freqs):
	plt.figure()
	plt.xlabel("Spatial Frequency")
	plt.ylabel("Modulation")
	plt.title("Modulation transfer function"\
	" of image: {}".format(os.path.basename(image)))
	y = [modulation[0] for modulation in modulations]
	plt.plot(spatial_freqs, y)
	plt.show()
