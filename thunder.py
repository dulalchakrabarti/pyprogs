day = raw_input('Enter start datetime(201807090300):')
fl = open('tsdata.csv','a+')
stn = {}
lines = [line.rstrip('\n') for line in open('india_station.csv')]
latlon = [line.split(',') for line in lines]
for rec in latlon:
 stn[rec[0]] = rec[1:]
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
   lst = inp.split()
   ts=''
   ts = [gr for gr in lst if gr[0:2] == '79']
   if len(ts)>0:
    stn[lst[0]].append(day)
    stn[lst[0]].extend(ts)
    for item in stn[lst[0]]:
     fl.write(item+',')
    fl.write('\n')


