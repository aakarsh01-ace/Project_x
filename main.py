#importing the libraries
import numpy as np
import pandas as pd

#pathlib allows you to handle files and folders in a minimal or efficient way possible
from pathlib import Path
import os.path
import matplotlib.pyplot as plt
import tensorflow as tf

# this below snippet imports 2 functinos, load_image and img_to_array from the image module. The 'load_img' 
# function loads a single image from file,
# and returns PIL image object (this represents an image loaded and stored in memory) and 
# the 'img_to_array' function converts the PIL image object to numpy array.
from tensorflow.keras.preprocessing.image import load_img,img_to_array

print(tf.__version__)
