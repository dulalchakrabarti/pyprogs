from PIL import Image, ImageDraw
import math
im = Image.open("3Dasiasec_ir2.jpg","r")
pixels = list(im.getdata())
pix1 = []
for set  in  pixels:
 s = sum(set) / len(set)
 pix1.append(s)
im = Image.open("3Dasiasec_ir1.jpg","r")
pixels = list(im.getdata())
pix2 = []
for set  in  pixels:
 s = sum(set) / len(set)
 pix2.append(s)
im = Image.new("L",(1260, 1580))
pix3=[]
for i in range(len(pix1)):
 pix3.append(pix1[i] - pix2[i])
im.putdata(pix3)
im.save("test.jpg")

