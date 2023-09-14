import tabula
tabula.convert_into("rf.pdf", "rf.csv", output_format="csv",pages='all')
latlon={}
lines = [line.rstrip('\n') for line in open('dist_lat_lon.csv')]
for line in lines:
 line = line.split(',')
 latlon[line[0]] = [line[1],line[2]]
print(len(latlon))
lines = [line.rstrip('\n') for line in open('rf.csv')]
count=0
gl = open('rflatlong.csv','w')
for line in lines:
 line = line.split(',')
 if line[0].isdigit():
  if line[1] in latlon.keys():
   latlon[line[1]].append(line[2])
   val = ','.join(str(x) for x in latlon[line[1]])
   gl.write(line[1]+','+val+'\n') 
  else:
   print(line[1])
  count+=1
print(count)
