import urllib.request
stn = {}
beg = ''
end = ''
lst = ''
dt = []
beg = input('Enter start datetime(201807090300):')
end = input('Enter end datetime(201807090359):')
txt_beg = ''
fa = open("india_station.csv")
tmp = [line.strip() for line in fa.readlines()]
for item in tmp:
 lst = item.split(',')
 stn[int(lst[0])] = lst[1:]
#fl = open("sql_syn.txt",'w+') 
f1 = urllib.request.urlopen("https://www.ogimet.com/cgi-bin/getsynop?begin="+beg+"&end="+end+"&block=42")
txt1 = f1.read()
syn = txt1.split(b'\n')
for item in syn:
 item = item.decode('utf-8')
 buf = item.split(',')
 b = buf[-1].split(' ')
 if len(b) > 5 and int(b[2]) in stn:
  for itm in stn[int(b[2])]:
   b.append(itm)
  z1 = ' '.join(x for x in b[-3:])
  z2 = ' '.join(x for x in b[:-3])
  z = z1+' '+z2
  #fl.write(z+'\n')
  txt_beg+=z+'\n'
f2 = urllib.request.urlopen("https://www.ogimet.com/cgi-bin/getsynop?begin="+beg+"&end="+end+"&block=43")
txt1 = f2.read()
syn = txt1.split(b'\n')
for item in syn:
 item = item.decode('utf-8')
 buf = item.split(',')
 b = buf[-1].split(' ')
 if len(b) > 5 and int(b[2]) in stn:
  for itm in stn[int(b[2])]:
   b.append(itm)
  z1 = ' '.join(x for x in b[-3:])
  z2 = ' '.join(x for x in b[:-3])
  z = z1+' '+z2
  #fl.write(z+'\n')
  txt_beg+=z+'\n'
#fl.close()
txt_beg = txt_beg.rstrip()
rep = txt_beg.split('\n')
from getpass import getpass
from mysql.connector import connect, Error
from pymetdecoder import synop as s
for itm in rep:
 itm = itm.split(' ')
 #print(itm)
 syn = itm[3:]
 synop = ' '.join(x for x in syn)
 #print(synop)
 output = s.SYNOP().decode(synop)
 #print(output)
 dt.append(output)
print(len(dt))
#['dateX', 'Gmt', 'StationId', 'Latitude', 'Longitude', 'ElevationHeight', 'CountryId', 'StationName', 'CloudBase', 'HorizontalVisibility', 'CloudCover', 'WindDirection', 'WindSpeed', 'AirTemp', 'DewPointTemp', 'StationPressure', 'SealevelPressure', 'PressureChangeLastThreeHours', 'RainGFirst', 'PresentWeather', 'PastWeather', 'LowCloud', 'MiddleCloud', 'HighCloud', 'MaxTemp', 'MinTemp', 'StateOfGroundWithSnowCover', 'PressureChangeLastTwentyFourHours', 'RainGThird', 'CloudCoverageOfLayer', 'GenusOfCloud', 'HeightOfCloudBase', 'AmountOfLowCloud', 'Rawdata', 'lat', 'lon']
#{'station_type': {'value': 'AAXX'}, 'obs_time': {'day': {'value': 21}, 'hour': {'value': 3}}, 'wind_indicator': {'value': 4, 'unit': 'KT', 'estimated': False}, 'station_id': {'value': '42468'}, 'region': {'value': 'II'}, 'precipitation_indicator': {'value': 3, 'in_group_1': False, 'in_group_3': False}, 'weather_indicator': {'value': 2, 'automatic': False}, 'lowest_cloud_base': {'_table': '1600', 'min': 2500, 'max': None, 'quantifier': 'isGreaterOrEqual', '_code': 9, 'unit': 'm'}, 'visibility': {'_table': '4377', 'value': 4000, 'quantifier': None, 'use90': True, '_code': 96, 'unit': 'm'}, 'cloud_cover': {'_table': '2700', 'value': 0, 'obscured': False, 'unit': 'okta', '_code': 0}, 'surface_wind': {'direction': {'_table': '0877', 'value': 360, 'varAllUnknown': False, 'calm': False, '_code': 36, 'unit': 'deg'}, 'speed': {'value': 2, 'unit': 'KT'}}, 'air_temperature': {'value': 11.0, 'unit': 'Cel'}, 'dewpoint_temperature': {'value': 6.8, 'unit': 'Cel'}, 'sea_level_pressure': {'value': 1015.9, 'unit': 'hPa'}, 'maximum_temperature': {'value': 20.0, 'unit': 'Cel'}, 'minimum_temperature': None, 'pressure_change': {'value': 0.2, 'unit': 'hPa'}, 'section5': ['10178=']}

for item in dt:
 dateX = beg[:4]+'-'+beg[4:6]+'-'+beg[6:8]
 Gmt = 0
 StationId = item['station_id']['value']
 Latitude = stn[int(StationId)][1]
 Longitude = stn[int(StationId)][2]
 ElevationHeight = '*'
 CountryId = 'IND'
 StationName = stn[int(StationId)][0]
 if item['lowest_cloud_base'] != None:
  CloudBase = item['lowest_cloud_base']['min']
 else:
  CloudBase = 'None'
 print(item)
 if item['visibility'] == None:
  HorizontalVisibility = 'None'
 else:
  HorizontalVisibility = item['visibility']['value']
 if item['cloud_cover'] == None:
  CloudCover = 'None'
 else:
  CloudCover = item['cloud_cover']['value']
 if item['surface_wind'] == None or item['surface_wind']['direction'] == None:
  WindDirection = None
 elif item['surface_wind']['direction']['value']:
  WindDirection = item['surface_wind']['direction']['value']
 else:
  WindDirection = 'Absent'
 if item['surface_wind'] == None:
  WindSpeed = 'None'
 else:
  WindSpeed = item['surface_wind']['speed']
 AirTemp = item['air_temperature']['value']
 DewPointTemp = item['dewpoint_temperature']['value']
 if 'station_pressure' in item.keys() and item['station_pressure'] != None:
  StationPressure = item['station_pressure']['value']
 else:
  StationPressure = 'Absent'
 if 'sea_level_pressure' in item.keys():
  if item['sea_level_pressure'] == None:
   SealevelPressure = 'None'
  else:
   SealevelPressure = item['sea_level_pressure']['value']
 else:
  SealevelPressure = ''
 PressureChangeLastThreeHours = '*'
 RainGFirst = item['precipitation_indicator']['value']
 if 'present_weather' in item.keys():
  PresentWeather = item['present_weather']['value']
 else:
  PresentWeather = ''
 if 'past_weather' in item.keys():
  if item['past_weather'][0] == None:
   PastWeather = 'None'
  else:
   PastWeather = item['past_weather'][0]['value']
 else:
  PastWeather = ''
 if 'minimum_temperature' in item.keys() and item['minimum_temperature'] != None:
  MinimumTemperature = item['minimum_temperature']['value']
 else:
  MinimumTemperature = 'Absent'
 if 'maximum_temperature' in item.keys() and item['maximum_temperature'] != None:
  MaximumTemperature = item['maximum_temperature']['value']
 else:
  MaximumTemperature = 'Absent'
 print(dateX,Gmt,StationId,Latitude,Longitude,ElevationHeight,CountryId,StationName,CloudBase,HorizontalVisibility,
 CloudCover,WindDirection,WindSpeed,AirTemp,DewPointTemp,StationPressure,SealevelPressure,PressureChangeLastThreeHours,RainGFirst,
 PresentWeather,PastWeather,MinimumTemperature,MaximumTemperature)
'''
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        use_db_query = "use weather"
        show_table_query = "show tables"
        desc_synopdata_query = "desc synopdata"
        with connection.cursor(buffered = True) as cursor:
            cursor.execute(use_db_query)
            cursor.execute(desc_synopdata_query)
            lst = [column[0] for column in cursor.fetchall()]
            print(lst)
except Error as e:
    print(e)
'''

