import pandas as pd
import numpy as np
from osgeo import osr,gdal
import struct
from gdalconst import *
def latLonToPixel(geotifAddr, latLonPairs):
	# Load the image dataset
	ds = gdal.Open(geotifAddr)
	# Get a geo-transform of the dataset
	gt = ds.GetGeoTransform()
	# Create a spatial reference object for the dataset
	srs = osr.SpatialReference()
	srs.ImportFromWkt(ds.GetProjection())
	# Set up the coordinate transformation object
	srsLatLong = srs.CloneGeogCS()
	ct = osr.CoordinateTransformation(srsLatLong,srs)
	# Go through all the point pairs and translate them to latitude/longitude pairings
	pixelPairs = []
	for point in latLonPairs:
		# Change the point locations into the GeoTransform space
		(point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
		# Translate the x and y coordinates into pixel values
		x = (point[1]-gt[0])/gt[1]
		y = (point[0]-gt[3])/gt[5]
		# Add the point to our return array
                band = ds.GetRasterBand(1)                   
                pix = band.ReadRaster(int(x),int(y), 1,1,1, 1, band.DataType)
                val = struct.unpack('B', pix)
		pixelPairs.append(val[0])
	return pixelPairs
dx = 0.046207358
dy = 0.046207358
#date = raw_input('Input date(2018-05-29)?')
#gl = open('monsoon'+'/'+date+'.csv','w')
dat = pd.read_csv("rflatlong.csv")
for index,row in dat.iterrows():
 if row["R2"] > 0.0:
  print latLonToPixel('/home/dulal/imgproc/insatin/3DIMG_05JUN2018_0300_L1C_ASIA_MER_IR1_modified.tif',[[row["LAT"]-4*dy,row["LON"]-4*dx],[row["LAT"]-4*dy,row["LON"]-3*dx],[row["LAT"]-4*dy,row["LON"]-2*dx],[row["LAT"]-4*dy,row["LON"]-dx],[row["LAT"]-4*dy,row["LON"]],[row["LAT"]-4*dy,row["LON"]+dx],[row["LAT"]-4*dy,row["LON"]+2*dx],[row["LAT"]-4*dy,row["LON"]+3*dx],[row["LAT"]-4*dy,row["LON"]+4*dx],
[row["LAT"]-3*dy,row["LON"]-4*dx],[row["LAT"]-3*dy,row["LON"]-3*dx],[row["LAT"]-3*dy,row["LON"]-2*dx],[row["LAT"]-3*dy,row["LON"]-dx],[row["LAT"]-3*dy,row["LON"]],[row["LAT"]-3*dy,row["LON"]+dx],[row["LAT"]-3*dy,row["LON"]+2*dx],[row["LAT"]-3*dy,row["LON"]+3*dx],[row["LAT"]-3*dy,row["LON"]+4*dx],
[row["LAT"]-2*dy,row["LON"]-4*dx],[row["LAT"]-2*dy,row["LON"]-3*dx],[row["LAT"]-2*dy,row["LON"]-2*dx],[row["LAT"]-2*dy,row["LON"]-dx],[row["LAT"]-2*dy,row["LON"]],[row["LAT"]-2*dy,row["LON"]+dx],[row["LAT"]-2*dy,row["LON"]+2*dx],[row["LAT"]-2*dy,row["LON"]+3*dx],[row["LAT"]-2*dy,row["LON"]+4*dx],
[row["LAT"]-dy,row["LON"]-4*dx],[row["LAT"]-dy,row["LON"]-3*dx],[row["LAT"]-dy,row["LON"]-2*dx],[row["LAT"]-dy,row["LON"]-dx],[row["LAT"]-dy,row["LON"]],[row["LAT"]-dy,row["LON"]+dx],[row["LAT"]-dy,row["LON"]+2*dx],[row["LAT"]-dy,row["LON"]+3*dx],[row["LAT"]-dy,row["LON"]+4*dx],
[row["LAT"],row["LON"]-4*dx],[row["LAT"],row["LON"]-3*dx],[row["LAT"],row["LON"]-2*dx],[row["LAT"],row["LON"]-dx],[row["LAT"],row["LON"]],[row["LAT"],row["LON"]+dx],[row["LAT"],row["LON"]+2*dx],[row["LAT"],row["LON"]+3*dx],[row["LAT"],row["LON"]+4*dx],
[row["LAT"]+dy,row["LON"]-4*dx],[row["LAT"]+dy,row["LON"]-3*dx],[row["LAT"]+dy,row["LON"]-2*dx],[row["LAT"]+dy,row["LON"]-dx],[row["LAT"]+dy,row["LON"]],[row["LAT"]+dy,row["LON"]+dx],[row["LAT"]+dy,row["LON"]+2*dx],[row["LAT"]+dy,row["LON"]+3*dx],[row["LAT"]+dy,row["LON"]+4*dx],
[row["LAT"]+2*dy,row["LON"]-4*dx],[row["LAT"]+2*dy,row["LON"]-3*dx],[row["LAT"]+2*dy,row["LON"]-2*dx],[row["LAT"]+2*dy,row["LON"]-dx],[row["LAT"]+2*dy,row["LON"]],[row["LAT"]+2*dy,row["LON"]+dx],[row["LAT"]+2*dy,row["LON"]+2*dx],[row["LAT"]+2*dy,row["LON"]+3*dx],[row["LAT"]+2*dy,row["LON"]+4*dx],
[row["LAT"]+3*dy,row["LON"]-4*dx],[row["LAT"]+3*dy,row["LON"]-3*dx],[row["LAT"]+3*dy,row["LON"]-2*dx],[row["LAT"]+3*dy,row["LON"]-dx],[row["LAT"]+3*dy,row["LON"]],[row["LAT"]+3*dy,row["LON"]+dx],[row["LAT"]+3*dy,row["LON"]+2*dx],[row["LAT"]+3*dy,row["LON"]+3*dx],[row["LAT"]+3*dy,row["LON"]+4*dx],
[row["LAT"]+4*dy,row["LON"]-4*dx],[row["LAT"]+4*dy,row["LON"]-3*dx],[row["LAT"]+4*dy,row["LON"]-2*dx],[row["LAT"]+4*dy,row["LON"]-dx],[row["LAT"]+4*dy,row["LON"]],[row["LAT"]+4*dy,row["LON"]+dx],[row["LAT"]+4*dy,row["LON"]+2*dx],[row["LAT"]+4*dy,row["LON"]+3*dx],[row["LAT"]+4*dy,row["LON"]+4*dx]
]),row["STATION"],row["R2"],row["LAT"],row["LON"]

