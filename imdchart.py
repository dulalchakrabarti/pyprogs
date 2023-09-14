from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
im = Image.open('850bl.png')
print(im.format, im.size, im.mode)
#r, g, b, a = im.split()
# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)
#im.show()
 
box = (100, 100, 240, 240)
region = im.crop(box)
region = region.transpose(Image.Transpose.ROTATE_180)
#im.paste(region, box)
region.show()

