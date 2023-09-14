fl = open('iitm-subdivrf.txt')
gl = open('subdivrf.csv','w')
txt = 'SUB,YEAR,JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC,JF,MAM,JJAS,OND,ANN'
gl.write(txt+'\n')
lines = [line.rstrip('\n') for line in fl]
for line in lines:
 line = line.split()
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

