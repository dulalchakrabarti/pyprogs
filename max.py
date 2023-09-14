import string
stn = {}
fl = open('india_station.csv')
gl = open('max.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('max.txt')]
for inp in lines:
   lst = inp.split()
   #print lst
   flag = True
   for word in lst:
     if flag:
       maxt = lst[3]
       if maxt[0].isdigit():
        stn[word].append(str(int(maxt[2:5])/10.0))
        print stn[word]
       flag = False
for val in  stn.values():
 if len(val) > 3:
  gl.writelines( val[0]+','+val[1]+','+val[2]+','+val[3]+'\n' ) 

