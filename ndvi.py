import string
stn = {}
fl = open('ndvi.csv')
gl = open('ndvi-out.csv','w')
line = fl.readline().strip('\n')
num=0
lon = 60.0
lat = 40.0
while line:
 num=num+1
 if (num >= 500) and (num <= 899):
  line = line.split(',')
  for idx in range(2400,2799):
   print (idx-1800)/10.0,lat,line[idx]
   gl.writelines( str((idx-1800)/10.0)+','+str(lat)+','+line[idx]+'\n' )
   lon = round((lon + .1),2)
  lat = round((lat - .1),2)
 line = fl.readline().strip('\n')
#print num
fl.close()
'''
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
   lst = inp.split()
   print lst
   flag = True
   for word in lst:
     if flag:
       wnd = lst[2]
       stn[word].append(str(int(wnd[1:3])*10))
       stn[word].append(wnd[3:5])
       flag = False
for val in  stn.values():
 if len(val) > 4:
  gl.writelines( val[0]+','+val[1]+','+val[2]+','+val[3]+','+val[4]+'\n' )
''' 

