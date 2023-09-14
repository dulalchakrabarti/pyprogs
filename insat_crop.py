#input:insat image
#output: writes to a directory 'insatout'
import cv2
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import glob
from datetime import datetime
dir_list = ['insatin']
for item in dir_list:
 for name in glob.glob(item+'/*.jpg'):
  mon = name.split('_')
  date = mon[1]
  time = mon[2]
  # Read original image
  img = cv2.imread(name)
  # Get width and height of the image
  if img is not None:
   height,width,channel = img.shape
   # Define a region of interest which is a small green strip from the bottom
   top = height - 1210
   bottom = height - 550
   left = 480
   right = width - 160
   roi = img[top:bottom,left:right]
   #print 'writing '+ 'ifprimar18/'+name[11:]
   crop = 'insatout/'+date+time+'.jpg'
   cv2.imwrite(crop,roi)
img = cv2.imread(crop)
height,width,channel = img.shape
ht = height/10
wt = width/10
for idx1 in range(10):
 for idx2 in range(10):
  roi = img[idx1*ht:(idx1+1)*ht,idx2*wt:(idx2+1)*wt]
  cv2.imwrite('insatout/'+date+time+str(idx1)+str(idx2)+'.jpg',roi)

