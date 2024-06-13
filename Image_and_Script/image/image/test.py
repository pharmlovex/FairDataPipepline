import os
import platform
from imgAnalysis import process_image
import sys


image_mask = "mask" # os.path.dirname("mask")
image_prop = "prop" # os.path.dirname("prop")
image_file = "single_frame_image.tif" #os.path.basename("single_frame_image.tif")

process_image(image_file, image_prop, image_mask)


