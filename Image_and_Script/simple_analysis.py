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
import platform
import data_pipeline_api as pipeline


# ----
# ### Get Current working directory 

# In[15]:

token = str(os.environ.get("FDP_LOCAL_TOKEN"))
#cwd = os.getcwd()
script = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "script.sh")
if platform.system() == "Windows":
    script = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "script.bat")
config = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "config.yaml")
handle = pipeline.initialise(token, config, script)


# ----
# ### Import image

# In[23]:


# Read the image data into the script.
image_data = tf.imread(pipeline.link_read(handle, 'python_basic/image'))
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
tf.imwrite(pipeline.link_write(handle, 'python_basic/results/figure', labels))

# Use Pandas to save shape analysis as a 
# .csv file. 
mask_data.to_csv(pipeline.link_write(handle, 'python_basic/results/analysis'))

pipeline.finalise(token, handle)
