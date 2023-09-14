import urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen("http://aws.imd.gov.in/AWS/dataview.php?a=aws&b=HARYANA&c=ALL_DISTRICT&d=ALL_STATION&e=2019-07-31&f=2019-07-31&g=ALL_HOUR&h=ALL_MINUTE").read()
soup = BeautifulSoup(''.join(html),"lxml")
table = soup.find('table')
rows = table.findAll('tr')
gl = open('marutiaws.csv','w')
gl.write('NO'+','+'DISTRICT'+','+'STATION'+','+'DATE'+','+'TIME'+','+'RAIN'+','+'TMP'+','
+'TMAX/MIN'+','+'RH'+','+'WD'+','+'WS'+','+'SLP'+','+'MSLP'+','
+'SUNSHINE'+','+'BAT'+','+'GPS'+'\n')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text().encode("utf-8"))
 for i in range(len(lst)):
  gl.write(str(lst[i])+',')
 gl.write('\n')
gl.close()
