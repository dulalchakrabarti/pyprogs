# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image

from PIL import GifImagePlugin
im = Image.open("../sat/BT.gif").convert('L')
pixels = list(im.getdata())
col,row = im.size
for i  in  range(col):
 for j in range(row):
  k = i*j + col
  print pixels[k],
 print'--------------------------------------------'




