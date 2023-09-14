import urllib2
from time import sleep
stn = {}
fa = open("india_station.csv")
tmp = [line.strip() for line in fa.readlines()]
for item in tmp:
 lst = item.split(',')
 stn[int(lst[0])] = lst[1:]
def get_data(beg,end):
    '''
    '''
    fl = open("aaxx.txt",'w+')
    f1 = urllib2.urlopen("https://www.ogimet.com/cgi-bin/getsynop?begin="+beg+"&end="+end+"&block=42")
    txt1 = f1.read()
    syn = txt1.split('\n')
    for item in syn:
     buf = item.split(',')
     if len(buf)>5:
      b = buf[-1].split(' ')
      z = b[2:]
      if len(z) > 2 and stn.has_key(int(z[0])):
       z = ' '.join(x for x in z)
       fl.write(z+'\n')
    f1.close()
    f2 = urllib2.urlopen("https://www.ogimet.com/cgi-bin/getsynop?begin="+beg+"&end="+end+"&block=43")
    txt1 = f2.read()
    syn = txt1.split('\n')
    for item in syn:
     buf = item.split(',')
     if len(buf)>5:
      b = buf[-1].split(' ')
      z = b[2:]
      if len(z) > 2 and stn.has_key(int(z[0])):
       z = ' '.join(x for x in z)
       fl.write(z+'\n')
    f2.close()
    fl.close()

def update(beg):
    '''
    '''
    day = beg
    fl = open('tsdata1.csv','a+')
    stn1 = {}
    lines = [line.rstrip('\n') for line in open('india_station.csv')]
    latlon = [line.split(',') for line in lines]
    for rec in latlon:
     stn1[rec[0]] = rec[1:]
    lines = [line.rstrip('\n') for line in open('aaxx.txt')]
    for inp in lines:
     lst = inp.split()
     ts=''
     ts = [gr for gr in lst if gr[0:2] == '79']
     if len(ts)>0:
      stn1[lst[0]].append(day)
      stn1[lst[0]].extend(ts)
      for item in stn1[lst[0]]:
       fl.write(item+',')
      fl.write('\n')
      print 'processed',beg
    fl.close()

yr = raw_input('Enter Year(2017):')
for mon in range(3,6):
 if mon == 3 or mon == 5:
  days = 31
 else:
  days = 30
 for day in range(1,days+1):
  if len(str(day)) == 1:
   beg = yr+'0'+str(mon)+'0'+str(day)+'1200'
   end = beg[:-2]+'59'
   get_data(beg,end)
   update(beg)
   sleep(5)
  else:
   beg = yr+'0'+str(mon)+str(day)+'1200'
   end = beg[:-2]+'59'
   get_data(beg,end)
   update(beg)
   sleep(5)

