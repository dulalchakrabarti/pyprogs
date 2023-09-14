ts = {}
fl = open('subdivrf.csv')
rfts = open('fields.csv','w')
buf=''
for i in range(511):
 fld=str(i)
 txt='field'+fld+','
 buf= buf+txt
buf = buf[:-1]
rfts.write(buf+'\n')
lines = [line.rstrip('\n') for line in fl]
for line in lines:
 line = line.split(',')
 #print(len(line[2:]))
 key = line[1]
 if key in ts.keys():
  ts[key].extend(line[2:])
 elif key.isdigit():
  ts[key] = line[2:]
keylist = ts.keys()
sorted(keylist)
for key in keylist:
 #print(key,ts[key])
 #print(len(ts[key]))
 txt = key+','+','.join(x for x in ts[key])
 rfts.write(txt+'\n')
