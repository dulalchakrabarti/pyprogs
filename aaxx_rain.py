import string
stn = {}
fl = open('/home/dulal/imgproc/india_station.csv')
gl = open('/home/dulal/imgproc/rain.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('/home/dulal/imgproc/aaxx.txt')]
for inp in lines:
   lst = inp.split()
   flag = True
   count = 0
   for word in lst:
    count += 1
    if flag:
     if count > 4 and word[0] == '6':
       rain = word[1:4]
       rf = float(rain)
       if rf >= 990:
        rf = (rf-990)/10.0
       stn[lst[0]].append(rf)
       flag = False
for val in  stn.values():
 if len(val) > 3:
  print val[0]+','+val[1]+','+val[2]+','+str(val[3])
  gl.writelines( val[0]+','+val[1]+','+val[2]+','+str(val[3])+'\n' ) 

