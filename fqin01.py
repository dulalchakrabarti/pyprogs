import urllib2
import datetime
import math
import numpy as np
from netCDF4 import Dataset
import pandas as pd
def deg_to_dir(deg):
    if deg == 0.0:
     dr = 'N'
    elif deg > 0.0 and deg < 45.0:
     dr = 'NNE'
    elif deg == 45.0:
     dr = 'NE'
    elif deg > 45.0 and deg < 90.0:
     dr = 'ENE'
    elif deg == 90.0:
     dr = 'E'
    elif deg > 90.0 and deg < 135.0:
     dr = 'ESE'
    elif deg == 135.0:
     dr = 'SE'
    elif deg > 135.0 and deg < 180.0:
     dr = 'SSE'
    elif deg == 180.0:
     dr = 'S'
    elif deg > 180.0 and deg < 235.0:
     dr = 'SSW'
    elif deg == 235.0:
     dr = 'SW'
    elif deg > 235.0 and deg < 270.0:
     dr = 'WSW'
    elif deg == 270.0:
     dr = 'W'
    elif deg > 270.0 and deg < 315.0:
     dr = 'WNW'
    elif deg == 315.0:
     dr = 'NW'
    elif deg > 315.0 and deg < 360.0:
     dr = 'NNW'
    return dr
url="ftp://tgftp.nws.noaa.gov/data/raw/fq/fqin01.dems..txt"
page =urllib2.urlopen(url)
data=page.read()
idx1 = data.index("PART:-I")
idx2 = data.index("PART:-II")
idx3 = data.index("ARB A1")
idx4 = data.index("A1-FORECAST FOR 24 HOURS")
idx5 = data.index("A1-FORECAST FOR 48 HOURS")
idx6 = data.index("ARB A2")
print data[idx1:idx2]
print data[idx2:idx3]
print data[idx4:idx5]
print data[idx5:idx6]
