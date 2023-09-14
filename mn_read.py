import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random
import matplotlib.pyplot as plt
df = pd.read_csv('mnist_train.csv')
img = []
lbl = []
for k,row in df.iterrows():
 pic = row.tolist()
 img1 = pic[1:]
 img1 =np.array(img1)
 img1 = img1.reshape(28,28)
 lbl1 = pic[0]
 img.append(img1)
 lbl.append(lbl1)
 print(k,lbl1,img1)
 if k > 49:
  break
print('end...')
