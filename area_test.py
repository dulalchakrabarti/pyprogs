import http
import numpy as np
import time
import requests
import json
try:
 txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX=58.7294921875,18.517578125,90.5458984375,44.357421875&I=362&J=294&TIME=2022-02-28T07:45:00.000Z/2022-03-07T07:15:00.000Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_TIR1&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=724&HEIGHT=588"#40.17,60.29
 
 r1 = requests.get(txt)
 resp = r1.text
 print(resp)
 data = json.loads(resp)
 print(data)
except requests.exceptions.ConnectionError:
 print('Timed out!!')
