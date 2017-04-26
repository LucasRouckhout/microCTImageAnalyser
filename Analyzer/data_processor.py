#!/usr/bin/env python3

import afbeeldingen.py as afb
import pandas as pd
import numpy as np

def create_data_frame(images, positions):
  df_main = pd.DataFrame()
  linepairs_per_distance = [position[0] for position in positions]
  
  df_main.set_index(linepairs_per_distance)

  for image in images:
    break

