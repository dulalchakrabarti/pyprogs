import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from datetime import *
def ist(time):
    '''
    '''
    offset = 5
    ist = time+offset
    if ist > 24:
     ist = ist - 24
    if len(str(ist)) == 1:
     ist = '0'+str(ist)
    else:
     ist = str(ist)
    ist = ist+':30'
    return ist

def conv_date(date):
    out_date = date
    return out_date
latlon = '480300'
df = pd.read_csv(latlon+'.csv')
dfg = df.transpose()
mydf = {}
for k,row in dfg.iterrows():
 mydf[k] = row.tolist()
dfnew = pd.DataFrame(mydf)
dfg = dfnew.groupby('date')
date=''
fl = open(latlon,'w')
for item in dfg:
 if str(item[0]) != date:
  date= str(item[0])
  print 'Date'+','+','+','+conv_date(date)+','+','+','+','
  fl.write('Date'+','+','+conv_date(date)+','+','+','+','+','+'\n')
 line = item[1]['time'].tolist()
 line = ','.join([ist(x) for x in line])
 print 'Time(IST)'+','+line
 fl.write('Time(IST)'+','+line+'\n')
 line = item[1]['wind'].tolist()
 line = ','.join([str(round(x,1)) for x in line])
 print 'Windspeed(m/s)'+','+line
 fl.write('Windspeed(m/s)'+','+line+'\n')
 line = item[1]['wd'].tolist()
 line=','.join([str(x) for x in line])
 print 'Winddir'+','+line
 fl.write('Winddir'+','+line+'\n')
 line = item[1]['gust'].tolist()
 line = ','.join([str(round(x,1)) for x in line])
 print 'Gust(m/s)'+','+line
 fl.write('Gust(m/s)'+','+line+'\n')
 rain = float(max(item[1]['rain'].tolist()))
 tempmax = max(item[1]['temp'].tolist())
 tempmin = min(item[1]['temp'].tolist())
 sky = max(item[1]['cloud'].tolist())
 print 'Weather'+','+'Rain(mm)/ltng: '+str(round(rain,1))+','+'Max Temp(C): '+str(round(tempmax,1))+','+'Min Temp(C): '+str(round(tempmin,1))+','+'Max cloud(%):'+str(sky)+'\n'
 fl.write('Weather'+','+'Rain(mm)/ltng:'+','+str(round(rain,1))+','+'MaxTemp(C): '+','+str(round(tempmax,1))+','+'MinTemp(C): '+','+str(round(tempmin,1))+','+'Maxcloud(%):'+','+str(sky)+'\n')
fl.close()

