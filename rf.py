flat = open('/home/dulal/insat/lat.txt','r')
flon = open('/home/dulal/insat/lon.txt','r')
frf = open('/home/dulal/insat/rf.txt','r')
wfl = open('/home/dulal/insat/daily_rainfall.txt','w')
rfd={}
count = 0
lat=flat.readline()
while lat:
 lat = lat.strip('\n')
 word = lat.split(' ')
 print word
 for idx in range(len(word)):
  rfd[count] = [word[idx]]
  count = count + 1
 lat=flat.readline()

"""
count = 0
lon = flon.readline() 
while lon:
 lst = lon.split(' ')
 for idx in range(len(lst)):
  rfd[count].append(lst[idx])
  count = count + 1
count = 0
rf = frf.readline() 
while rf:
 lst = rf.split(' ')
 for idx in range(len(lst)):
  rfd[count].append(lst[idx])
  count = count + 1
for val in rfd.values():
 wfl.writelines(val[0]+','+val[1]+','+val[2])
flat.close()
flon.close()
frf.close()
wfl.close() 
"""
