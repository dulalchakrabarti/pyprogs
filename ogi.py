import urllib.request
stn = {}
beg = ''
end = ''
beg = input('Enter start datetime(201807090300):')
end = input('Enter end datetime(201807090359):')
fa = open("india_station.csv")
tmp = [line.strip() for line in fa.readlines()]
for item in tmp:
 lst = item.split(',')
 stn[int(lst[0])] = lst[1:]
fl = open("aaxx.txt",'w+') 
f1 = urllib.request.urlopen("https://www.ogimet.com/cgi-bin/getsynop?begin="+beg+"&end="+end+"&block=42")
txt1 = f1.read()
syn = txt1.split(b'\n')
for item in syn:
 buf = item.split(b',')
 if len(buf)>5:
  b = buf[-1].split(b' ')
  z = b[2:]
  if len(z) > 2 and int(z[0]) in stn:
   z = b' '.join(x for x in z)
   z = z.decode('utf-8')
   fl.write(z+'\n')
f2 = urllib.request.urlopen("https://www.ogimet.com/cgi-bin/getsynop?begin="+beg+"&end="+end+"&block=43")
txt1 = f2.read()
syn = txt1.split(b'\n')
for item in syn:
 buf = item.split(b',')
 if len(buf)>5:
  b = buf[-1].split(b' ')
  z = b[2:]
  if len(z) > 2 and int(z[0]) in stn:
   z = b' '.join(x for x in z)
   z = z.decode('utf-8')
   fl.write(z+'\n')
fl.close()
