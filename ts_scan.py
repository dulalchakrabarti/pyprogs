import os
import glob
import matplotlib.pyplot as plt
from datetime import datetime
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def rain_class(rfdif):
    if float(rfdif) <= 0.0:
     cat = 0
    elif float(rfdif) > 0.0 and float(rfdif) <= 60.0:
     cat = 1
    elif float(rfdif) > 60.0:
     cat = 2
    return cat
files = glob.glob('*_*_.csv')
dlst = []
for item in files:
 itm = item.split('_')
 if isfloat(itm[0]):
  #print(item,'opened..................')
  gl = open(item[:-4]+'_.csv','w')
  ir1 = []
  ir2 = []
  mir = []
  wv = []
  now = 0
  then = 0    
  lines = [line.rstrip('\n') for line in open(item)]
  for line in lines:
   line = line.split(',')
   dlst.append(line[-1])
  gl.close()
  #print(item,'closed..................')
print(len(dlst))
dls = [i for i in dlst if i>'0']
print(dls)
