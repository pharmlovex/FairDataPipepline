# Simple image Analysis 

import tifffile as tf
import skimage
import pandas as pd 
import os 
import numpy as np

cwd = os.getcwd()

# Read the image data into the script.
image_data = tf.imread(cwd + '/single_frame_image.tif')
# Copy image data so as not to corrupt raw data. 
im_data_copy = np.array(image_data)

# Initalise image_masks
image_masks = []

# Initalise image properties
props = {'Label', 'Area', 'Eccentricity', 'Perimeter'}

# Threshold the image
threshold = skimage.filters.threshold_otsu(im_data_copy)
im_data_copy[im_data_copy<threshold] = 0 
im_data_copy[im_data_copy>=threshold] = 1

# Create Labels from image. 
labels = skimage.measure.label(im_data_copy)

# Get nuclei mask shape properties. 
mask_data = pd.DataFrame(skimage.measure.regionprops_table(labels, properties = props))

# Use tifffile to save the cell masks. 
tf.imwrite(cwd + '/single_frame_image_mask.tif', labels)

# Use Pandas to save shape analysis as a 
# .csv file. 
mask_data.to_csv(cwd + '/single_frame_shape_analysis.csv')