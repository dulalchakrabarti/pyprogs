import numpy as np
ir1lines = [line.rstrip('\n') for line in open('trainir1.csv')]
img = []
lbl = []
for num in range(len(ir1lines)):
 ir1line = ir1lines[num].split(',')
 ir1cnt = ir1line[3:]
 lblcnt = ir1line[2]
 mir1cnt = max(ir1cnt)
 nir1cnt = [round(float(x)/float(mir1cnt)) for x in ir1cnt]
 arr = np.array(nir1cnt)
 arr = arr.reshape(15,15)
 img.append(arr)
 lbl.append(lblcnt)
img = np.array(img)
lbl = np.array(lbl)
print(img.shape)
print(lbl.shape)
