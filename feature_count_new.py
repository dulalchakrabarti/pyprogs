import urllib.request
import time
from urllib.error import HTTPError,URLError
#from socket import timeout
fl = open('ftr_ir1.csv','w')
fl.write('lat'+','+'lon'+','+'cls'+','+'cnt'+'\n')
seconds1 = time.time()
def ret_val(i,j,la):
    '''
    '''
    f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetFeatureInfo&version=1.3.0&CRS=CRS:84&BBOX=60,"+str(la-8)+",110,"+str(la+8)+"&I="+str(i)+"&J="+str(j)+"&TIME=2021-10-25T03:15:00&INFO_FORMAT=text/xml&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=1282&HEIGHT=358",timeout=None)
    txt1 = f1.read().decode('utf-8')
    f1.close()
    val_ = txt1.split('<value>')
    val = val_[1].split('</value>')
    val = val[0]
    return(val)
##########
dx =0.03900156
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
 out = []
 i = round((lon-60)/dx)
 j = 179
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
   out.append(ret_val(x,y,lat))
  except (TimeoutError) as error:
   out.append(ret_val(x,y,lat))
  except (HTTPError, URLError) as error:
   out.append(ret_val(x,y,lat))
 val = ','.join(str(x) for x in out)
 fl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
 count+=1
 print(count)
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)

