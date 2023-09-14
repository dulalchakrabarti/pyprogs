#sn,dist,stn,dt,tm,rncum3,tmp,tmpmx/mn,rh,rhmax/min,bat,gps
import requests
from bs4 import BeautifulSoup
#import tabula
#read lat long file & store in a dictionary
mumloc = {}
lines = [line.rstrip('\n') for line in open('mum_lat_lon_new.csv')]
for inp in lines:
 inp = inp.split(',')
 stn_name = inp[1]
 mumloc[stn_name] = inp[2:]
df = {}
date = input('Input date(2018-03-29)?')
gl = open(date+'.csv','w')
#gl.write('stn'+','+'lat'+','+'lon'+','+'rain'+','+'temp'+','+'tmin'+','+'tmax'+','+'RH'+'\n')
url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWS&b=MAHARASHTRA&c=MUMBAI_CITY&d=ALL_STATION&e="+date+"&f="+date+"&g="+"ALL_HOUR"+"&h=ALL_MINUTE"
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 #print(cols)
 lst = []
 for td in cols:
  lst.append(td.get_text().encode("utf-8"))
 if len(lst)>0:
  lst = [x.decode() for x in lst]
  #print(lst)
  stn_name=lst[2]
  name = 'AWS_'+lst[2]+'_'+lst[3]+'_'+lst[4]
  df[name] = [mumloc[stn_name],lst[5],lst[6],lst[7],lst[8],lst[9]]
url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=ARG&b=MAHARASHTRA&c=MUMBAI_CITY&d=ALL_STATION&e="+date+"&f="+date+"&g="+"ALL_HOUR"+"&h=ALL_MINUTE"
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text().encode("utf-8"))
 if len(lst)>0:
  lst = [x.decode() for x in lst]
  #print(lst)
  stn_name=lst[2]
  name = 'ARG_'+lst[2]+'_'+lst[3]+'_'+lst[4]
  df[name] = [mumloc[stn_name],lst[5],lst[6],lst[7],lst[8],lst[9]]
keylist = df.keys()
sorted(keylist)
for key in keylist:
 lst = df[key]
 #print(lst)
 if lst[5] == '1':
  lst[3] = '-'
  lst[4] = '-'
  lst[5] = '1'
 elif lst[3] == '' and lst[4] == '' and lst[5] == '':
  lst[3] = '-'
  lst[4] = '-'
  lst[5] = '-'
 elif lst[3] == '' and lst[4] == '':
  lst[3] = '-'
  lst[4] = '-'
 elif lst[3] == '' and lst[4] != '':
  lst[3] = '-'
 elif lst[4] == '' and lst[3] != '':
  lst[4] = '-'
 print(key,lst[0][0],lst[0][1],lst[1],lst[2],lst[3],lst[4],lst[5])
 gl.write(key+','+str(lst[0][0])+','+str(lst[0][1])+','+lst[1]+','+lst[2]+','+lst[3]+','+lst[4]+','+lst[5]+'\n')
gl.close()

