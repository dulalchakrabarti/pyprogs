wx = {}
with open("ww.csv") as fl:
 lines = [x.strip() for x in fl.readlines()]
 for line in lines:
  line = line.split(',')
  wx[int(line[0])]= line[1]
import string
stn = {}
fl = open('india_station.csv')
gl = open('aaxx.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[int(line[0])]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
 lst = inp.split()
 #print lst
 if len(lst)>0 and len(lst[0])==5:
  idx = int(lst[0])
  for word in lst:
    if word[:1] == '7':
     if len(word) > 2: stn[idx].append(word[:5])
for key,val in stn.items():
   if len(val) >= 4:
    print key,val[0],wx[int(val[3][1:3])]



