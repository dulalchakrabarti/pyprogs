stn = {}
lines = [line.rstrip('\n') for line in open('tsdata.csv')]
latlon = [line.split(',') for line in lines]
date = ''
for item in latlon:
 if stn.has_key(item[3]):
  stn[item[3]].append(item[0])
  stn[item[3]].append(item[1])
  stn[item[3]].append(item[2])
 else:
  stn[item[3]] = item[0:3]
keys = stn.keys()
keys.sort()
for key in keys:
 print key,stn[key] 

