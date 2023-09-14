import string
stn = {}
fl = open('/home/dulal/synop/india_station.csv')
gl = open('/home/dulal/synop/ttaa.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
fl1 = open('/home/dulal/synop/ttaa.txt').readlines()
ttaa = False
flag1 = False
tttdd = False
for line in fl1:
 if 'TTAA' in line:
  ttaa = True
 if ttaa:
  words = line.split()
  for item in words:
   if flag1 and tttdd:
      stn[stnidx].append(item[0:3])
      stn[stnidx].append(item[3:])
      flag1 = False
      tttdd = False
   if flag1:
     tttdd = True
   if 'TTAA' in item:
    stnidx = words[2]
   if '85' in item:
     if item[0:2] == '85':
      flag1 = True
   if '=' in item:
    ttaa = False
for val in  stn.values():
 if len(val) > 4:
  gl.writelines( val[0]+','+val[1]+','+val[2]+','+val[3]+','+val[4]+'\n' ) 

