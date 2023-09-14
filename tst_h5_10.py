import h5py
import numpy as np
from PIL import Image
import glob
import re
from time import sleep
from math import *
import cv2


count = 0
for name in glob.glob('3DIMG*.h5'):
 f = h5py.File(name, 'r+')
 f.keys()
 f.values()
 members = []
 f.visit(members.append)
 for i in range(len(members)):
    sub = members[i]
    if sub[:4] == 'IMG_':
     time = re.findall(r'\d+', name)
     with h5py.File(name, mode='r') as f:
      chan = '/'+sub
      data = f[chan][:]
      if len(data.shape)>2:
       status=cv2.imwrite(sub+time[3]+str(count)+'.tif',data[0])
       print 'Saved.....'+sub+time[3]+str(count),status
       sleep(5)

'''
       count = count+1
       cv2.imwrite(sub+time[3]+str(count)+'.tif',data[0])
       print 'Saved.....'+sub+time[3]+str(count)
       sleep(5)
#im1 = cv2.imread('IMG_MIR06001.tif')
img_np = np.ones([100,100])*100
for i in range(len(img_np)):
 if i%5 == 0:
  img_np[i] = 0
 else:
  img_np[i] = img_np[i]*i
cv2.imshow('image',img_np)
cv2.waitKey(0)

im1 = cv2.imread('IMG_MIR06001.tif')
im2 = cv2.imread('IMG_MIR06001.jpg')
b,g,r = cv2.split(im1)
print b
print im1.shape,im2.shape

img_np = np.ones([100,100])
print img_np
print  '--------------'
img_cv = cv2.resize(img_np,(200,200))
print img_cv
cv2.imshow('image',img_cv)
cv2.waitKey(0)
       im = data[0]
       #im = im.convert("L")
       count = count+1
       cv2.imwrite(sub+time[3]+str(count)+'.tif',im)
       print 'Saved.....'+sub+time[3]+str(count)
       sleep(5)
'''


