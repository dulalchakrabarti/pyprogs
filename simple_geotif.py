from osgeo import gdal
import numpy as np

#geotransform[0] = top left x
#geotransform[1] = w-e pixel resolution
#geotransform[2] = 0
#geotransform[3] = top left y
#geotransform[4] = 0
#geotransform[5] = n-s pixel resolution (negative value)
# Read the input raster into a Numpy array
infile = "insatir1_modified.tif"
data   = gdal.Open(infile)
arr    = data.ReadAsArray()
print arr[2]
# Do some processing....

# Save out to a GeoTiff
print arr.shape
# First of all, gather some information from the original file
[chan,cols,rows] = arr.shape
print data.GetMetadata()
print data.RasterCount
trans       = data.GetGeoTransform()
print trans
proj        = data.GetProjection()
print proj
nodatav     = 0.0#data.GetRasterBand(1).GetNoDataValue()
outfile     = "outputfile.tif"

# Create the file, using the information from the original file
outdriver = gdal.GetDriverByName("GTiff")
outdata   = outdriver.Create(str(outfile), rows, cols, 1, gdal.GDT_Float32)

# Write the array to the file, which is the original array in this example
outdata.GetRasterBand(1).WriteArray(arr[0])

# Set a no data value if required
outdata.GetRasterBand(1).SetNoDataValue(nodatav)

# Georeference the image
outdata.SetGeoTransform(trans)

# Write projection information
outdata.SetProjection(proj)


