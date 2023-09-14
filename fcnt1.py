import urllib.request
import time
from urllib.error import HTTPError,URLError
from socket import timeout
i=100
j=200
f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetFeatureInfo&version=1.3.0&CRS=CRS:84&BBOX=60,0,100,16&I="+str(i)+"&J="+str(j)+"&TIME=2021-10-25T03:15:00&INFO_FORMAT=text/xml&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=1282&HEIGHT=358",timeout=None)
txt1 = f1.read().decode('utf-8')
f1.close()
val_ = txt1.split('<value>')
val = val_[1].split('</value>')
print(val[0])

  
