import urllib2
from bs4 import BeautifulSoup
f1 = urllib2.urlopen("http://aws.imd.gov.in/AWS/dataview.php?a=aws&b=DELHI&c=ALL_DISTRICT&d=ALL_STATION&e=2019-02-05&f=2019-02-05&g=ALL_HOUR&h=ALL_MINUTE")
html = f1.read()
soup = BeautifulSoup(''.join(html),"lxml")
table = soup.find('table')
rows = table.findAll('tr')
#S NO. 	DISTRICT 	STATION 	DATE(YYYY-MM-DD) 	TIME (UTC) 	TEMP ('C) 	TEMP MIN HOURLY ('C) 	TEMP MAX HOURLY ('C) 	TEMP DAY MIN MAX ('C)	RH (%) 	RAIN HOURLY CUMULATIVE (mm) 	RAIN DAY CUMULATIVE SINCE 0300 UTC (mm)	BATTERY (V) 	GPS
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text().encode("utf-8"))
 print lst
