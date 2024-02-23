import time
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="aws_new", timeout = None)
#read lat long file & store in adictionary
stn = {}
gl = open('aws.csv','w')
lines = [line.rstrip('\n') for line in open('awslatlong.csv')]
fl = open('awslatlong.csv','a')
ml = open('missing.csv','w')
for inp in lines:
 lst = inp.split(',')
 #print(lst)
 if len(lst)>3:
  stn[lst[3]] = [lst[4],lst[5]]
date = input('Input date(2018-03-29)?')
tm = input('Input time in UTC(1)?')
st_lst = ['ANDAMAN_AND_NICOBAR','ANDHRA_PRADESH','ARUNACHAL_PRADESH','ASSAM','BANGLADESH','BHUTAN','BIHAR','CHANDIGARH','CHHATISGARH','DAMAN_AND_DIU','DELHI',
'GOA','GUJARAT','HARYANA','HIMACHAL_PRADESH','JAMMU_AND_KASHMIR','JHARKHAND','KARNATAKA','KERALA','LAKSHADWEEP','MADHYA_PRADESH',
'MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','NEPAL','ORISSA','PUDUCHERRY','PUNJAB','RAJASTHAN','SIKKIM',
'TAMIL_NADU','TELANGANA','TRIPURA','UTTARAKHAND','UTTAR_PRADESH','WEST_BENGAL']
gl.write('stn'+','+'lat'+','+'lon'+','+'rain'+'\n')

def proc(typ,date,tm):
    '''
    '''
    print('processing.......'+typ)
    count = 0
    for item in st_lst:
     url = "http://aws.imd.gov.in:8091/AWS/dataview.php? a="+typ+"&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+tm+"&h=ALL_MINUTE"
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
       print(lst)
       if name in stn.keys():
        stn[name].append(lst[5])
       else:
        print("new station found...locating...")
        location = geolocator.geocode(name)
        if location != None:
         fl.write(','+','+','+name+','+str(location.latitude)+','+str(location.longitude)+'\n')
         stn[name]=[str(location.latitude)+','+str(location.longitude)+','+lst[5]]
         time.sleep(1.0)
        else:
         print(name+','+'not found'+'\n')
         ml.write(name+','+'not found'+'\n')
         nm = name.split('_')
         nm1 = nm[0]
         location = geolocator.geocode(nm1)
         if location != None:
          fl.write(','+','+','+name+','+str(location.latitude)+','+str(location.longitude)+'\n')
          stn[name]=[str(location.latitude)+','+str(location.longitude)+','+lst[5]]
          print(name+','+'...inserted'+'\n')
          time.sleep(1.0)
      count+=1
    return count
       
tot_count=0
typ_lst = ['aws','arg','agro']
for typ in typ_lst:
 typ_count = proc(typ,date,tm)
 print('processed....'+typ+'....'+str(typ_count))
 tot_count+=typ_count
 for key in stn.keys():
  if len(stn[key]) > 2:
   rain = max(stn[key][2:])
   txt = ','.join(stn[key][:2])
   gl.write(key+','+txt +','+ rain + '\n')
gl.close()
print('total stations processed='+str(tot_count))




