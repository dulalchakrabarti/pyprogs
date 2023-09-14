import urllib2
import re
from time import sleep

def get_indices(stn,year,mon,dttm,pl):
    '''
    '''
    data =''
    ua = {'Stationidentifier':'99999','Stationnumber':'99999','Observationtime':'99999','Stationlatitude':'99999','Stationlongitude':'99999',
'Stationelevation':'99999','Showalterindex':'99999','Liftedindex':'99999','LIFTcomputedusingvirtualtemperature':'99999','SWEATindex':'99999',
'Kindex':'99999','Crosstotalsindex':'99999','Verticaltotalsindex':'99999','Totalstotalsindex':'99999',
'ConvectiveAvailablePotentialEnergy':'99999','CAPEusingvirtualtemperature':'99999','ConvectiveInhibition':'99999',
'CINSusingvirtualtemperature':'99999','BulkRichardsonNumber':'99999','BulkRichardsonNumberusingCAPV':'99999',
'Temp[K]oftheLiftedCondensationLevel':'99999','Pres[hPa]oftheLiftedCondensationLevel':'99999',
'Meanmixedlayerpotentialtemperature':'99999','Meanmixedlayermixingratio':'99999','1000hPato500hPathickness':'99999',
'Precipitablewater[mm]forentiresounding':'99999'}
    try:
     f1 = urllib2.urlopen("http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ALIST&YEAR="+year+"&MONTH="+mon+"&FROM="+dttm+"&TO="+dttm+"&STNM="+stn)
    except:
     sleep(10)
     f1 = urllib2.urlopen("http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ALIST&YEAR="+year+"&MONTH="+mon+"&FROM="+dttm+"&TO="+dttm+"&STNM="+stn)
    txt1 = f1.read()
    temp = txt1.split('PRE')
    if len(temp) == 6:
     idx = temp[-2]
     idx = idx[1:-2]
     idx = idx.split('\n')
     txt_ = [x.replace(' ','') for x in idx]
     txt = [ x for x in txt_ if x != '']
     txt1 = [x.split(':') for x in txt]
     for y in txt1:
      ua[y[0]] = y[1]
     data = ua['Stationlatitude']+','+ua['Stationlongitude']+','+ua['Showalterindex']+','+ua['Liftedindex']+','+ua['LIFTcomputedusingvirtualtemperature']+','+ua['SWEATindex']+','+ua['Kindex']+','+ua['Crosstotalsindex']+','+ua['Verticaltotalsindex']+','+ua['Totalstotalsindex']+','+ua['ConvectiveAvailablePotentialEnergy']+','+ua['CAPEusingvirtualtemperature']+','+ua['ConvectiveInhibition']+','+ua['CINSusingvirtualtemperature']+','+ua['BulkRichardsonNumber']+','+ua['BulkRichardsonNumberusingCAPV']+','+ua['Temp[K]oftheLiftedCondensationLevel']+','+ua['Pres[hPa]oftheLiftedCondensationLevel']+','+ua['Meanmixedlayerpotentialtemperature']+','+ua['Meanmixedlayermixingratio']+','+ua['1000hPato500hPathickness']+','+ua['Precipitablewater[mm]forentiresounding']
    print 'processed',stn,year,mon,dttm,pl
    return data
fl = open('idx.csv','w')
fl.write('lat'+','+'lon'+','+'Shlt'+','+'Lift'+','+'Liftv'+','+'SWEAT'+','+'K'+','+'Cross'+','+
'Vert'+','+'Total'+','+'CAPE'+','+'CAPEv'+','+'CIN'+','+'CINv'+','+'BulkR'+','+'BulkRv'+','+
'TempLFCT'+','+'PresLFCT'+','+'Meanpottemp'+','+'MeanMixrat'+','+'Thick'+','+'Prec'+','+'year'+','+'mon'+','+'dttm'+','+'pl'+'\n')
stns = ['42182', '42314', '42339', '42361', '42369', '42379', '42410', '42647', '42667', '42809', '42867', '42971', '43003', '43041', '43128', '43185', '43192', '43279', '43295', '43353', '43369', '43371']
lines = [line.rstrip('\n') for line in open('tsdata.csv')]
for line in lines:
 line = line.split(',')
 pl = line[0]
 yr = line[3][:4]
 mon = line[3][4:6]
 date = line[3][6:8]
 dttm = date+'00'
 for stn in stns:
  line = get_indices(stn,yr,mon,dttm,pl)
  fl.write(line+','+yr+','+mon+','+dttm+','+pl+'\n')
