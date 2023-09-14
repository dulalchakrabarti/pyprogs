import numpy as np
import pandas as pd
df = pd.read_csv('trainir1.csv')
img = []
lbl = []
for k,row in df.iterrows():
 pic = row.tolist()
 img1 = pic[3:]
 img1 =np.array(img1)
 img1 = img1.reshape(28,28)
 lbl1 = pic[2]
 img.append(img1)
 lbl.append(lbl1)
 if k > 48:
  break
train_images = np.array(img)
train_labels = np.array(lbl)
print(train_images.shape,train_labels.shape)

