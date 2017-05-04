#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 10:54:03 2015

@author: amelie
"""

import matplotlib.pyplot as plt
from matplotlib import image as mpimg
import numpy as np
from PIL import Image

from os import listdir
from os.path import isfile, join

# Load the image
def Read_Image(filename,Selection=False,Lower_X=None,Upper_X=None,Lower_Y=None,Upper_Y=None):
    
    im = Image.open(filename)
    Tags = im.tag
    offset = __Get_Offset(Tags)
    slope = __Get_Slope(Tags)
    Pixel_Array = np.array(im)
    
    Low_X = 0
    Low_Y = 0
    High_X = len(Pixel_Array[0])
    High_Y = len(Pixel_Array[0])  
    if Selection:
        if Lower_X!=None:
            Low_X = Lower_X
        if Lower_Y!=None:
            Low_Y = Lower_Y
        if Upper_X!=None:
            High_X = Upper_X
        if Upper_Y!=None:
            High_Y = Upper_Y
        
        return [float(slope)*float(Pixel_Array[Low_Y][i]) + float(offset[:-2]) for i in range(Low_X,High_X)]


    out = []
    for i in range(Low_X,High_X):
        out_Row =[]
        for j in range(Low_Y,High_Y):
             out_Row.append(float(float(slope)*float(Pixel_Array[j][i]) + float(offset)))
        out.append(out_Row)
    return out



#A Dictionary is received containing the Header Tags from the Image
#This function returns the Offset Value
def __Get_Offset(Tags):
    for key in Tags:
        offset =  str(Tags[270])[34:45]
    return offset

#A Dictionary is received containing the Header Tags from the Image
#This function returns the Slope Value    
def __Get_Slope(Tags):
    for key in Tags:
        slope =  str(Tags[270])[11:22]
    return slope


'''
# Show the result
plt.imshow(img, clim=(0.9,1.01), cmap=plt.cm.gray) #plot enkel in grijswaarden, clim veranderen of weglaten bij niet-genormalisserde beelden
plt.axis('off')
plt.colorbar()
plt.figure()
plt.imshow(img)
plt.axis('off')
'''
# The normal way to apply the offsets
'''
    out = []
    for i in range(Low_X,High_X):
        out_Row =[]
        for j in range(Low_Y,High_Y):
            out_Row.append(float(float(slope)*float(Pixel_Array[j][i]) + float(offset)))
        out.append(out_Row)
    return out
    '''
