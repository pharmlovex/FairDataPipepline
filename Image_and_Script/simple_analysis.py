# Simple image Analysis 

import tifffile as tf
import skimage
import pandas as pd 
import os 
import numpy as np
import platform
import data_pipeline_api as pipeline


token = str(os.environ.get("FDP_LOCAL_TOKEN"))
script = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "script.sh")
if platform.system() == "Windows":
    script = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "script.bat")
config = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "config.yaml")
handle = pipeline.initialise(token, config, script)

# Read the image data into the script.
image_data = tf.imread(pipeline.link_read(handle, "Ryan_analysis/image"))

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
tf.imwrite(pipeline.link_write(handle, "Ryan_analysis/results/figure"),labels)

# Use Pandas to save shape analysis as a .csv file. 
mask_data.to_csv(pipeline.link_write(handle, "Ryan_analysis/results/analysis"))

pipeline.finalise(token, handle)