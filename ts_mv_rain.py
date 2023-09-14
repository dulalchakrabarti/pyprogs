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

def rain_class(rain):
    if float(rain) > 0.0 and float(rain) <= 10.0:
     cat = 0
    elif float(rain) > 10.0 and float(rain) <= 60.0:
     cat = 1
    elif float(rain) > 60.0:
     cat = 2
    return cat
gl = open('total.csv','w')
files = glob.glob('*_*.csv')
for item in files:
 itm = item.split('_')
 if isfloat(itm[0]):
  #print(item,'opened..................')
  ir1 = []
  ir2 = []
  mir = []
  wv = []
  lines = [line.rstrip('\n') for line in open(item)]
  for line in lines:
   line = line.split(',')
   if line[-1] == 'ir1':
    ir1.append(line[:-1])
   elif line[-1] == 'ir2':
    ir2.append(line[:-1])
   elif line[-1] == 'mir':
    mir.append(line[:-1])
   elif line[-1] == 'wv':
    wv.append(line[:-1])
  for k,l,m,n in zip(ir1,ir2,mir,wv):
   rain = n[-1]
   rfcl = rain_class(rain)
   #print(k[0]+','+k[1]+','+l[1]+','+m[1]+','+n[1]+','+str(rfcl))
   gl.write(k[0]+','+k[1]+','+l[1]+','+m[1]+','+n[1]+','+str(rfcl)+'\n')
  #print(item,'closed..................')
