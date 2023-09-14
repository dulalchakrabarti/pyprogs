from PIL import Image
import numpy as np
 
im = Image.open('500.png')
im = im.convert('RGBA')
 
data = np.array(im)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
 
# Replace black with red... (leaves alpha values alone...)
black_areas = (red < 180) & (blue < 180) & (green < 180)
data[..., :-1][black_areas.T] = (255, 0, 0) # Transpose back needed
 
im2 = Image.fromarray(data)
im2.save('500_.png')
