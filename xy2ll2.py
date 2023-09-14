import pyproj
p = pyproj.Proj("+proj=merc +lon_0=75 +x_0=0 +y_0=0 +a=6378137 +b=6356752.3142 +lat_0=17.75 +units=m +no_defs")
x,y = -3234623.003937, 5401854.420193
lon, lat = p(x, y, inverse=True)
print lat, lon
'''
  Projection_Information_false_easting=0 
  Projection_Information_false_northing=0 
  Projection_Information_grid_mapping_name=mercator
  Projection_Information_longitude_of_projection_origin=75 
  Projection_Information_lower_left_lat_lon(degrees)=-10 44.5 
  Projection_Information_lower_right_lat_lon(degrees)=-10 105.5 
  Projection_Information_semi_major_axis=6378137 
  Projection_Information_semi_minor_axis=6356752.3142 
  Projection_Information_standard_parallel=17.75 
  Projection_Information_upper_left_lat_lon(degrees)=45.5 44.5 
  Projection_Information_upper_left_xy(meters)=-3234623.003937 5401854.420193 
  Projection_Information_upper_right_lat_lon(degrees)=45.5 105.5 
'''
