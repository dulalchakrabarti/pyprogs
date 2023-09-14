import glob
import matplotlib.pyplot as plt
def tm(buf):
    '''
    '2022-03-22T21:30:00.000Z'
    '''
    tim = buf.split('T')
    return tim
files = glob.glob('*-*.csv')
lstf = []
ser1={}
ser2={}
lstd = []
lstr = []
tmd = []
tmr = []
for item in files:
 lstf.append(item)
lstf.sort()
for item1 in lstf:
  lines = [line.rstrip('\n') for line in open(item1)]
  for num in range(len(lines)):
   line = lines[num].split(',')
   line = [x.strip('[') for x in line]
   line = [x.strip(']') for x in line]
   line = [x.strip(' ') for x in line]
   l = int(len(line[1:]))//1
   tm1 = line[1:(l//2)+1]
   #tm1 = [float(x) for x in tm1 if str.isdigit(x)]
   tm2 = line[(l//2)+1:]
   #print(tm1)
   tm2 = [x.strip('[') for x in tm2]
   if 'None' in tm2:
    pass
   else:
    if len(tm1) and len(tm2) <= 48:
     if line[0][-1] == 'D':
      tmd.extend(tm1)
      lstd.extend(tm2)
     elif line[0][-1] == 'R':
      #ftm2 = [float(x) for x in tm2]
      #vmax = max(ftm2)
      #ftm_ = [x/vmax for x in ftm2]
      tmr.extend(tm1)
      lstr.extend(tm2)
      
vald_ = [float(x) for x in lstd]
valmaxd = max(vald_)
vald = [x/valmaxd for x in vald_]
valr_ = [float(x) for x in lstr]
valmaxr = max(valr_)
valr = [x/valmaxr for x in valr_]
print(len(tmd))
print(len(vald))
print(len(tmr))
print(len(valr))
'''
def countList(lst1, lst2):
    return [item for pair in zip(lst1, lst2 + [0])
                                 for item in pair]
drtm = countList(tmd,tmr)  
print(len(drtm))
drval = countList(vald,valr)
print(len(drval))
'''                              
