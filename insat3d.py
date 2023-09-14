from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from numpy import *
import scipy
#import csv
#import pandas
import math
import urllib2
from bs4 import BeautifulSoup
names = ''
lat = 0.0
lon = 0.0
x=0
y=0
def lat_long_to_pixel_3d(lon, lat):
 global x, y
 if lon >= 50 and lon < 60 and lat >= 40:
   x = ((lon - 50) / 0.0485) + 114
   y = 313 + ((lat-40)/0.0396)
 elif lon >= 50 and lon < 60 and lat >= 30 and lat < 40:
   x = ((lon - 50) / 0.0485) + 114
   y = 313 + ((40 - lat) / 0.0396) 
 elif lon >= 50 and lon < 60 and lat >= 20 and lat < 30:
   x = ((lon - 50) / 0.0485) + 114
   y = 565 + ((30 - lat) / 0.0438) 
 elif lon >= 50 and lon < 60 and lat >= 10 and lat < 20:
   x = ((lon - 50) / 0.0485) + 114
   y = 793 + ((20 - lat) / 0.0467) 
 elif lon >= 50 and lon < 60 and lat >= 0 and lat < 10:
   x = ((lon - 50) / 0.0485) + 114
   y = 1007 + ((10 - lat) / 0.0483) 
 elif lon >= 50 and lon < 60 and lat < 0:
   x = ((lon - 50) / 0.0485) + 114
   y = ((0 - lat) / 0.0483) + 1214
 elif lon >= 60 and lon < 70 and lat >= 40:
   x = ((lon - 60) / 0.0485) + 320
   y = 313 + ((lat-40)/0.0396)
 elif lon >= 60 and lon < 70 and lat >= 30 and lat < 40:
   x = ((lon - 60) / 0.0485) + 320
   y = 313 + ((40 - lat) / 0.0396) 
 elif lon >= 60 and lon < 70 and lat >= 20 and lat < 30:
   x = ((lon - 60) / 0.0485) + 320
   y = 565 + ((30 - lat) / 0.0438) 
 elif lon >= 60 and lon < 70 and lat >= 10 and lat < 20:
   x = ((lon - 60) / 0.0485) + 320
   y = 793 + ((20 - lat) / 0.0467) 
 elif lon >= 60 and lon < 70 and lat >= 0 and lat < 10:
   x = ((lon - 60) / 0.0485) + 320
   y = 1007 + ((10 - lat) / 0.0483) 
 elif lon >= 60 and lon < 70 and lat < 0:
   x = ((lon - 60) / 0.0485) + 320
   y = ((0 - lat) / 0.0483) + 1214
 elif lon >= 70 and lon < 80 and lat >= 40:
   x = ((lon - 70) / 0.0485) + 526
   y = 313 + ((lat-40)/0.0396)
 elif lon >= 70 and lon < 80 and lat >= 30 and lat < 40:
   x = ((lon - 70) / 0.0485) + 526
   y = 313 + ((40 - lat) / 0.0396) 
 elif lon >= 70 and lon < 80 and lat >= 20 and lat < 30:
   x = ((lon - 70) / 0.0485) + 526
   y = 565 + ((30 - lat) / 0.0438) 
 elif lon >= 70 and lon < 80 and lat >= 10 and lat < 20:
   x = ((lon - 70) / 0.0485) + 526
   y = 793 + ((20 - lat) / 0.0467) 
 elif lon >= 70 and lon < 80 and lat >= 0 and lat < 10:
   x = ((lon - 70) / 0.0485) + 526
   y = 1007 + ((10 - lat) / 0.0483) 
 elif lon >= 70 and lon < 80 and lat < 0:
   x = ((lon - 70) / 0.0485) + 526
   y = ((0 - lat) / 0.0483) + 1214
 elif lon >= 80 and lon < 90 and lat >= 40:
   x = ((lon - 80) / 0.0485) + 733
   y = 313 + ((lat-40)/0.0396)
 elif lon >= 80 and lon < 90 and lat >= 30 and lat < 40:
   x = ((lon - 80) / 0.0485) + 733
   y = 313 + ((40 - lat) / 0.0396)
 elif lon >= 80 and lon < 90 and lat >= 20 and lat < 30:
   x = ((lon - 80) / 0.0485) + 733
   y = 565 + ((30 - lat) / 0.0438) 
 elif lon >= 80 and lon < 90 and lat >= 10 and lat < 20:
   x = ((lon - 80) / 0.0485) + 733
   y = 793 + ((20 - lat) / 0.0467) 
 elif lon >= 80 and lon < 90 and lat >= 0 and lat < 10:
   x = ((lon - 80) / 0.0485) + 733
   y = 1007 + ((10 - lat) / 0.0483) 
 elif lon >= 80 and lon < 90 and lat < 0:
   x = ((lon - 80) / 0.0485) + 733
   y = ((0 - lat) / 0.0483) + 1214
 elif lon >= 90 and lon < 100 and lat >= 40:
   x = ((lon - 90) / 0.0485) + 939
   y = 313 + ((lat-40)/0.0396)
 elif lon >= 90 and lon < 100 and lat >= 30 and lat < 40:
   x = ((lon - 70) / 0.0485) + 939
   y = 313 + ((40 - lat) / 0.0396) 
 elif lon >= 90 and lon < 100 and lat >= 20 and lat < 30:
   x = ((lon - 90) / 0.0485) + 939
   y = 565 + ((30 - lat) / 0.0438) 
 elif lon >= 90 and lon < 100 and lat >= 10 and lat < 20:
   x = ((lon - 90) / 0.0485) + 939
   y = 793 + ((20 - lat) / 0.0467) 
 elif lon >= 90 and lon < 100 and lat >= 0 and lat < 10:
   x = ((lon - 70) / 0.0485) + 939
   y = 1007 + ((10 - lat) / 0.0483) 
 elif lon >= 90 and lon < 100 and lat < 0:
   x = ((lon - 90) / 0.0485) + 939
   y = ((0 - lat) / 0.0483) + 1214
 elif lon >= 100 and lat >= 40:
   x = ((lon - 100) / 0.0485) + 1145
   y =   313 + ((lat-40)/0.0396)
 elif lon >= 100 and lat >= 30 and lat < 40:
   x = ((lon - 100) / 0.0485) + 1145
   y = 313 + ((40 - lat) / 0.0396) 
 elif lon >= 100 and lat >= 20 and lat < 30:
   x = ((lon - 100) / 0.0485) + 1145
   y = 565 + ((30 - lat) / 0.0438) 
 elif lon >= 100 and lat >= 10 and lat < 20:
   x = ((lon - 100) / 0.0485) + 1145
   y = 793 + ((20 - lat) / 0.0467) 
 elif lon >= 100 and lat >= 0 and lat < 10:
   x = ((lon - 100) / 0.0485) + 1145
   y = 1007 + ((10 - lat) / 0.0483) 
 elif lon >= 100 and lat < 0:
   x = ((lon - 100) / 0.0485) + 1145
   y = ((0 - lat) / 0.0483) + 1214
 return int(x), int(y)
#colnames = ['time', 'station', 'latitude', 'longitude', 'rainfall']
#data = pandas.read_csv('/home/dulal/insat3d/0512/00.csv', names=colnames)
#names = list(data.station)
#lat = list(data.latitude)
#lon = list(data.longitude)
im1 = Image.open('3Dasiasec_ir1.jpg').convert('L')
im = array(im1)
im = 1*(im<128)
labels, nbr_objects = scipy.ndimage.measurements.label(im)
print "Number of objects:", nbr_objects
scipy.misc.imsave(im1, im)
#rows = im.shape[0]
#for row in range(rows):
# print im[row,:]
draw = ImageDraw.Draw(im1)
#for i in range(len(lon)):
f = urllib2.urlopen("http://www.imdaws.com/WeatherARGData.aspx?&FromDate=17/12/2014&ToDate=17/12/2014&Time=00")
html = f.read()
soup = BeautifulSoup(''.join(html))
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows[2:]:
  cols = tr.findAll('td')
  i = 0
  for td in cols:
      text= td.get_text()
      if i == 1:
       names = text
       i += 1
      elif i == 4:
       lat = float(text)
       i += 1
      elif i == 5:
       lon = float(text)
       i += 1
      elif i == 6:
       rf = text
       i += 1
      else:
       i += 1
#  print
  i = 0 
  if rf.isdigit():
   if int(rf) != 0:
#    draw.ellipse((lat_long_to_pixel_3d(lon,lat)[0]-1, lat_long_to_pixel_3d(lon, lat)[1]-1,
#                lat_long_to_pixel_3d(lon,lat)[0]+1, lat_long_to_pixel_3d(lon, lat)[1]+1),
#                fill="white")
#  print lon[i], lat[i], names[i]
    draw.text((lat_long_to_pixel_3d(lon,lat)[0], lat_long_to_pixel_3d(lon,lat)[1]),rf,fill='white')
im1.save("test.jpg")
