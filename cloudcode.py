cloud = {}
lines = [line.rstrip('\n') for line in open('nchh.csv')]
for line in lines:
 layers = ''
 line = line.split('(')
 for xx in line:
  ln = xx.split(')')
  if len(ln[0]) == 2:
   if ln[0] not in layers:
    layers = layers + ln[0]
 if cloud.has_key(layers):
  cloud[layers] = cloud[layers] + 1
 else:
  cloud[layers] = 1
keylist = cloud.keys()
keylist.sort()
for key in keylist:
 if len(key) > 0:
  print key

