import xarray as xr
import pandas as pd
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

