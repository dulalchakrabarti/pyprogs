"""
Read LAI data from h5 files with following tile details
24 05 60/40,70/30
24 06 60/30,70/20
24 07 60/20,70/10
25 05 70/40,80/30
25 06 70/30,80/20
25 07 70/20,80/10
25 08 70/10,80/0
26 05 80/40,90/30
26 06 80/30,90/20
26 07 80/20,90/10
26 08 90/10,90/0
27 06 90/30,100/20
27 07 90/20,100/10
valid range - 0:100, fill value-249:255, scale factor-0.1

import os
import numpy as np
import pandas as pd
"""
import glob
import h5py

def select_tile(lat,lon):
    """
    lat - float
    lon - float
    returns string tile
    """
    if lon > 60 and lon < 70:
     if lat > 30 and lat < 40:
      return 'h24v05'
     elif lat > 20 and lat < 30:
      return 'h24v06'
     elif lat > 10 and lat < 20:
      return 'h24v07'
    elif lon > 70 and lon < 80:
     if lat > 30 and lat < 40:
      return 'h25v05'
     elif lat > 20 and lat < 30:
      return 'h25v06'
     elif lat > 10 and lat < 20:
      return 'h25v07'
     elif lat > 0 and lat < 10:
      return 'h25v08'
    elif lon > 80 and lon < 90:
     if lat > 30 and lat < 40:
      return 'h26v05'
     elif lat > 20 and lat < 30:
      return 'h26v06'
     elif lat > 10 and lat < 20:
      return 'h26v07'
     elif lat > 0 and lat < 10:
      return 'h26v08'
    elif lon > 90 and lon < 100:
     if lat > 20 and lat < 30:
      return 'h27v06'
     elif lat > 10 and lat < 20:
      return 'h27v07'
def get_all(name):
    """
    appends sub file names in an empty list dl
    """
    dl.append(name)
def read_lat_lon():
    lines = [line.rstrip('\n') for line in open('wheat_lat_lon.csv')]
    return lines
def get_data(lat,lon):
    """
    selects specified tile and retrieves prior,current and next pixel value
    """
    lat = lat
    lon = lon
    dlat = 10.0/2400
    dlon = 10.0/2400
    for item in glob.glob('VNP15A2H*.h5'):
     if item[18:24] == select_tile(lat,lon):
      f = h5py.File(item,'r')
      f.visit(get_all)
      name = dl[-4]
      data = f[name]
      word = item.split('.')
      lon_ = int(word[2][1:3])
      lat_ = int(word[2][4:])
      lonc = lon_*10 - 180
      latc = 90 -lat_*10
      row_ = (latc-lat)/dlat
      col_ = (lon-lonc)/dlon
      row_ = int(row_)
      col_ = int(col_)
      return (data[row_-1][col_-1],data[row_][col_],data[row_+1][col_+1])
# main program calling the methods
fl = open('lai.csv','w')
fl.write('lat'+','+'lon'+','+'px-1'+','+'px'+','+'px+1'+'\n')
latlon = read_lat_lon()
for item in latlon:
 item =  item.split(',')
 if item[0][1].isdigit():
  lat = float(item[0])
  lon = float(item[1])
  dl = []
  (px1,px2,px3) = get_data(lat,lon)
  fl.write(item[0]+','+item[1]+','+str(px1)+','+str(px2)+','+str(px3)+'\n')



