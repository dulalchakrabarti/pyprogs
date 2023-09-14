import urllib2
import pandas as pd
import datetime,time
from bs4 import BeautifulSoup

df  = pd.DataFrame(index = range(31),columns=['00','01','02','03','04','05','06','07','08','09','10','11','12',
'13','14','15','16','17','18','19','20','21','22','23'])
f = urllib2.urlopen("http://www.incois.gov.in/portal/osf/tidegraphphases.jsp?region=Kakinada")
html = f.read()
soup = BeautifulSoup(''.join(html),"lxml")
table = soup.find('table')
rows = table.find_all('tr')
print len(rows)
print rows[7].get_text().encode('utf-8').strip()
'''
n_rows = 0
n_columns = 0
column_names = []
for row in table.find_all('tr'):
                
 # Determine the number of rows in the table
 td_tags = row.find_all('td')
 if len(td_tags) > 0:
  n_rows+=1
  if n_columns == 0:
   # Set the number of columns for our table
   n_columns = len(td_tags)
                        
 # Handle column names if we find them
 th_tags = row.find_all('th') 
 if len(th_tags) > 0 and len(column_names) == 0:
  for th in th_tags:
   column_names.append(th.get_text().encode('utf-8').strip())
print n_rows,n_columns,column_names    
header = []
for table_row in table.findAll('th'):
    header.append(table_row.text.encode('utf-8').strip())
for item in header:
 print item

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text.encode('utf-8').strip())
    output_rows.append(output_row)
print output_rows
headings = []
for td in table_data[0].find_all("td"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())
print headings

rows = table.findAll('tr')
inf = []
for tr in rows:
  cols = tr.findAll('td')
  for td in cols:
      text= td.get_text().encode('utf-8')
      inf.append(text)
for item in inf:
  item = item.replace('AM','AM ')
  item = item.replace('PM','PM ')
  print item

tide = literal_eval(tide)
date = ''
timed = collections.OrderedDict()
for idx in range(len(tide)):
 timestamp = int(tide[idx][0])/1000
 time = datetime.datetime.fromtimestamp(timestamp).strftime('%c')
 tim = time.split()
 hh = tim[3].split(':')
 if tim[2] != date:
  if len(timed)>0:
   for k,v in timed.items():
    df.loc[df.index[int(date)], k] = v
   timed = collections.OrderedDict()
   date = tim[2]
   timed[hh[0]]=tide[idx][1]
  else:
   date = tim[2]
   timed[hh[0]]=tide[idx][1]
 else:
  timed[hh[0]] = tide[idx][1]
for k,v in timed.items():
 df.loc[df.index[int(date)], k] = v
df.dropna().to_csv('tide.csv')
'''
