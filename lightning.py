import requests
from bs4 import BeautifulSoup
from time import gmtime, strftime
from datetime import datetime
import time
def sec(strs):
    '''
    '''
    s = strs
    d = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    ss = time.mktime(d.timetuple())
    return ss

fl = open('ltng.csv','w')
url = "https://www.tropmet.res.in/~lln/current-lightning.html"
html = requests.get(url).text
html = html.split('\n')
m1 = 0
m2 = 0
one = 0
dif = 0
flag = True
for item in html:
 if 'var cg20=[' in item:
  m1 = html.index(item)
 elif '[]];' in item:
  m2 = m1+html[m1:].index(item)
 else:
  pass
ltn = html[m1+1:m2]
count = 1
for item in ltn:
 data = item.split(',')
 lat = data[0].strip('[')
 lon = data[1]
 tm1 = data[2].strip(']')
 tm1 = tm1.strip("'")
 if flag:
  one = sec(tm1)
  flag = False
 else:
  dif = sec(tm1)-one 
 if dif >900:
  print(count,lat, lon, int(dif))
  fl.write(str(count)+','+str(lat)+','+str(lon)+','+str(int(dif))+'\n')
  count+=1
