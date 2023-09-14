import requests
from bs4 import BeautifulSoup
date = input('Input date(2018-03-29)?')
dat = date.split('-')
dt = dat[2]+dat[1]+dat[0]
fl = open('india-airport.csv')
lines = [line.rstrip('\n') for line in fl]
ap = {}
for line in lines:
 fld = line.split(':')
 #print(fld[0],fld[1],fld[4],fld[5])
 ap[fld[0]] = fld[2:]
keylist = ap.keys()
sorted(keylist)
txt = 'https://www.aviationweather.gov/metar/data?ids=VOVZ%20VOTR%20VOHS%20VOML%20VOCL%20VOBL%20VOCB%20VOCI%20VEGT%20VEPT%20VAAH%20VANP%20VEBS%20VILK%20VOTV%20VIJP%20VIDP%20VECC%20VABB%20VOMM&format=decoded&hours=96&taf=off&layout=on'
r1 = requests.get(txt)
resp = r1.text
soup = BeautifulSoup(resp,"lxml")
rows = soup.findAll('tr')
#print(rows)
lst = []
flag = False
stn = ''
tm = ''
loc = {}
for tr in rows:
 cols = tr.findAll('td')
 for td in cols:
  lst.append(td.get_text())
for num in range(len(lst)):
 if lst[num] == 'Text:':
  metar = lst[num+1].split()
  if dat[2] == metar[1][:2]:
   stn = metar[0]
   tm = metar[1]
   flag = True
 elif flag and lst[num] == 'Visibility:':
  vis = lst[num+1].split()
  flag = False
  if stn in ap.keys():
   lat = ap[stn][2]
   lon = ap[stn][3]
   loc[stn] = lat+','+lon
   print(tm,vis[3])
print(loc) 
'''
 time = fld[1].split()
 if fld[0]+','+time[0]+','+fld[3]+','+fld[2] in ap.keys():
  ap[fld[0]+','+time[0]+','+fld[3]+','+fld[2]].append(time[1]+','+fld[4])
 else:
  ap[fld[0]+','+time[0]+','+fld[3]+','+fld[2]] =[time[1]+','+fld[4]]
for key in keylist:
 k = key.split(',')
 k1 = k[1].split('-')
 name = k[0]+'-'+k1[2]+k1[1]+k1[0]+'-'+k[2]+'-'+k[3]
 if len(ap[key]) == 48:
  gl = open(name+'.csv','w')
  txt = ap[key]
  lst = [x.split(',') for x in txt]
  #print(lst)
  [gl.write(x[0]+','+x[1]+'\n') for x in lst]
  gl.close()
ir1 = open(dt+'fog_ir1.csv')
ir2 = open(dt+'fog_ir2.csv')
mir = open(dt+'fog_mir.csv')
wv = open(dt+'fog_wv.csv')
lir1 = [line.rstrip('\n') for line in ir1]
lir2 = [line.rstrip('\n') for line in ir2]
lmir = [line.rstrip('\n') for line in mir]
lwv = [line.rstrip('\n') for line in wv]
for num in range(len(lir1)):
 print(lir1[num],lir2[num],lmir[num],lwv[num])
'''

