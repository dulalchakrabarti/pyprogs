import requests
from bs4 import BeautifulSoup
import tabula
#read lat long file & store in adictionary
stn = {}
fl = open('arg_aws_agro_meta.csv')
gl = open('rain_hr.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[3]] = [line[4],line[5]]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
date = input('Input date(2018-03-29)?')
time = input('Input time in UTC(1)?')
st_lst = ['ANDAMAN_AND_NICOBAR','ANDHRA_PRADESH','ARUNACHAL_PRADESH','ASSAM','BANGLADESH','BHUTAN','BIHAR','CHANDIGARH','CHHATISGARH','DAMAN_AND_DIU','DELHI',
'GOA','GUJARAT','HARYANA','HIMACHAL_PRADESH','JAMMU_AND_KASHMIR','JHARKHAND','KARNATAKA','KERALA','LAKSHADWEEP','MADHYA_PRADESH',
'MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','NEPAL','ORISSA','PUDUCHERRY','PUNJAB','RAJASTHAN','SIKKIM',
'TAMIL_NADU','TELANGANA','TRIPURA','UTTARAKHAND','UTTAR_PRADESH','WEST_BENGAL']
gl.write('stn'+','+'lat'+','+'lon'+','+'rain'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=aws&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=00"
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
   print('aws ',lst)
   stn[name].append(lst[5])
for key in stn.keys():
 if len(stn[key]) > 2:
  rain = max(stn[key][2:])
  txt = ','.join(stn[key][:2])
  gl.write(key+','+txt +','+ rain + '\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=arg&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=00"
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
   print('arg ',lst)
   stn[name].append(lst[5])
for key in stn.keys():
 if len(stn[key]) > 2:
  rain = max(stn[key][2:])
  txt = ','.join(stn[key][:2])
  gl.write(key+','+txt +','+ rain + '\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=agro&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=00"
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
   print('agro ',lst)
   stn[name].append(lst[5])
for key in stn.keys():
 if len(stn[key]) > 2:
  rain = max(stn[key][2:])
  txt = ','.join(stn[key][:2])
  gl.write(key+','+txt +','+ rain + '\n')
gl.close()



