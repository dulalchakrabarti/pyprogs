from PIL import Image
import numpy as np
 
im = Image.open('850.png')
im = im.convert('RGBA')
 
data = np.array(im)   # "data" is a height x width x 4 numpy array
print(data.shape)
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
 
# Replace black with blue... (leaves alpha values alone...)
black_areas = (red < 240) & (blue < 240) & (green < 240)
data[..., :-1][black_areas.T] = (0, 0, 255) # Transpose back needed
 
im2 = Image.fromarray(data)
im2.save('850bl.png')
