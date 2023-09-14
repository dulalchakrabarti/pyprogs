import requests
from bs4 import BeautifulSoup
import tabula
#read lat long file & store in adictionary
stn = {}
fl = open('dist_lat_lon.csv')
gl = open('rfseason.csv','w')
line = fl.readline()
while line:
 lst = line.split(',')
 stn[lst[0]] = lst[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
gl.write('district'+','+'lat' +','+'lon'+','+'srf'+ '\n')
tabula.convert_into("rf.pdf", "rf.csv", output_format="csv",pages='all')
hl = open('rf.csv')
line = hl.readline()
srf = ''
while line:
 line = line.split(',')
 if line[0].isdigit():
  line = [x for x in line if x != '']
  srf = line[-1].split()
  srf = srf[-2][:-1]
  gl.write(line[1]+','+stn[line[1]][0] +','+stn[line[1]][1]+','+srf+ '\n')
  print(line[1],stn[line[1]][0],stn[line[1]][1],srf)
 line = hl.readline()
 line = line.strip('\n')
hl.close()




