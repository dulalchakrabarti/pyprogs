import requests
from bs4 import BeautifulSoup
import tabula
import numpy as np
#read lat long file & store in a dictionary
date = input('Input date(2018-03-29)?')
dat = date.split('-')
hr = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
tm = ['00','15','30','45']
dttm = {}
for hrx in hr:
 for tmx in tm:
  dttm[dat[2]+dat[1]+dat[0]+hrx+tmx] = ''
#print(dttm)
latlon = {}
lines = [line.rstrip('\n') for line in open('arg_aws_agro_meta.csv')]
for inp in lines:
 lst = inp.split(',')
 #print(lst)
 latlon[lst[3]] = [lst[4],lst[5]]
#print(latlon)
st_lst = ['ANDAMAN_AND_NICOBAR','ANDHRA_PRADESH','ARUNACHAL_PRADESH','ASSAM','BANGLADESH','BHUTAN','BIHAR','CHANDIGARH','CHHATISGARH','DAMAN_AND_DIU','DELHI',
'GOA','GUJARAT','HARYANA','HIMACHAL_PRADESH','JAMMU_AND_KASHMIR','JHARKHAND','KARNATAKA','KERALA','LAKSHADWEEP','MADHYA_PRADESH',
'MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','NEPAL','ORISSA','PUDUCHERRY','PUNJAB','RAJASTHAN','SIKKIM',
'TAMIL_NADU','TELANGANA','TRIPURA','UTTARAKHAND','UTTAR_PRADESH','WEST_BENGAL']
tm_lst =['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
for item in st_lst:
 for time in tm_lst:
  url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=aws&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5]
     latlon[name].append([dat[2]+tim[0]+tim[1],rain])
     print('aws',name,dat[2]+tim[0]+tim[1],rain)
for item in st_lst:
 for time in tm_lst:
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5]
     latlon[name].append([dat[2]+tim[0]+tim[1],rain])
     print('arg',name,dat[2]+tim[0]+tim[1],rain)
for item in st_lst:
 for time in tm_lst:
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5]
     latlon[name].append([dat[2]+tim[0]+tim[1],rain])
     print('agro',name,dat[2]+tim[0]+tim[1],rain)
keylist = latlon.keys()
sorted(keylist)
fl = open(dat[2]+dat[1]+dat[0]+'rain.csv','w')
for key in keylist:
 if len(latlon[key]) > 2:
  print(key)
  #['30.99', '78.94', ['280000', '4.0'], ['280100', '4.0'], ['280200', '4.0'], ['280300', '4.0']]
  out = latlon[key]
  print(out[0],out[1])
  dttm = []
  pptn = []
  for num in range(len(out[2:])):
   num = num+2
   print(out[num][0],out[num][1])
   dttm.append(out[num][0])
   pptn.append(float(out[num][1]))
  dif = np.diff(pptn)
  arr = np.array(dif)
  cnt = np.count_nonzero(arr)
  if cnt > 0:
   #txt1 = ','.join([str(x) for x in dttm])
   #print(','.join([str(x) for x in dttm]))
   #fl.write(out[0]+','+out[1]+','+txt1+'\n')
   #print(','.join([str(x)for x in pptn]))
   #txt2 = ','.join([str(x) for x in pptn])
   #fl.write(out[0]+','+out[1]+','+txt2+'\n')
   v = np.array(pptn)
   rn = np.where(v[:-1] != v[1:])[0] + 1
   #print(rn)
   rntime = [dttm[x] for x in rn]
   rnpptn = [pptn[x] for x in rn]
   for l,m in zip(rntime,rnpptn):
    fl.write(str(out[0])+','+str(out[1])+','+str(l)+','+str(m)+'\n')
   #print(','.join([str(x) for x in dif]))
   #txt3 = ','.join([str(x) for x in dif])
   #fl.write(out[0]+','+out[1]+','+txt3+'\n')

