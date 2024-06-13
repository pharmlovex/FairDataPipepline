#!/usr/bin/env python
# coding: utf-8

# # Simple image Analysis 
# -----
# 
# All this does is read in a single frame from a time-lapse image of some dendritic cell nuclei, we'll segment out the cells and perform some shape analysis.   
# Parameters we will extract: 
# - Number of nuclei.
# - Area of each nuclei 
# - The eccentricity of the nuclei
# - Circumference of the nuclei

# In[ ]:

### Import dependancies


# In[1]:


import tifffile as tf
import skimage
import pandas as pd 
import os 
import numpy as np


# ----
# ### Get Current working directory 

# In[15]:


cwd = os.getcwd()


# ----
# ### Import image

# In[23]:


# Read the image data into the script.
image_data = tf.imread(cwd + 'Image_and_Script/single_frame_image.tif')
# Copy image data so as not to corrupt raw data. 
im_data_copy = np.array(image_data)


# ----
# ### Threshold and Segment out the cells.

# In[24]:


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


# ---
# ### Perform the shape analysis of the nuclei

# In[25]:


# Get nuclei mask shape properties. 
mask_data = pd.DataFrame(skimage.measure.regionprops_table(labels, properties = props))


# # Save the Outputs. 

# In[22]:


# Use tifffile to save the cell masks. 
tf.imwrite(cwd + '/single_frame_image_mask.tif', labels)

# Use Pandas to save shape analysis as a 
# .csv file. 
mask_data.to_csv(cwd + '/single_frame_shape_analysis.csv')

