import re
fl = open("fieldu10m.txt")
hl = open("fieldu10m_out.txt","w")
lines = [line.strip() for line in fl.readlines()]
for line in lines:
 line = line.split(',')
 if re.match("^\d+?\.\d+?$", line[0]):
  print line
  if float(line[0])>60 and float(line[0])<100 and float(line[1]) >0 and float(line[1])< 40 and float(line[2]) > 0:
   print line
   hl.write(line[0]+','+line[1]+','+line[2]+'\n')

