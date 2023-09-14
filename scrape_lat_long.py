gl = open('arg_aws_agro_lat_long.csv','w')
stn={}
lst = ['arg','aws','agro']
for item in lst:
 with open(item+'.txt') as fl:
    lines = [line.strip() for line in fl]
    for line in lines:
     line = line.split(',')
     print line
     stn[line[-1]] = [line[1],line[2]]
 fl.close()
keylist = stn.keys()
keylist.sort()
for key in keylist:
 latlong = ','.join(stn[key])
 print key+','+latlong
 gl.write(key+','+latlong+'\n')

