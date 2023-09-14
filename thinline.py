#input:globs JPG images recursively and crops from bottom 88x88x3 rois
#output: writes to a directory 'ifprimar18'
import cv2
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
img = cv2.imread('850bl.png')
   # Get width and height of the image
if img is not None:
 print(img.shape)
 height,width,channel = img.shape
 # Define a region of interest which is a small green strip from the bottom
 h1=height-100
 h2=height
 w1 = width//2
 w2 = w1+100
 print(h1,h2,w1,w2)
 for i in range(0,height,200):
  for j in range(0,width,200):
   roi = img[i:i+200,j:j+200]
   cv2.imshow('roi',roi)
   cv2.waitKey(240) 
   cv2.destroyAllWindows()
  
