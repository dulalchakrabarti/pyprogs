import string
import re
stn = {}
fl = open('india_station.csv')
gl = open('temp9.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
   lst = inp.split()
   if len(lst) > 2:
    try:
      word = lst[0]
      for grp in lst[1:]:
       if grp[:2] == '10':
        stn[word].append(grp[2:4]+'.'+grp[4])
        print word,grp[2:4]+'.'+grp[4]
    except ValueError:
     continue
for val in  stn.values():
 if len(val) > 3:
  gl.writelines( val[0]+','+val[1]+','+val[2]+','+val[3]+'\n' ) 

