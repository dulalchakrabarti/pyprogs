import requests
from bs4 import BeautifulSoup
import tabula
fl = open('arg_aws_agro_meta.csv','w')
#read AWS lat long file & store in a dictionary
url = 'http://aws.imd.gov.in:8091/AWS/networkmeta.php?a=ARG&b=ALL_STATE'
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
  print(lst)
  txt = ','.join(lst)
  fl.write(txt+'\n')
#read ARG lat long file & store in a dictionary
url = 'http://aws.imd.gov.in:8091/AWS/networkmeta.php?a=AWS&b=ALL_STATE'
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
  print(lst)
  txt = ','.join(lst)
  fl.write(txt+'\n')
#read ARG lat long file & store in a dictionary
url = 'http://aws.imd.gov.in:8091/AWS/networkmeta.php?a=AGRO&b=ALL_STATE'
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
  print(lst)
  txt = ','.join(lst)
  fl.write(txt+'\n')
fl.close()
