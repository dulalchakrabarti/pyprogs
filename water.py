import urllib2
import re
from time import sleep
import json
#http://52.172.40.227:8992/services/getLatestDataForStation.aspx?key=controlroom&sid=26
cnt = []
for idx in range(1,3):
 url = "http://52.172.40.227:8992/services/getLatestDataForStation.aspx?key=controlroom&sid=%s"%idx
 print url
 try:
  f1 = urllib2.urlopen(url)
  txt = f1.read()
  f1.close()
  stn = txt[1:-1]
  res = json.loads(stn)
  keylist = res.keys()
  buf = ''
  for key in keylist:
   buf = buf+str(res[key])+' '
  print buf
  sleep(2)
 except:
  pass
print cnt
