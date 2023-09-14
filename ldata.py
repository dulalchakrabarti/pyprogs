import requests
from bs4 import BeautifulSoup
import tabula
#read lat long file & store in adictionary
stn = {}
gl = open('lrain.csv','w')
lines = [line.rstrip('\n') for line in open('awslatlong.csv')]
for inp in lines:
 lst = inp.split(',')
 #print(lst)
 stn[lst[3]] = [lst[4],lst[5]]
date = input('Input date(2018-03-29)?')
time = input('Input time in UTC(1)?')
st_lst = ['ANDAMAN_AND_NICOBAR','ANDHRA_PRADESH','ARUNACHAL_PRADESH','ASSAM','BANGLADESH','BHUTAN','BIHAR','CHANDIGARH','CHHATISGARH','DAMAN_AND_DIU','DELHI',
'GOA','GUJARAT','HARYANA','HIMACHAL_PRADESH','JAMMU_AND_KASHMIR','JHARKHAND','KARNATAKA','KERALA','LAKSHADWEEP','MADHYA_PRADESH',
'MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','NEPAL','ORISSA','PUDUCHERRY','PUNJAB','RAJASTHAN','SIKKIM',
'TAMIL_NADU','TELANGANA','TRIPURA','UTTARAKHAND','UTTAR_PRADESH','WEST_BENGAL']
gl.write('stn'+','+'lat'+','+'lon'+','+'rain'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=aws&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
 #print(url)
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
   name = lst[2]
   #print(lst[:5])
   txt = ','.join(lst)
   #print(stn[name][0]+','+stn[name][1]+','+txt)
   gl.write(stn[name][0]+','+stn[name][1]+','+txt+ ','+'aws'+'\n')
gl.write('lat'+','+'lon'+','+'sn'+','+'dist'+','+'stn'+','+'date'+','+'time'+','+'rain'+','+'bat'+'gps''\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=arg&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
   name = lst[2]
   txt = ','.join(lst)
   #print(stn[name][0]+','+stn[name][1]+','+txt)
   gl.write(stn[name][0]+','+stn[name][1]+','+txt+ ','+'arg'+ '\n')
gl.write('lat'+','+'lon'+','+'sn'+','+'dist'+','+'stn'+','+'date'+','+'time'+','+'rain'+','+'temp'+','+'min'+','+'max'+','+'rh'+','+'rhminmax'+','+'dir10'+','+'speed10'+','+'gust10'+','+'dir3'+','+'speed3'+','+'gust3'+','+'slp'+','+'mslp'+','+'sunshine'+','+'soiltemp10'+','+'soilmios10'+','+'soiltemp30'+','+'soilmois30'+'soiltemp70'+','+'soilmois70'+'soiltemp100'+','+'soilmois100'+'globalrad'+','+'PAR'+','+'bat'+','+'gps'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=agro&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
   name = lst[2]
   txt = ','.join(lst)
   #print(stn[name][0]+','+stn[name][1]+','+txt)
   gl.write(stn[name][0]+','+stn[name][1]+','+txt+ ','+'agro'+'\n')
gl.write('lat'+','+'lon'+','+'sn'+','+'dist'+','+'stn'+','+'date'+','+'time'+','+'rain'+','+'temp'+','+'min'+','+'max'+','+'rh'+','+'rhminmax'+','+'dir10'+','+'speed10'+','+'gust10'+','+'dir3'+','+'speed3'+','+'gust3'+','+'slp'+','+'mslp'+','+'sunshine'+','+'soiltemp10'+','+'soilmios10'+','+'soiltemp30'+','+'soilmois30'+'soiltemp70'+','+'soilmois70'+'soiltemp100'+','+'soilmois100'+'globalrad'+','+'PAR'+','+'bat'+','+'gps'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWSAGRO&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
   name = lst[2]
   txt = ','.join(lst)
   print(stn[name][0]+','+stn[name][1]+','+txt)
   gl.write(stn[name][0]+','+stn[name][1]+','+txt+ ','+'awsagro'+ '\n')
gl.close()



