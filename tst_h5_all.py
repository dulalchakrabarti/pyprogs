import h5py
import numpy as np
from PIL import Image
import glob
import re
from time import sleep
from math import *

def map_uint16_to_uint8(img, lower_bound=None, upper_bound=None):
    '''
    Map a 16-bit image trough a lookup table to convert it to 8-bit.

    Parameters
    ----------
    img: numpy.ndarray[np.uint16]
        image that should be mapped
    lower_bound: int, optional
        lower bound of the range that should be mapped to ``[0, 255]``,
        value must be in the range ``[0, 65535]`` and smaller than `upper_bound`
        (defaults to ``numpy.min(img)``)
    upper_bound: int, optional
       upper bound of the range that should be mapped to ``[0, 255]``,
       value must be in the range ``[0, 65535]`` and larger than `lower_bound`
       (defaults to ``numpy.max(img)``)

    Returns
    -------
    numpy.ndarray[uint8]
    '''
    if not(0 <= lower_bound < 2**16) and lower_bound is not None:
        raise ValueError(
            '"lower_bound" must be in the range [0, 65535]')
    if not(0 <= upper_bound < 2**16) and upper_bound is not None:
        raise ValueError(
            '"upper_bound" must be in the range [0, 65535]')
    if lower_bound is None:
        lower_bound = np.min(img)
    if upper_bound is None:
        upper_bound = np.max(img)
    if lower_bound >= upper_bound:
        raise ValueError(
            '"lower_bound" must be smaller than "upper_bound"')
    lut = np.concatenate([
        np.zeros(lower_bound, dtype=np.uint16),
        np.linspace(0, 255, upper_bound - lower_bound).astype(np.uint16),
        np.ones(2**16 - upper_bound, dtype=np.uint16) * 255
    ])
    return lut[img].astype(np.uint8)

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
      data = np.ma.masked_where(np.isnan(data), data)
      if len(data.shape)>2:
       img8 = map_uint16_to_uint8(data[0])
       im = Image.fromarray(img8)
       im = im.convert("L")
       count = count+1
       im.save(sub+time[3]+str(count)+'.tif')
       print 'Saved.....'+sub+time[3]+str(count)
      else:
       im = Image.fromarray(img8)
       im = im.convert("L")
       count = count+1
       im.save(sub+time[3]+str(count)+'.tif')
       print 'Saved.....'+sub+time[3]+str(count)
      sleep(5)

