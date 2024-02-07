#
#This program downloads the basic marine data available from NOAA servers
#Author: Dulal Chakrabarti
#Date: 29.01.2024
#
# Install python modules
import netCDF4
import datetime
import xarray as xr
import requests
from bs4 import BeautifulSoup as bsoup
import re
#
hr = datetime.datetime.now(datetime.UTC)
hr1 = hr.strftime('%Y-%m-%d %H:%M:%S')
hr = int(hr1[11:13])
hr = int(hr/6)
#print(hr)
if hr>=0 and hr<1:
 hr = 3
 hr_ = datetime.datetime.now(datetime.UTC)- datetime.timedelta(days=1)
 hr1_ = hr_.strftime('%Y-%m-%d %H:%M:%S')
elif hr>=1 and hr<=2:
 hr = 0
elif hr>2 and hr<=3:
 hr = 2
elif hr>=3:
 hr = 3
else:
 pass
HH = ['00','06','12','18']
if hr == 3:
 dt=hr1_[:10]
 dt=dt.split('-')
 mydate = dt[0]+dt[1]+dt[2]
else:
 dt=hr1[:10]
 dt=dt.split('-')
 mydate = dt[0]+dt[1]+dt[2]
print(mydate)
#
#Wind data from GFS 0.25
#
urlair='http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs'+mydate+'/gfs_0p25_'+HH[hr]+'z'
print(urlair)
dair=xr.open_dataset(urlair)
dair_all = xr.Dataset()
time = dair.variables['time']
lat = dair.variables['lat']
lon = dair.variables['lon']
params = {'apcpsfc':'RAIN','pressfc':'PRES','prmslmsl':'PRESMSL','vissfc':'VIS','ugrd10m':'WINDX10','ugrd30m':'WINDX30','ugrd50m':'WINDX50','vgrd10m':'WINDY10','vgrd30m':'WINDY30','vgrd50m':'WINDY50','gustsfc':'WINDGUST10'}
keylist = params.keys()
for key in keylist:
 dair1 = dair[key][:40,447,290]
 dair_all = dair_all.merge(dair1)
df = dair_all.to_dataframe()
df.to_csv('air.csv')
print("Downloaded air data....")
#
#Wave data from GFSWAVE 0.16
#
urlwave='http://nomads.ncep.noaa.gov:80/dods/wave/gfswave/'+mydate+'/gfswave.global.0p16_'+HH[hr]+'z'
print(urlwave)
ds = xr.open_dataset(urlwave)
ds_all = xr.Dataset()
time = ds.variables['time']
lat = ds.variables['lat']
lon = ds.variables['lon']
wvparams = {'htsgwsfc':'TOTHS','dirpwsfc':'TOTDIR','perpwsfc':'TOTTZ','wvhgtsfc':'WVHS','wvdirsfc':'WVDIR','wvpersfc':'WVTZ','swdir_1':'SWDIR','swper_1':'SWT'}
keylist=wvparams.keys()
for key in keylist:
 ds1 = ds[key][:40,220,435]
 ds_all = ds_all.merge(ds1)
df = ds_all.to_dataframe()
df.to_csv('wave.csv')
#
# Sea area bulletin for South East Arabian Sea
#
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
print("completed all downloads....")
