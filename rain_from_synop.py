import string
def rrr(x):
    '''
    '''
    if int(x) >= 0 and int(x) < 990:
     return str(int(x)/10.0)
    else:
     return str((int(x)-989)/10.0)
stn = {}
fl = open('india_station.csv')
gl = open('rain_synop.csv','w')
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
   for word in lst:
    if word[0] == '6':
     stn[lst[0]].append(word[1:4])
for item in stn.values():
 if len(item)>3:
  print item[3]
  gl.writelines( item[0]+','+item[1]+','+item[2]+','+rrr(item[3])+'\n' )

