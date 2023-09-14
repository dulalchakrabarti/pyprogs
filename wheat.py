# Shannon Entropy of an Image
# (min number of bits required to encode each color)
# FB - 201012131
import math
from PIL import Image
im = Image.open("w3.jpg","r")
pixels = list(im.getdata())
for p  in  pixels:
 pix = []
 red = p[0]
 green = p[1]
 blue = p[2]
 if red > green:
  if red > blue:
   pix.append("red")
 if green > red:
  if green > blue:
   pix.append("green")
 if blue > red:
  if blue > green:
   pix.append("blue")
 if "green" in pix:
  if red > blue:
   pix.append("red")
   pix.append("blue")
  else:
   pix.append("blue")
   pix.append("red")
 elif "red" in pix:
  if green > blue:
   pix.append("green")
   pix.append("blue")
  else:
   pix.append("blue")
   pix.append("green")
 elif "blue" in pix:
  if red > green:
   pix.append("red")
   pix.append("green")
  else:
   pix.append("green")
   pix.append("red")
 print pix,p


