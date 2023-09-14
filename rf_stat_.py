import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
fl = open('rf.csv')
lines = [line.rstrip('\n') for line in fl]
countd = 0
countn = 0
counte = 0
d1 = {}
for line in lines:
 line = line.split(',')
 if line[0] != '""':
  #print(line[-1][-2:])
  if 'D' in line[-1][-2:] or 'LD' in line[-1][-2:]:
   countd+=1
   d1[line[1]] = line[2:]
  elif 'N' in line[-1][-2:]:
   countn+=1
   d1[line[1]] = line[2:]
  elif 'E' in line[-1][-2:] or 'LE' in line[-1][-2:]:
   counte+=1
   d1[line[1]] = line[2:]
 else:
   print(line)
tot = float(countd+countn+counte)
print((countd*100)/tot,(countn*100)/tot,(counte*100)/tot,countd,countn,counte,tot)

