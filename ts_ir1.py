import http
import numpy as np
import time
import requests
import json
seconds1 = time.time()
date1_ = input('Start date(2018-03-29)?')
date1 = date1_.split('-')
time1 = input('Start time(07:45:00.000)?')
date2_ = input('End date(2018-03-29)?')
date2 = date2_.split('-')
time2 = input('End time(07:45:00.000)?')
gl = open(date1[2]+date1[1]+date1[0]+'-'+date2[2]+date2[1]+date2[0]+'rain.csv','a+')
fl = open(date1[2]+date1[1]+date1[0]+'rain.csv')
def count_out(lo, la, dr):
    '''
    '''
    lo = float(lo)
    la = float(la)
    print(lo,la)
    dlon = 15.908203125
    dlat = 12.919921875
    lllo = lo - dlon
    llla = la - dlat
    urlo = lo + dlon
    urla = la + dlat
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=362&J=294&TIME="+date1_+"T"+time1+"Z/"+date2_+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3"+dr+"IMG_L1B_STD4/IMG_TIR1&LAYERS=3"+dr+"IMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=724&HEIGHT=588"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     print(data['domain']['axes']['x']['values'],data['domain']['axes']['y']['values'])
     print(data['ranges']['IMG_TIR1']['values'])
     print(data['domain']['axes']['t']['values'])
    except requests.exceptions.ConnectionError:
     print('Timed out!!')
count = 0
lines = [line.rstrip('\n') for line in fl]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 tm = lst[2]
 dr = tm[4:]
 if dr == '15' or dr == '45':
  dr = 'R'
 else:
  dr = 'D'
 buf = count_out(lon,lat,dr)
 print('..............'+dr+'...................')
 count+=1
 #gl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
 #if count > 0:
  #seconds2 = time.time()
  #print('elapsed minutes....',(seconds2-seconds1)/60.0)
  #exit()
#gl.close()
print(count)
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)
