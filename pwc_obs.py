#Python script to download 15 min observations for one day-needs latlong csv file 'arg_aws_agro_meta.csv'
#Author: Dulal Chakrabarti
#Date:13.7.2022
#import modules
import requests
from bs4 import BeautifulSoup
import tabula
import numpy as np
#input date
date = input('Input date(2018-03-29)?')
dat = date.split('-')
#read lat long file for stations and store in a dictionary: if there is key error update file with new lat long of station
latlon = {}
lines = [line.rstrip('\n') for line in open('arg_aws_agro_meta.csv')]
for inp in lines:
 lst = inp.split(',')
 #print(lst)
 latlon[lst[3]] = [lst[4],lst[5]]
#print(latlon)
st_lst = ['UTTAR_PRADESH']# can add more states
tm_lst =['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
#open output csv file
fl = open(dat[2]+dat[1]+dat[0]+'rain_up.csv','w')
##aws stations
fl.write('type'+','+'name'+','+'time'+','+'lat'+','+'lon'+','+'rain'+','+'temp'+','+'tmin'+','+'tmax'+','+'rh'+','+'rhdaymin/max'+','+'wd10'+','+'ws10'+','+'gust10'+','+'slp'+','+'mslp'+','+'sunshine'+','+'bat'+','+'gps'+','+'\n')
#start download
for item in st_lst:
 for time in tm_lst:
  url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=aws&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5:]
     rn = ','.join(rain)
     latlon[name].append([dat[2]+tim[0]+tim[1],rn])
     print('aws'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn)
     fl.write('aws'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn+'\n')
##arg stations
fl.write('type'+','+'name'+','+'time'+','+'lat'+','+'lon'+','+'rain'+','+'temp'+','+'tmin'+','+'tmax'+','+'rh'+','+'rhdaymin/max'+','+'bat'+','+'gps'+','+'\n')
for item in st_lst:
 for time in tm_lst:
  url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=arg&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5:]
     rn = ','.join(rain)
     latlon[name].append([dat[2]+tim[0]+tim[1],rn])
     print('arg'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn)
     fl.write('arg'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn+'\n')
##agro stations
fl.write('type'+','+'name'+','+'time'+','+'lat'+','+'lon'+','+'rain'+','+'temp'+','+'tmin'+','+'tmax'+','+'rh'+','+'rhdaymin/max'+','+'wd10'+','+'ws10'+','+'gust10'+','+'wd3'+','+'ws3'+','+'gust3'+','+'slp'+','+'mslp'+','+'sunshine'+','+'st10'+','+'sm10'
+','+'st30'+','+'sm30'+','+'st70'+','+'sm70'+','+'st100'+','+'sm100'+','+'glorad'+','+'par'+','+'bat'+','+'gps'+','+'\n')
for item in st_lst:
 for time in tm_lst:
  url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=agro&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5:]
     rn =','.join(rain)
     latlon[name].append([dat[2]+tim[0]+tim[1],rn])
     print('agro'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn)
     fl.write('agro'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn+'\n')
##awsagro stations
fl.write('type'+','+'name'+','+'time'+','+'lat'+','+'lon'+','+'rain'+','+'temp'+','+'tmin'+','+'tmax'+','+'rh'+','+'rhdaymin/max'+','+'wd10'+','+'ws10'+','+'gust10'+','+'wd3'+','+'ws3'+','+'gust3'+','+'slp'+','+'mslp'+','+'sunshine'+','+'st10'+','+'sm10'
+','+'st30'+','+'sm30'+','+'st70'+','+'sm70'+','+'st100'+','+'sm100'+','+'glorad'+','+'par'+','+'bat'+','+'gps'+','+'\n')
for item in st_lst:
 for time in tm_lst:
  url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWSAGRO&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
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
    if lst[5] != '' and float(lst[5])>0:
     name = lst[2]
     dat = lst[3].split('-')
     tim = lst[4].split(':')
     rain = lst[5:]
     rn = ','.join(rain)
     latlon[name].append([dat[2]+tim[0]+tim[1],rn])
     print('AWSAGRO'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn)
     fl.write('AWSAGRO'+','+name+','+dat[2]+tim[0]+tim[1]+','+latlon[name][0]+','+latlon[name][1]+','+rn+'\n')

