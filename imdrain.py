import httplib 
import urllib 
import urllib2 
from bs4 import BeautifulSoup
import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
url = 'http://hydro.imd.gov.in/hydrometweb/(S(byyhp455hq1m1ivpul5tdbnj))/landing.aspx'
br.open(url)
response = br.response().read()
soup = BeautifulSoup(''.join(response),'lxml')
table = soup.find('table',id="rfGrid")
rows = table.findAll('tr')
fl = open('aws.csv','w')
for tr in rows:
  stn = []
  cols = tr.findAll('td')
  for td in cols:
      text= td.get_text().encode('utf8').strip('\n')
      stn.append(text)
  if len(stn)>0: fl.writelines( stn[0]+','+stn[1]+','+stn[2]+'\n' )
fl.close()
