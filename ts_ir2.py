import http
import numpy as np
import time
import requests
import json
seconds1 = time.time()
date1_ = input('Start date(2018-03-29)?')
date1 = date1_.split('-')
time1 = '00:00:00.000'
date2_ = input('End date(2018-03-29)?')
date2 = date2_.split('-')
time2 = '00:00:00.000'
gl = open(date1[2]+date1[1]+date1[0]+'-'+date2[2]+date2[1]+date2[0]+'rain.csv','w')
fl = open(date1[2]+date1[1]+date1[0]+'rain.csv')
def count_out(lo, la):
    '''
    '''
    ser = []
    lo = float(lo)
    la = float(la)
    dlon = 15.908203125
    dlat = 12.919921875
    lllo = lo - dlon
    llla = la - dlat
    urlo = lo + dlon
    urla = la + dlat
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=362&J=294&TIME="+date1_+"T"+time1+"Z/"+date2_+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3DIMG_L1B_STD4/IMG_TIR1&LAYERS=3DIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=724&HEIGHT=588"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='D'
     dval = data['ranges']['IMG_TIR1']['values']
     dtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(dtime)
     ser.append(dval)
    except requests.exceptions.ConnectionError:
     print('D-Timed out!!')
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=362&J=294&TIME="+date1_+"T"+time1+"Z/"+date2_+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=724&HEIGHT=588"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='R'
     rval = data['ranges']['IMG_TIR1']['values']
     rtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(rtime)
     ser.append(rval)
    except requests.exceptions.ConnectionError:
     print('R-Timed out!!')
    return ser
count = 0
d = {}
lines = [line.rstrip('\n') for line in fl]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 val = lat+'_'+lon
 d[val] = lst[-1]
keylist = d.keys()
sorted(keylist)
#print(d)
d_ = {}
for key in d.copy():
 lst = key.split('_')
 #print(lst[0],lst[1])
 buf = count_out(lst[1],lst[0])
 #print(len(buf))
 if len(buf) != 6:
   buf = count_out(lon,lat)
 else:
  d_[date1_+'_'+buf[0]] = [buf[1],buf[2]]
  d_[date1_+'_'+buf[3]] = [buf[4],buf[5]]
  count+=1
  print('..............'+lst[1]+','+lst[0]+'.........'+str(count)+'..........')
keylist = d_.keys()
sorted(keylist)
for key in keylist:
 #print(key,d_[key])
 gl.write(str(key)+','+str(d_[key])+'\n')
gl.close()
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)
