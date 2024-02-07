from siphon.catalog import TDSCatalog
import xarray as xr
import pandas as pd
#date = datetime.utcnow() - timedelta(days=1)
#print(date)
cat = TDSCatalog('https://thredds.ucar.edu/thredds/catalog/grib/NCEP/WW3/Global/catalog.xml')
#print(cat.datasets)
best_WW3 = TDSCatalog('https://thredds.ucar.edu/thredds/catalog/grib/NCEP/WW3/Global/catalog.xml?dataset=grib/NCEP/WW3/Global/Best')
best_ds = list(best_WW3.datasets.values())[0]
ncss = best_ds.subset()
query = ncss.query()
import datetime
query.lonlat_box(north=22, south=21, east=73, west=72).time(datetime.datetime.now(datetime.UTC))
query.accept('netcdf4')
query.variables('Significant_height_of_wind_waves_surface')
from xarray.backends import NetCDF4DataStore
import xarray as xr

data = ncss.get_data(query)
data = xr.open_dataset(NetCDF4DataStore(data))
#print(list(data))
sigw_3d = data['Significant_height_of_wind_waves_surface']
# Helper function for finding proper time variable
def find_time_var(var, time_basename='time'):
    for coord_name in var.coords:
        if coord_name.startswith(time_basename):
            return var.coords[coord_name]
    raise ValueError('No time variable found for ' + var.name)
time_1d = find_time_var(sigw_3d)
lat_1d = data['latitude']
lon_1d = data['longitude']
print(time_1d,lat_1d,lon_1d)
import numpy as np
from netCDF4 import num2date
from metpy.units import units

# Reduce the dimensions of the data and get as an array with units
sigw_3d = sigw_3d.metpy.unit_array.squeeze()

# Combine latitude and longitudes 
lon_2d, lat_2d = np.meshgrid(lon_1d, lat_1d)


'''
ds = xr.open_dataset(best_WW3.access_urls['OPENDAP']).sel(lon=slice(72-73,0.25),lat=slice(21-22,0.25))
data_var = ds.metpy.parse_cf('Significant_height_of_swell_waves_ordered_sequence_of_data')
#print(data_var)
#request_time = date.replace(hour=18, minute=0, second=0, microsecond=0)
ds = xr.open_dataset('india.nc')
keylist = ds.keys()
for key in keylist:
 # select a variable subset
 ds_sub = ds.get([str(key)])
 ds_mean = ds_sub.mean(dim='number')
 ds_std = ds_sub.std(dim='number')
 #Convert to pandas dataframe and save it
 df1 = ds_mean.to_dataframe()
 df2 = ds_std.to_dataframe()
 df1.to_csv(str(key)+'_mean.csv')
 df2.to_csv(str(key)+'_spread.csv')
'''

