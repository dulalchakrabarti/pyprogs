import urllib2
from bs4 import BeautifulSoup
#read lat long file & store in adictionary
stn = {}
fl = open('arg_aws_agro_lat_long.csv')
gl = open('aws.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
#read date & time
date = raw_input('Input date(2018-03-29)?')
time = raw_input('Input time in UTC(1)?')
st_lst = ['ANDAMAN_AND_NICOBAR','ANDHRA_PRADESH','ARUNACHAL_PRADESH','ASSAM','BANGLADESH','BHUTAN','BIHAR','CHANDIGARH','CHHATISGARH','DAMAN_AND_DIU','DELHI',
'GOA','GUJARAT','HARYANA','HIMACHAL_PRADESH','JAMMU_AND_KASHMIR','JHARKHAND','KARNATAKA','KERALA','LAKSHADWEEP','MADHYA_PRADESH',
'MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','NEPAL','ORISSA','PUDUCHERRY','PUNJAB','RAJASTHAN','SIKKIM',
'TAMIL_NADU','TELANGANA','TRIPURA','UTTARAKHAND','UTTAR_PRADESH','WEST_BENGAL']
gl.write('LAT'+','+'LON'+','+'SN'+','+'DT'+','+'ST'+','+'DA'+','+'TM'+','+'TP'+','+'TN'+','+'TX'+','+'TD'+','+'DP'+','+'RH'+','+
'R1'+','+'R2'+','+'wd'+','+'ws'+','+'SP'+','+'MP'+','+'SS'+','+'BT'+','+'GP'+'\n')
for item in st_lst:
 html = urllib2.urlopen("http://210.212.167.219/AWS/data1.php?a=aws&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=0").read()
 #print 'State: '+item
 soup = BeautifulSoup(''.join(html),"lxml")
 table = soup.find('table')
 rows = table.findAll('tr')
 #S NO. 	DISTRICT 	STATION 	DATE(YYYY-MM-DD) 	TIME (UTC) 	TEMP ('C) 	TEMP MIN HOURLY ('C) 	TEMP MAX HOURLY ('C) 	TEMP DAY MIN MAX ('C)	RH (%) 	RAIN HOURLY CUMULATIVE (mm) 	RAIN DAY CUMULATIVE SINCE 0300 UTC (mm)	BATTERY (V) 	GPS
 for tr in rows:
  cols = tr.findAll('td')
  lst = []
  for td in cols:
   lst.append(td.get_text().encode("utf-8"))
  if len(lst)>0:
   name = lst[2]
   stn[name].extend(lst)
keylist = stn.keys()
keylist.sort()
for key in keylist:
 if len(stn[key])>3:
  txt = ','.join(stn[key])
  gl.write(txt+'\n')

