fl = open('subdivrf.csv')
gl = open('rain23.csv','w')
seq = {99:'SUB',9999:'YEAR',0:'JAN',1:'FEB',2:'MAR',3:'APR'APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC,JF,MAM,JJAS,OND,ANN'
#gl.write(txt+'\n')
lines = [line.rstrip('\n') for line in fl]
for line in lines:
 line = line.split(',')
 sub = line[0]
 yr = line[1]
 print(sub,yr)
 count = 0
 for fld in line[2:]:
  print(count,fld)
  count+=1
'''
 if len(line)==10 or len(line)==11 or len(line)==12:
  sub = line[1]
 elif (len(line)) == 1:
  pass
 elif (len(line)) == 18:
  line.append(sub)
  line = line[-1:] + line[:-1]
  if line[1] == 'MEAN' or line[1] == 'P-Ann' or line[1] == 'SD' or line[1] == 'CV' or line[1] == 'YEAR':
   pass
  else:
   txt = ','.join(x for x in line)
   print(txt)
   gl.write(txt+'\n')
'''
