import h5py
import numpy as np
a_file = h5py.File('model_checkpoint.h5', 'r')

x = a_file.keys()
for k in x:
 dataset = a_file[k]

 print(dataset)


