import tifffile as tf
import skimage
import pandas as pd 
import os 
import numpy as np
import argparse

def process_image(file_path, mask_dir, prop_dir):
    # Read the image data into the script.
    image_data = tf.imread(file_path)
    # Copy image data so as not to corrupt raw data. 
    im_data_copy = np.array(image_data)

    image_masks = []

    # Initialize image properties
    props = ['label', 'area', 'eccentricity', 'perimeter']

    # Threshold the image
    threshold = skimage.filters.threshold_otsu(im_data_copy)
    im_data_copy[im_data_copy < threshold] = 0 
    im_data_copy[im_data_copy >= threshold] = 1

    # Create Labels from image. 
    labels = skimage.measure.label(im_data_copy)

    # Get nuclei mask shape properties. 
    mask_data = pd.DataFrame(skimage.measure.regionprops_table(labels, properties=props))

    # Use tifffile to save the cell masks. 
    output_mask_path = os.path.join(mask_dir + os.path.splitext(file_path)[0] + '_mask.tif')
    tf.imwrite(output_mask_path, labels)

    # Use Pandas to save shape analysis as a 
    # .csv file. 
    output_csv_path = os.path.join(prop_dir + os.path.splitext(file_path)[0] + '_shape_analysis.csv')
    mask_data.to_csv(output_csv_path)

def main():
    parser = argparse.ArgumentParser(description="Process a single-frame image and generate masks and shape analysis.")
    parser.add_argument('file_path', type=str, help="Path to the single-frame image file.")
    parser.add_argument('mask_dir', type=str, help="Path to the output image mask.")
    parser.add_argument('prop_dir', type=str, help="Path to the output image prop.")
    
    args = parser.parse_args()
    
    process_image(args.file_path,args.mask_dir, args.prop_dir)

if __name__ == '__main__':
    main()
