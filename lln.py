# Reading an animated GIF file using Python Image Processing Library - Pillow
import cv2
from PIL import Image

from PIL import GifImagePlugin
import os

def com1com2(fr):
    '''
    '''
    if fr == 0:
     com1 = 'gdal_translate -of GTiff -gcp 17.5156 217.052 69.0279 22.387 -gcp 169.572 386.348 79.9403 10.2934 -gcp 409.954 151.245 97.1525 27.112 "/home/dc/codes/0.jpg" "/tmp/0.jpg"'
     com2 = 'gdalwarp -r near -order 1 -co COMPRESS=NONE  -t_srs EPSG:4326 "/tmp/0.jpg" "/home/dc/codes/0_modified.tif"'
    elif fr == 1:
     com1 = 'gdal_translate -of GTiff -gcp 17.5156 217.052 69.0279 22.387 -gcp 169.572 386.348 79.9403 10.2934 -gcp 409.954 151.245 97.1525 27.112 "/home/dc/codes/1.jpg" "/tmp/1.jpg"'
     com2 = 'gdalwarp -r near -order 1 -co COMPRESS=NONE  -t_srs EPSG:4326 "/tmp/1.jpg" "/home/dc/codes/1_modified.tif"'
    elif fr == 2:
     com1 = 'gdal_translate -of GTiff -gcp 17.5156 217.052 69.0279 22.387 -gcp 169.572 386.348 79.9403 10.2934 -gcp 409.954 151.245 97.1525 27.112 "/home/dc/codes/2.jpg" "/tmp/2.jpg"'
     com2 = 'gdalwarp -r near -order 1 -co COMPRESS=NONE  -t_srs EPSG:4326 "/tmp/2.jpg" "/home/dc/codes/2_modified.tif"'
    return (com1,com2)

imageObject = Image.open("./BT.gif")

#print(imageObject.is_animated)

#print(imageObject.n_frames)

 

# Display individual frames from the loaded animated GIF file

for frame in range(0,imageObject.n_frames):
    imageObject.seek(frame)
    imageObject.convert('RGB').save(str(frame)+'_.jpg')
    img = cv2.imread(str(frame)+'_.jpg')
    height,width,channel = img.shape
    roi = img[125:height-100,200:width-250]
    cv2.imwrite(str(frame)+'.jpg',roi)
    txt1,txt2 = com1com2(frame)
    com1 = txt1
    com2 = txt2
    result = os.system(com1)
    if result == 0:
     result = os.system(com2)
     print(str(frame)+' success-georeferenced')

