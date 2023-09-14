import string
stn = {}
fl = open('india_station.csv')
gl = open('cloudgr.csv','w')
line = fl.readline().strip()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
 lst = inp.split()
 if len(lst)>0 and len(lst[0])==5:
  idx = lst[0]
  if stn.has_key(idx):
   flag1 = True
   flag2 = True
   for word in lst[3:]:
    if word[:1] == '7': stn[idx].append(word[:5])
    if flag1:
     if word[:1] == '8':
      if len(word) > 2: stn[idx].append(word[:5])
      flag1 = False
    elif flag2:
     if word[:1] == '8' or word[:1] == '6':
      if len(word) > 2: stn[idx].append(word[:5])
cld = {}
lines1 = [line.rstrip('\n') for line in open('cl.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 cld[inp1[0]] = inp1[1]
cmd = {}
lines1 = [line.rstrip('\n') for line in open('cm.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 cmd[inp1[0]] = inp1[1]
chd = {}
lines1 = [line.rstrip('\n') for line in open('ch.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 chd[inp1[0]] = inp1[1]
cd = {}
lines1 = [line.rstrip('\n') for line in open('c.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 cd[inp1[0]] = inp1[1]
hhd = {}
lines1 = [line.rstrip('\n') for line in open('hh.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 hhd[inp1[0]] = inp1[1]
wwd={}
lines1 = [line.rstrip('\n') for line in open('ww.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 wwd[inp1[0]] = inp1[1]
w1w2d={}
lines1 = [line.rstrip('\n') for line in open('w1w2.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 w1w2d[inp1[0]] = inp1[1]
dec = {}
for key,val in stn.items():
 if len(val) > 3:
  rf = 0.0
  city = val[0]
  dec[city] = []
  lat = val[1]
  dec[city].append(lat)
  lon = val[2]
  dec[city].append(lon)
  for idx in range(3,len(val)):
   if idx == 3:
    if val[idx][0] == '7' and '/' not in val[idx]:
     ww = wwd[val[idx][1:3]]
     w1 = w1w2d[val[idx][3]]
     w2 = w1w2d[val[idx][4]]
     text2 = ww+','+w1+','+w2
     dec[city].append('7www1w2')
     dec[city].append(text2)
     #print idx,val[0],text2
    elif val[idx][0] == '8':
     nh = val[idx][1]
     cl = cld[val[idx][2]]
     cm = cmd[val[idx][3]]
     ch = chd[val[idx][4]]
     text3 = nh+','+cl+','+cm+','+ch
     dec[city].append('8nccc')
     dec[city].append(text3)
     #print idx,val[0],text3
   elif idx == 4:
    if val[idx][0] == '6':
     rain = val[idx][1:4]
     rf = float(rain)
     if rf >= 990:
      rf = (rf-990)/10.0
     #dec[city].append(str(rf))
     #print idx,val[0],str(rf)
    elif val[idx][0] == '8':
     if '/' not in val[idx][3:5]:
      ht1 = val[idx][3:5]
      cov1 = val[idx][1]
      gen1 = cd[val[idx][2]]
      met1 = hhd[ht1]
      text4 = cov1+','+gen1+','+met1
      dec[city].append('8nchh')
      dec[city].append(text4)
      #print idx,val[0],text4
   elif idx == 5:
    if val[idx][0] == '6':
     rain = val[idx][1:4]
     rf = float(rain)
     if rf >= 990:
      rf = (rf-990)/10.0
     #dec[city].append(str(rf))
     #print val[0],str(rf)
    elif val[idx][0] == '8':
     if '/' in val[idx][3:5]:
      #ht2 = val[idx][3]+'0'
      pass
     else:
      ht2 = val[idx][3:5]
      met2 = hhd[ht2]
     cov2 = val[idx][1]
     gen2 = cd[val[idx][2]]
     text5 = cov2+','+gen2+','+met2
     dec[city].append('8nchh')
     dec[city].append(text5)
     #print idx,val[0],text5
   elif idx > 5:
    if val[idx][0] == '8'and len(val[idx])==5:
     if '/' in val[idx][3:5]:
      #ht = val[idx][3]+'0'
      pass
     else:
      ht = val[idx][3:5]
     text6 = val[idx][1]+','+cd[val[idx][2]]+','+hhd[ht]
     dec[city].append('8nchh')
     dec[city].append(text6)
     #print idx,val[0],text6
  dec[city].append('6rrr/')
  dec[city].append(str(rf))
keylist = dec.keys()
keylist.sort()
for key in keylist:
 for i in range(len(dec[key])):
  dec[key][i] = dec[key][i].replace(',',' ')
 line = ','.join(x for x in dec[key])
 gl.write(key+','+line+'\n')

