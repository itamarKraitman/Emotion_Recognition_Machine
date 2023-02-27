import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image") # the path to the input image
ap.add_argument("-p", "--prototext", required=True, help="path to Caffe 'deploy' prototext file") # the path to the caffe file
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-traind model") # the path to the pretraind Caffe model
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

#check if works




