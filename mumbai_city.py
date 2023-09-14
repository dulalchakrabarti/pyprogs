#sn,dist,stn,dt,tm,rncum3,tmp,tmpmx/mn,rh,rhmax/min,bat,gps
import requests
from bs4 import BeautifulSoup
#import tabula
#read lat long file & store in a dictionary
mumloc = {}
lines = [line.rstrip('\n') for line in open('mum_lat_lon.csv')]
for inp in lines:
 inp = inp.split(',')
 mumloc[inp[1]] = inp[2:]
mumkeylist = mumloc.keys()
sorted(mumkeylist)
df = {}
gl = open('mum.csv','w')
date = input('Input date(2018-03-29)?')
st_lst = ['MAHARASHTRA']
gl.write('stn'+','+'lat'+','+'lon'+','+'rain'+','+'temp'+','+'tempmax/min'+','+'RH'+','+'RHmax/min'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWSAGRO&b="+item+"&c=MUMBAI_CITY&d=ALL_STATION&e="+date+"&f="+date+"&g="+"ALL_HOUR"+"&h=ALL_MINUTE"
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
   stn_name=lst[2]
   name = 'AWSAGRO_'+lst[2]+'_'+lst[3]+'_'+lst[4]
   mumloc[stn_name].append([lst[5],lst[6],lst[7],lst[8],lst[9]])
   df[name] = mumloc[stn_name]
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWS&b="+item+"&c=MUMBAI_CITY&d=ALL_STATION&e="+date+"&f="+date+"&g="+"ALL_HOUR"+"&h=ALL_MINUTE"
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
   stn_name=lst[2]
   name = 'AWS_'+lst[2]+'_'+lst[3]+'_'+lst[4]
   mumloc[stn_name].append([lst[5],lst[6],lst[7],lst[8],lst[9]])
   df[name] = mumloc[stn_name]
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=ARG&b="+item+"&c=MUMBAI_CiTY&d=ALL_STATION&e="+date+"&f="+date+"&g="+"ALL_HOUR"+"&h=ALL_MINUTE"
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
   stn_name=lst[2]
   name = 'ARG_'+lst[2]+'_'+lst[3]+'_'+lst[4]
   mumloc[stn_name].append([lst[5],lst[6],lst[7],lst[8],lst[9]])
   df[name] = mumloc[stn_name]
keylist = df.keys()
sorted(keylist)
for key in keylist:
 #print(key,df[key])
 lst = df[key]
 for item in lst[2:]:
  xx = ['-' if x == '' else x for x in item]
  val = ','.join(str(x) for x in xx)  
  print(key+','+str(lst[0])+','+str(lst[1])+','+val)
  x = key.replace(" ", "_")
  gl.write(x+','+str(lst[0])+','+str(lst[1])+','+val+'\n')
gl.close()
  
