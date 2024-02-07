#
#This program generates graphics from the basic marine data available from NOAA servers.
#Author: Dulal Chakrabarti
#Date: 05.02.2024
#
# Install python modules
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
import numpy as np
from metpy.units import units
import pandas as pd
from datetime import datetime,timezone,timedelta
import matplotlib as mpl
import requests
from bs4 import BeautifulSoup as bsoup
import math
#Write weather summary in a figure
#Define helper functions
fig,ax = plt.subplots(figsize=(14,14))
def tm_reorder(st):
    st = st.split('-')
    buf = st[2].split(':')
    buf_ = buf[0].split()
    dttm = buf_[0]+st[1]+buf_[1]+buf[1]
    return dttm
def degToCompass(num):
     val=int((num/22.5)+.5)
     arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
     return arr[val%16]
    
def gen_arrow_head_marker(rot):
    arr = np.array([[.1, .3], [.1, -.3], [1, 0], [.1, .3]])  # arrow shape
    angle = rot / 180 * np.pi
    rot_mat = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
        ])
    arr = np.matmul(arr, rot_mat)  # rotates the arrow

    # scale
    x0 = np.amin(arr[:, 0])
    x1 = np.amax(arr[:, 0])
    y0 = np.amin(arr[:, 1])
    y1 = np.amax(arr[:, 1])
    scale = np.amax(np.abs([x0, x1, y0, y1]))
    codes = [mpl.path.Path.MOVETO, mpl.path.Path.LINETO,mpl.path.Path.LINETO, mpl.path.Path.CLOSEPOLY]
    arrow_head_marker = mpl.path.Path(arr, codes)
    return arrow_head_marker, scale
print("Opening.. sea.csv... text file for writing texts....")
fl = open("sea.csv", "w")

#
# Coastal bulletin for South Gujrat coast
#
urlsyn1='https://mausam.imd.gov.in/Forecast/coastal_bulletin_new.php?id=3'
html = requests.get(urlsyn1).text
soup = bsoup(html,"html.parser")
soup.prettify()
tables = soup.find_all("table")
cap = soup.find_all('caption')
for num in range(len(tables)):
 rows = tables[num].findAll('tr')
 if num == 0:
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
 elif num == 2:
  buf = cap[1].get_text()
  fl.write(buf+'\n')
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
 elif num == 3:
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
#
# Sea area bulletin for North East Arabian sea...
#
urlsyn='https://mausam.imd.gov.in/Forecast/seaarea_bulletin_new.php?id=4'
html = requests.get(urlsyn).text
soup = bsoup(html,"html.parser")
soup.prettify()
tables = soup.find_all("table")
cap = soup.find_all('caption')
for num in range(len(tables)):
 rows = tables[num].findAll('tr')
 if num == 0:
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
 elif num == 1:
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
 elif num == 3:
  buf = cap[3].get_text()
  fl.write(buf+'\n')
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
 elif num == 13:
  for tr in rows:
   cols = tr.findAll('td')
   lst = []
   for td in cols:
    lst.append(td.get_text()) 
   buf=','.join(x for x in lst)
   fl.write(buf+'\n')
fl.close()
lines = [line.rstrip('\n') for line in open('sea.csv')]
fc = {}
for line in lines:
 line = line.split(',')
 if len(line) > 0:
  fc[line[0]+':']=''.join(x for x in line[1:])
#
# Meteorological analysis for India and neighbouring countries
#
url = 'https://tgftp.nws.noaa.gov/data/raw/ww/wwin40.dems..txt'
html = requests.get(url).text
html = html.split(':')
buf = html[1].split('\n')
txt = [x for x in buf[:-1] if x != '']
buf = ''.join(x for x in txt)
buf = buf.lower()
fc['Synoptic Situation:'] = buf
#
# City weather for Dahej...
#
url = 'https://city.imd.gov.in/citywx/city_weather_test_try.php?id=42838'
html = requests.get(url).text
soup = bsoup(html,"html.parser")
soup.prettify()
cols = soup.findAll('td')
fl = open('xx.txt','w')
for td in cols:
 buf = td.get_text().rstrip()
 buf = buf.split()
 txt=''.join(x for x in buf)
 fl.write(txt+'\n')
fl.close()
wx = []
lines = [line.rstrip() for line in open('xx.txt')]
for line in lines:
 wx.append(line)
#print(wx)
for i in range(len(wx)):
 if 'Maximum' in wx[i]:
  fc['Maximum:'] = str(wx[i+1])
 elif 'Departure' in wx[i]:
  if 'MaxDeparture:' not in fc.keys():
   fc['MaxDeparture:'] = str(wx[i+1])
  elif 'MinDeparture:' not in fc.keys():
   fc['MinDeparture:'] = str(wx[i+1])
 elif 'Minimum' in wx[i]:
  fc['Minimum:'] = str(wx[i+1])
 elif '24HoursRainfall(mm)' in wx[i]:
  fc['24HoursRainfall(mm):'] = str(wx[i+1])
 elif 'RelativeHumidityat0830hrs(%)' in wx[i]:
  fc['Relative Humidity at 0830 hrs(%):'] = str(wx[i+1])
 elif 'RelativeHumidityat1730hrs(%)' in wx[i]:
  fc['Relative Humidity at 1730 hrs(%):'] = str(wx[i+1])
 elif 'TodaysSunset(IST)' in wx[i]:
  fc['Todays Sunset(IST):'] = str(wx[i+1])
 elif 'Tomorrow\'sSunrise(IST)' in wx[i]:
  fc['Tomorrow''s Sunrise(IST):'] = str(wx[i+1])
 elif '7Day\'sForecast' == wx[i]:
  fc['Forecast'+str(wx[i+5])+':'] ='Min:'+' '+str(wx[i+6])+' '+'Max:'+' '+str(wx[i+7])+' '+'Weather:'+' '+str(wx[i+9])
  fc['Forecast'+str(wx[i+10])+':'] ='Min:'+' '+str(wx[i+11])+' '+'Max:'+' '+str(wx[i+12])+' '+'Weather:'+' '+str(wx[i+14])
  fc['Forecast'+str(wx[i+15])+':'] ='Min:'+' '+str(wx[i+16])+' '+'Max:'+' '+str(wx[i+17])+' '+'Weather:'+' '+str(wx[i+19])
  fc['Forecast'+str(wx[i+20])+':'] ='Min:'+' '+str(wx[i+21])+' '+'Max:'+' '+str(wx[i+22])+' '+'Weather:'+' '+str(wx[i+24])
  fc['Forecast'+str(wx[i+25])+':'] ='Min:'+' '+str(wx[i+26])+' '+'Max:'+' '+str(wx[i+27])+' '+'Weather:'+' '+str(wx[i+29])
keylist = [x for x in fc.keys() if fc[x] != '']
x = np.arange(35)
y = np.arange(35)
y1=np.ones_like(y)
y2=y1*35
ax.plot(x,y1,color='black')
ax.plot(x,y2,color='black')
i=35
j=32
for key in keylist:
 if fc[key] != '':
  txt = key+fc[key]
  if (len(txt)) > 100:
   m = int(len(txt)/100)
   l = int(len(txt)%100)
   for n in range(m):
    var = str(n)
    r1 = n*100
    r2 = (n+1)*100
    buf = txt[r1:r2]
    ax.text(1, j, buf,color='black')
    j-=1.2
   buf1 = txt[r2:]
   ax.text(1, j, buf1,color='black')
   j-=1
  else:
   ax.text(1, j, txt,color='black')
   j-=1
ax.set_title('Weather Summary for location Latitude:21.67 and Longitude:72.51',fontsize = 14)
plt.savefig("fc.jpg")
plt.show()
df = pd.DataFrame.from_dict(fc,orient='index', columns=['par'])
df.to_csv('fc.csv')
print('opening.....air.csv')   
df1 = pd.read_csv('air.csv')
tm1 = df1['time'].values
tm_ = [(datetime.strptime(x, '%Y-%m-%d %H:%M:%S')+timedelta(hours=5,minutes=30)).strftime('%Y-%m-%d %H:%M:%S') for x in tm1]
tm = [tm_reorder(x) for x in tm_]
uknots = df1['ugrd10m'].values*units("meter / second").to( units("knot"))
vknots = df1['vgrd10m'].values*units("meter / second").to( units("knot"))
wgust = df1['gustsfc'].values*units("meter / second").to( units("knot"))
# Calculate the wind speed and generate wind chart
ws = mpcalc.wind_speed(uknots, vknots)
ws_ = [str(x).split() for x in ws]
ws_ = [int(float(x[0])) for x in ws_ ]
wg_ = [str(x).split() for x in wgust]
wg_ = [int(float(x[0])) for x in wg_ ]
wgd = mpcalc.wind_direction(uknots, vknots,'from')
ug,vg = mpcalc.wind_components(wgust,wgd)
uknots = df1['ugrd30m'].values*units("meter / second").to( units("knot"))
vknots = df1['vgrd30m'].values*units("meter / second").to( units("knot"))
ws30 = mpcalc.wind_speed(uknots, vknots)
ws30_ = [str(x).split() for x in ws]
ws30_ = [int(float(x[0])) for x in ws30_ ]
uknots = df1['ugrd50m'].values*units("meter / second").to( units("knot"))
vknots = df1['vgrd50m'].values*units("meter / second").to( units("knot"))
ws50 = mpcalc.wind_speed(uknots, vknots)
ws50_ = [str(x).split() for x in ws50]
ws50_ = [int(float(x[0])) for x in ws50_ ]
rain = df1['apcpsfc'].values
mslp = df1['prmslmsl'].values
vis = df1['vissfc'].values
fig,ax = plt.subplots(figsize=(14,14))
ax.set_ylim(-3,35)
ax.grid()
ax.plot(tm,ws,label='10m wind')
ax.plot(tm,wgust,label='10m gust')
for i in range(len(ws_)):
 txt = str(ws_[i])+'g'+str(wg_[i])
 ax.text(i,ws[i],txt)
ax.barbs(tm,ws_,uknots,vknots,zorder=5)
ax.barbs(tm,ws_,ug,vg,color='red',zorder=4)
ax.plot([0, 39],[25, 25], linewidth=4, color='tab:orange')
ax.text(39,25,'Critical Level 1')
ax.plot([0, 39],[30, 30], linewidth=4, color='r')
ax.text(39,30,'Critical Level 2')
ax.text(39,25,'Critical Level 1')
ax.text(5,20,'& 5g7 means wind barb 5 knots gusting to 7 knots coming from NNE(NorthNorthEast) direction')
ax.text(4,20,'/-')
ax.text(1,23,'N')
ax.text(1,22,'/\\')
ax.text(1,21,'|')
ax.text(1,20,'--->E')
ax.text(1,19,'|')
ax.text(1,18,'V')
ax.text(1,17,'S')
ax.text(0,20,'W<---')
ax.text(1,21,'I')
ax.set_title('Wind Charts for location Latitude:21.67 and Longitude:72.51',fontsize = 14) 
ax.legend(loc = 'upper left')
plt.xticks(rotation = 80, rotation_mode="anchor")
plt.xlabel('Hours(IST)')
plt.savefig("wind.jpg")
plt.show()
fig,ax = plt.subplots(figsize=(14,14))
df1 = pd.read_csv('wave.csv')
#Total sea combined swell and significant wave parameters
tot_ht = df1['htsgwsfc'].values
tot_dir = df1['dirpwsfc'].values
tot_per = df1['perpwsfc'].values
U = np.cos(tot_dir) * tot_ht
V = np.sin(tot_dir) * tot_ht
ax.plot(tm,tot_ht,color='orange')
dr = []
for i in range(len(tot_dir)):
 txt1 = degToCompass(tot_dir[i])
 dr.append(txt1)
for i in range(0,len(tot_ht),4):
 txt = str(round(tot_ht[i],2))+'m'+str(round(tot_per[i],1))+dr[i]
 ax.text(i,tot_ht[i]+.1,txt)
tot_ht_ = tot_ht+0.3
for i in range(len(tot_dir)):
 rot = tot_dir[i]
 marker, scale = gen_arrow_head_marker(rot)
 markersize = 30
 ax.scatter(tm[i],tot_ht[i],marker=marker, s=(markersize*scale)**2,color='black')
ax.scatter(tm[i],tot_ht[39],marker=marker, s=(markersize*scale)**2,color='orange',label="Total(sw+wv) height(m)/Dir")
#Significant wave parameters
wv_ht_mean = df1['wvhgtsfc'].mean()
df1['wvhgtsfc'].fillna(value=wv_ht_mean, inplace=True)
wv_ht = df1['wvhgtsfc'].values
wv_dir_mean = df1['wvdirsfc'].mean()
df1['wvdirsfc'].fillna(value=wv_dir_mean, inplace=True)
wv_dir = df1['wvdirsfc'].values
wv_per_mean = df1['wvpersfc'].mean()
df1['wvpersfc'].fillna(value=wv_per_mean, inplace=True)
wv_per = df1['wvpersfc'].values
wv_ht = wv_ht+1
ax.plot(tm,wv_ht,color='blue')
dr = []
for i in range(len(wv_dir)):
 txt1 = degToCompass(wv_dir[i])
 dr.append(txt1)
for i in range(0,len(wv_ht),4):
 txt = str(round(wv_ht[i],2))+'m'+str(round(wv_per[i],1))+dr[i]
 ax.text(i,wv_ht[i]+.1,txt)
for i in range(len(wv_dir)):
 rot = wv_dir[i]
 marker, scale = gen_arrow_head_marker(rot)
 markersize = 30
 ax.scatter(tm[i],wv_ht[i],marker=marker, s=(markersize*scale)**2,color='black')
ax.scatter(tm[i],wv_ht[38],marker=marker, s=(markersize*scale)**2,color='blue',label= "Wave height(m)/Dir")
#Swell parameters
sw_dir_mean = df1['swdir_1'].mean()
if(math.isnan(sw_dir_mean)):
 txt = 'Swell forecast not available'
 ax.text(1,1.6,txt)
else:
 df1['swdir_1'].fillna(value=sw_dir_mean, inplace=True)
 sw_dir = df1['swdir_1'].values
 sw_per_mean = df1['swper_1'].mean()
 df1['swper_1'].fillna(value=sw_per_mean, inplace=True)
 sw_per = df1['swper_1'].values
 wv_ht = df1['wvhgtsfc'].values
 wv_ht1 = wv_ht+1.5
 ax.plot(tm,wv_ht1,color='green')
 dr = []
 for i in range(len(sw_dir)):
  txt1 = degToCompass(sw_dir[i])
  dr.append(txt1)
 for i in range(0,len(wv_ht1),4):
  txt = str(round(wv_ht[i],2))+'m'+str(round(sw_per[i],1))+dr[i]
  ax.text(i,wv_ht1[i]+.1,txt)
 for i in range(len(sw_dir)):
  rot = sw_dir[i]
  marker, scale = gen_arrow_head_marker(rot)
  markersize = 30
  ax.scatter(tm[i],wv_ht1[i],marker=marker, s=(markersize*scale)**2,color='black')
 ax.scatter(tm[i],wv_ht1[37],marker=marker, s=(markersize*scale)**2,color='green',label="Swell height(m)/Dir")
plt.xticks(rotation = 80, rotation_mode="anchor")
ax.set_ylim(-0.5,3)
ax.plot([0, 39],[2, 2], linewidth=4, color='tab:orange')
ax.plot([0, 39],[2.5, 2.5], linewidth=4, color='tab:red')
ax.text(0,2.1,'Critical Level 1')
ax.text(0,2.6,'Critical Level 2')
ax.grid()
ax.text(1,.6,'1.5m2.0NNE means height:1.5 m,per:2.0 min heading towards NNE(NorthNorthEast) direction')
plt.xlabel('Hours(IST)')
ax.legend(loc = 'upper right')
ax.set_title('Wave Charts for location Latitude:21.67 and Longitude:72.51',fontsize = 14)
plt.savefig("wave.jpg")
plt.show()
df2 = pd.DataFrame(data=None, columns=['DateTime(IST)','WDir(deg)','WS10(knot)','WG10(knot)','WS30(knot)','WS50(knot)',
'Twh(m)','Twdir(deg)','Twz(min)','Swdir(deg)','Swp(min)','Rain(mm)','Pres(pa)','Vis(m)'])
df2['DateTime(IST)'] = tm
df2['WDir(deg)'] = wgd
df2['WS10(knot)'] = ws_
df2['WG10(knot)'] = wg_
df2['WS30(knot)'] = ws30_
df2['WS50(knot)'] = ws50_
df2['Twh(m)'] = tot_ht
df2['Twdir(deg)'] = tot_dir
df2['Twz(min)'] = tot_per
sw_dir_mean = df1['swdir_1'].mean()
if(math.isnan(sw_dir_mean)):
 print('Swell forecast not available')
else:
 df2['Swdir(deg)'] = sw_dir
 df2['Swp(min)'] = sw_per
df2['Rain(mm)'] = rain
df2['Pres(pa)'] = mslp
df2['Vis(m)'] = vis
df2.to_csv("dahej.csv")
print("table written to dahej.csv")
