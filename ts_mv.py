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
    if rfdif>0.0:
     print(rfdif)
    if float(rfdif) <= 0.0:
     cat = 0
    elif float(rfdif) > 0.0 and float(rfdif) <= 60.0:
     cat = 1
    elif float(rain) > 60.0:
     cat = 2
    return cat
files = glob.glob('*_*.csv')
for item in files:
 itm = item.split('_')
 if isfloat(itm[0]):
  print(item,'opened..................')
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
   if line[-1] == 'ir1':
    ir1.append(line[:-1])
   elif line[-1] == 'ir2':
    ir2.append(line[:-1])
   elif line[-1] == 'mir':
    mir.append(line[:-1])
   elif line[-1] == 'wv':
    wv.append(line[:-1])
  for k,l,m,n in zip(ir1,ir2,mir,wv):
   now = n[-1]
   if float(now)-float(then) != 0: 
    dif = float(now) - float(then)
    then = now
   else:
    dif = 0
   print(k[0]+','+k[1]+','+l[1]+','+m[1]+','+n[1]+','+str(dif))
   gl.write(k[0]+','+k[1]+','+l[1]+','+m[1]+','+n[1]+','+str(dif)+'\n')
  gl.close()
  print(item,'closed..................')

  

