date = input('Input date(2018-03-29)?')
df={}
fl = open('mumrh'+date,'w')
lines = [line.rstrip('\n') for line in open(date+'.csv')]
for line in lines:
 line = line.split(',')
 time = line[0]
 time = time.split(':')
 if time[1] == '00':
  df[line[0]] = line[1:]
keylist = df.keys()
sorted(keylist)
for key in keylist:
 keyname = key.split('_')
 print(keyname[1]+keyname[2]+keyname[-1],df[key][-1])
 if keyname[1] == 'MAHALAXMI':
  pass
 else:
  fl.write(keyname[1]+keyname[2]+keyname[-1]+','+df[key][-1]+'\n')
 #print(keyname,df[key][-1])
