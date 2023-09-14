import requests
from bs4 import BeautifulSoup
date = input('Input date(27)?')
txt = 'https://www.aviationweather.gov/metar/data?ids=VOVZ%20VOTR%20VOHS%20VOML%20VOCL%20VOBL%20VOCB%20VOCI%20VEGT%20VEPT%20VAAH%20VANP%20VEBS%20VILK%20VOTV%20VIJP%20VIDP%20VECC%20VABB%20VOMM&format=decoded&hours=96&taf=off&layout=on'
r1 = requests.get(txt)
resp = r1.text
soup = BeautifulSoup(resp,"lxml")
rows = soup.findAll('tr')
#print(rows)
lst = []
flag = False
stn = ''
tm = ''
for tr in rows:
 cols = tr.findAll('td')
 for td in cols:
  lst.append(td.get_text())
for num in range(len(lst)):
 if lst[num] == 'Text:':
  metar = lst[num+1].split()
  if date == metar[1][:2]:
   stn = metar[0]
   tm = metar[1]
   flag = True
 elif flag and lst[num] == 'Visibility:':
  vis = lst[num+1]
  flag = False
  print(stn,tm,vis)

