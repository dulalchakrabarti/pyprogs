lines1 = [line1.rstrip('\n') for line1 in open('awslatlong.csv')]
itm1 = []
for inp1 in lines1:
 inp1 = inp1.split(',')
 itm1.append(inp1)
print(len(itm1))
lines2 = [line2.rstrip('\n') for line2 in open('arg_aws_agro_meta.csv')]
itm2 = []
for inp2 in lines2:
 inp2 = inp2.split(',')
 inp2 = inp2[3:]
 itm2.append(inp2)
print(len(itm2))
d1 = {}
for inp3 in itm1:
 if '_UKG' in inp3[0]:
  d1[inp3[0]] = inp3[1:]
print(len(d1))
d2 = {}
for inp4 in itm2:
 if '_UKG' in inp4[0]:
  d2[inp4[0]] = inp4[1:]
print(len(d2))
keylist1 = d1.keys()
keylist2 = d2.keys()
sorted(keylist1)
sorted(keylist2)
fl = open('diff.csv','w')
for key1 in keylist1:
 if key1 in keylist2:
  pass
 else:
  buf = ','.join(str(x) for x in d1[key1])
  fl.write(','+','+','+key1+','+buf+'\n')
fl.close()
