import os
import platform
from imgAnalysis import process_image
import sys


image_mask = "mask" 
image_prop = "prop" 
image_file = "single_frame_image.tif" 

process_image(image_file, image_prop, image_mask)


