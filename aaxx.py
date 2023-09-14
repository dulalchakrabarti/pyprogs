import string
stn = {}
fl = open('india_station.csv')
gl = open('surface_wind.csv','w')
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
   print lst
   flag = True
   for word in lst:
     if flag:
       wnd = lst[2]
       if wnd[1:2].isdigit(): stn[word].append(str(int(wnd[1:3])*10))
       stn[word].append(wnd[3:5])
       flag = False
for val in  stn.values():
 if len(val) > 4:
  gl.writelines( val[0]+','+val[1]+','+val[2]+','+val[3]+','+val[4]+'\n' ) 

