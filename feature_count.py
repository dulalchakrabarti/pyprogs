import urllib.request
import time
from urllib.error import HTTPError,URLError
#from socket import timeout
fl = open('ftr_ir1.csv','w')
fl.write('lat'+','+'lon'+','+'cls'+','+'cnt'+'\n')
seconds1 = time.time()
def ret_val1(i,j):
    '''
    '''
    print(i,j)
    f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetFeatureInfo&version=1.3.0&CRS=CRS:84&BBOX=60,-4,110,12&I="+str(i)+"&J="+str(j)+"&TIME=2021-10-25T03:15:00&INFO_FORMAT=text/xml&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=1282&HEIGHT=358",timeout=None)
    txt1 = f1.read().decode('utf-8')
    f1.close()
    val_ = txt1.split('<value>')
    val = val_[1].split('</value>')
    val = val[0]
    return(val)
##########
def ret_val2(i,j):
    '''
    '''
    print(i,j)
    f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetFeatureInfo&version=1.3.0&CRS=CRS:84&BBOX=60,12,110,28&I="+str(i)+"&J="+str(j)+"&TIME=2021-10-25T03:15:00&INFO_FORMAT=text/xml&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=1282&HEIGHT=358",timeout=None)
    txt1 = f1.read().decode('utf-8')
    f1.close()
    val_ = txt1.split('<value>')
    val = val_[1].split('</value>')
    val = val[0]
    return(val)
##########
def ret_val3(i,j):
    '''
    '''
    print(i,j)
    f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetFeatureInfo&version=1.3.0&CRS=CRS:84&BBOX=60,28,110,44&I="+str(i)+"&J="+str(j)+"&TIME=2021-10-25T03:15:00&INFO_FORMAT=text/xml&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=1282&HEIGHT=358",timeout=None)
    txt1 = f1.read().decode('utf-8')
    f1.close()
    val_ = txt1.split('<value>')
    val = val_[1].split('</value>')
    val = val[0]
    return(val)
##########
def ret_val4(i,j):
    '''
    '''
    print(i,j)
    f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetFeatureInfo&version=1.3.0&CRS=CRS:84&BBOX=60,20,110,36&I="+str(i)+"&J="+str(j)+"&TIME=2021-10-25T03:15:00&INFO_FORMAT=text/xml&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=1282&HEIGHT=358",timeout=None)
    txt1 = f1.read().decode('utf-8')
    f1.close()
    val_ = txt1.split('<value>')
    val = val_[1].split('</value>')
    val = val[0]
    return(val)
##########
dx =0.031201248
dy=.044692737430168
stn = {}
lines = [line.rstrip('\n') for line in open('class.csv')]
for inp in lines:
 lst = inp.split(',')
 stn[lst[0]] = lst[1:]
dec = {}
for key,val in stn.items():
 city = key
 city1 = city+'_'
 city2 = city+'__'
 city3 = city+'___'
 if city in dec:
  city = city+'_'
 elif city1 in dec:
  city = city1+'_'
 elif city2 in dec:
  city = city2+'_'
 elif city3 in dec:
  city = city3+'_'
 dec[city] = []
 lat = val[1]
 dec[city].append(lat)
 lon = val[2]
 dec[city].append(lon)
 cls = val[3]
 dec[city].append(cls)
#print(dec)
keylist = dec.keys()
sorted(keylist)
#print(len(keylist))
count=0
for key in keylist:
 lat = float(dec[key][0])
 lon = float(dec[key][1])
 cls = dec[key][2]
 if lat < 12:
  out1 = []
  i = round((lon-60)/dx)
  j = round((lat+4)/dy)
  pixel = [[i-4,j+4],[i-3,j+4],[i-2,j+4],[i-1,j+4],[i,j+4],[i+1,j+4],[i+2,j+4],[i+3,j+4],[i+4,j+4],
[i-4,j+3],[i-3,j+3],[i-2,j+3],[i-1,j+3],[i,j+3],[i+1,j+3],[i+2,j+3],[i+3,j+3],[i+4,j+3],
[i-4,j+2],[i-3,j+2],[i-2,j+2],[i-1,j+2],[i,j+2],[i+1,j+2],[i+2,j+2],[i+3,j+2],[i+4,j+2],
[i-4,j+1],[i-3,j+1],[i-2,j+1],[i-1,j+1],[i,j+1],[i+1,j+1],[i+2,j+1],[i+3,j+1],[i+4,j+1],
[i-4,j],[i-3,j],[i-2,j],[i-1,j],[i,j],[i+1,j],[i+2,j],[i+3,j],[i+4,j],
[i-4,j-1],[i-3,j-1],[i-2,j-1],[i-1,j-1],[i,j-1],[i+1,j-1],[i+2,j-1],[i+3,j-1],[i+4,j-1],
[i-4,j-2],[i-3,j-2],[i-2,j-2],[i-1,j-2],[i,j-2],[i+1,j-2],[i+2,j-2],[i+3,j-2],[i+4,j-2],
[i-4,j-3],[i-3,j-3],[i-2,j-3],[i-1,j-3],[i,j-3],[i+1,j-3],[i+2,j-3],[i+3,j-3],[i+4,j-3],
[i-4,j-4],[i-3,j-4],[i-3,j-4],[i-1,j-4],[i,j-4],[i+1,j-4],[i+2,j-4],[i+3,j-4],[i+4,j-4]]
  for item in pixel:
   x = item[0]
   y = item[1]
   #time.sleep(0.5)
   try:
    out1.append(ret_val1(x,y))
   except (TimeoutError) as error:
    out1.append(ret_val1(x,y))
   except (HTTPError, URLError) as error:
    out1.append(ret_val1(x,y))
  #print(out1)
  val = ','.join(str(x) for x in out1)
  fl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
  count+=1
  print(count)
 elif lat > 12 and lat < 28:
  out2 = []
  i = round((lon-60)/dx)
  j = round((lat-12)/dy)
  pixel = [[i-4,j+4],[i-3,j+4],[i-2,j+4],[i-1,j+4],[i,j+4],[i+1,j+4],[i+2,j+4],[i+3,j+4],[i+4,j+4],
[i-4,j+3],[i-3,j+3],[i-2,j+3],[i-1,j+3],[i,j+3],[i+1,j+3],[i+2,j+3],[i+3,j+3],[i+4,j+3],
[i-4,j+2],[i-3,j+2],[i-2,j+2],[i-1,j+2],[i,j+2],[i+1,j+2],[i+2,j+2],[i+3,j+2],[i+4,j+2],
[i-4,j+1],[i-3,j+1],[i-2,j+1],[i-1,j+1],[i,j+1],[i+1,j+1],[i+2,j+1],[i+3,j+1],[i+4,j+1],
[i-4,j],[i-3,j],[i-2,j],[i-1,j],[i,j],[i+1,j],[i+2,j],[i+3,j],[i+4,j],
[i-4,j-1],[i-3,j-1],[i-2,j-1],[i-1,j-1],[i,j-1],[i+1,j-1],[i+2,j-1],[i+3,j-1],[i+4,j-1],
[i-4,j-2],[i-3,j-2],[i-2,j-2],[i-1,j-2],[i,j-2],[i+1,j-2],[i+2,j-2],[i+3,j-2],[i+4,j-2],
[i-4,j-3],[i-3,j-3],[i-2,j-3],[i-1,j-3],[i,j-3],[i+1,j-3],[i+2,j-3],[i+3,j-3],[i+4,j-3],
[i-4,j-4],[i-3,j-4],[i-3,j-4],[i-1,j-4],[i,j-4],[i+1,j-4],[i+2,j-4],[i+3,j-4],[i+4,j-4]]
  for item in pixel:
   x = item[0]
   y = item[1]
   try:
    out2.append(ret_val2(x,y))
   except (TimeoutError) as error:
    out2.append(ret_val2(x,y))
   except (HTTPError, URLError) as error:
    out2.append(ret_val2(x,y))
  #print(out2)
  val = ','.join(str(x) for x in out2)
  fl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
  count+=1
  print(count)
 elif lat > 32:
  out3 = []
  i = round((lon-60)/dx)
  j = round((lat-28)/dy)
  pixel = [[i-4,j+4],[i-3,j+4],[i-2,j+4],[i-1,j+4],[i,j+4],[i+1,j+4],[i+2,j+4],[i+3,j+4],[i+4,j+4],
[i-4,j+3],[i-3,j+3],[i-2,j+3],[i-1,j+3],[i,j+3],[i+1,j+3],[i+2,j+3],[i+3,j+3],[i+4,j+3],
[i-4,j+2],[i-3,j+2],[i-2,j+2],[i-1,j+2],[i,j+2],[i+1,j+2],[i+2,j+2],[i+3,j+2],[i+4,j+2],
[i-4,j+1],[i-3,j+1],[i-2,j+1],[i-1,j+1],[i,j+1],[i+1,j+1],[i+2,j+1],[i+3,j+1],[i+4,j+1],
[i-4,j],[i-3,j],[i-2,j],[i-1,j],[i,j],[i+1,j],[i+2,j],[i+3,j],[i+4,j],
[i-4,j-1],[i-3,j-1],[i-2,j-1],[i-1,j-1],[i,j-1],[i+1,j-1],[i+2,j-1],[i+3,j-1],[i+4,j-1],
[i-4,j-2],[i-3,j-2],[i-2,j-2],[i-1,j-2],[i,j-2],[i+1,j-2],[i+2,j-2],[i+3,j-2],[i+4,j-2],
[i-4,j-3],[i-3,j-3],[i-2,j-3],[i-1,j-3],[i,j-3],[i+1,j-3],[i+2,j-3],[i+3,j-3],[i+4,j-3],
[i-4,j-4],[i-3,j-4],[i-3,j-4],[i-1,j-4],[i,j-4],[i+1,j-4],[i+2,j-4],[i+3,j-4],[i+4,j-4]]
  for item in pixel:
   x = item[0]
   y = item[1]
   try:
    out3.append(ret_val3(x,y))
   except (TimeoutError) as error:
    out3.append(ret_val3(x,y))
   except (HTTPError, URLError) as error:
    out3.append(ret_val3(x,y))
  #print(out3)
  val = ','.join(str(x) for x in out3)
  fl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
  count+=1
  print(count)
 else:
  out4 = []
  i = round((lon-60)/dx)
  j = round((lat-20)/dy)
  pixel = [[i-4,j+4],[i-3,j+4],[i-2,j+4],[i-1,j+4],[i,j+4],[i+1,j+4],[i+2,j+4],[i+3,j+4],[i+4,j+4],
[i-4,j+3],[i-3,j+3],[i-2,j+3],[i-1,j+3],[i,j+3],[i+1,j+3],[i+2,j+3],[i+3,j+3],[i+4,j+3],
[i-4,j+2],[i-3,j+2],[i-2,j+2],[i-1,j+2],[i,j+2],[i+1,j+2],[i+2,j+2],[i+3,j+2],[i+4,j+2],
[i-4,j+1],[i-3,j+1],[i-2,j+1],[i-1,j+1],[i,j+1],[i+1,j+1],[i+2,j+1],[i+3,j+1],[i+4,j+1],
[i-4,j],[i-3,j],[i-2,j],[i-1,j],[i,j],[i+1,j],[i+2,j],[i+3,j],[i+4,j],
[i-4,j-1],[i-3,j-1],[i-2,j-1],[i-1,j-1],[i,j-1],[i+1,j-1],[i+2,j-1],[i+3,j-1],[i+4,j-1],
[i-4,j-2],[i-3,j-2],[i-2,j-2],[i-1,j-2],[i,j-2],[i+1,j-2],[i+2,j-2],[i+3,j-2],[i+4,j-2],
[i-4,j-3],[i-3,j-3],[i-2,j-3],[i-1,j-3],[i,j-3],[i+1,j-3],[i+2,j-3],[i+3,j-3],[i+4,j-3],
[i-4,j-4],[i-3,j-4],[i-3,j-4],[i-1,j-4],[i,j-4],[i+1,j-4],[i+2,j-4],[i+3,j-4],[i+4,j-4]]
  for item in pixel:
   x = item[0]
   y = item[1]
   try:
    out4.append(ret_val4(x,y))
   except (TimeoutError) as error:
    out4.append(ret_val4(x,y))
   except (HTTPError, URLError) as error:
    out4.append(ret_val4(x,y))
  #print(out4)
  val = ','.join(str(x) for x in out4)
  fl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
  count+=1
  print(count)
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)

