#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib3 import PoolManager
import json

d = {'api_key': '9394be6908a5b377',
     'state_code': 'IL',
     'personal_weather_station': 'pws:KILMORRI2'}
pm = PoolManager()
r = pm.request('GET', 'http://api.wunderground.com/api/' +
               d['api_key'] + '/conditions/q/' + d['state_code'] +
               '/' + d['personal_weather_station'] + '.json')
co = json.loads(r.data.decode('utf-8'))['current_observation']

print("\n\033[1;36mWeather: Current\033[0;0m (Weather Underground)\n",
      "* Station: {}\n".format(
        co['observation_location']['full']),
      "* {}\n\n".format(
        co['observation_time']),
      "* \033[1;34mWeather condition\033[0;0m: {}\n".format(
        co['weather']),
      "* \033[1;34mTemperature\033[0;0m: {}\n".format(
        co['temperature_string']),
      "* \033[1;34mFeels like\033[0;0m: {}\n\n".format(
        co['feelslike_string']),
      "* \033[1;34mHumidity\033[0;0m: {}\n".format(
        co['relative_humidity']),
      "* \033[1;34mDewpoint\033[0;0m: {}\n".format(
        co['dewpoint_string']),
      "* \033[1;34mWind\033[0;0m: {}\n".format(
        co['wind_string']),
      "* \033[1;34mWindchill\033[0;0m: {}\n".format(
        co['windchill_string']),
      "* \033[1;34mHeat index\033[0;0m: {} HI (±1.3 F)\n".format(
        co['heat_index_string']),
      "* \033[1;34mSolar radiation\033[0;0m: {} SI\n".format(
        co['solarradiation']),
      "* \033[1;34mUltraviolet\033[0;0m: {} UV\n".format(
        co['UV']),
      "* \033[1;34mVisibility\033[0;0m: {} mi.\n".format(
        co['visibility_mi']),
      "* \033[1;34mPrecipitation 1hr\033[0;0m: {}\n".format(
        co['precip_1hr_string']),
      "* \033[1;34mPrecipitation today\033[0;0m: {}\n".format(
        co['precip_today_string']),
      '* \033[1;34mAtmospheric pressure\033[0;0m: {}{} inHg\n'.format(
        co['pressure_in'],
        co['pressure_trend']),
      "* \033[1;34mSoil temperature\033[0;0m: {} F".format(
        co['soil_temp_f']))
try:
    print(" * \033[1;34mLeaf wetness\033[0;0m: {} (0–15)\n".format(co['leaf_wetness']))
except KeyError:
    pass

r.close()
