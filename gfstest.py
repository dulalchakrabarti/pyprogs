import urllib2
import math
import matplotlib.pyplot as plt
import numpy as np
sd = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20201104/gfs_0p25_1hr_00z.ascii?sunsdsfc[0:120][360:520][240:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 print item
