# Create a datetime for our request - notice the times are from laregest (year) to smallest (hour)
from datetime import datetime
request_time = datetime(2022, 3, 15, 0)
# Store the station name in a variable for flexibility and clarity
station = '42182'
# Import the Wyoming simple web service and request the data
# Don't worry about a possible warning from Pandas - it's related to our handling of units
from siphon.simplewebservice.wyoming import WyomingUpperAir
df = WyomingUpperAir.request_data(request_time, station)
from metpy.units import pandas_dataframe_to_unit_arrays, units
sounding = pandas_dataframe_to_unit_arrays(df)
import matplotlib.pyplot as plt
from metpy.plots import SkewT
# Make a figure
fig = plt.figure(figsize=(10, 10))

# Make a SkewT object
skew = SkewT(fig)

# Plot the temperature and dewpoint
skew.plot(sounding['pressure'], sounding['temperature'], linewidth=2, color='tab:red')
skew.plot(sounding['pressure'], sounding['dewpoint'], linewidth=2, color='tab:green')
# Plot wind barbs
skew.plot_barbs(sounding['pressure'], sounding['u_wind'], sounding['v_wind'])

# Add dry adiabats
skew.plot_dry_adiabats()

# Add moist adiabats
skew.plot_moist_adiabats()

# Add mixing ratio lines
skew.plot_mixing_lines()
import metpy.calc as mpcalc
# Calculate the ideal surface parcel path
sounding['profile'] = mpcalc.parcel_profile(sounding['pressure'],
                                            sounding['temperature'][0],
                                            sounding['dewpoint'][0]).to('degC')
#We can also calculate the ideal parcel profile and plot it.
# Plot the profile
skew.plot(sounding['pressure'], sounding['profile'], color='black')

# Calculate the LCL
lcl_pressure, lcl_temperature = mpcalc.lcl(sounding['pressure'][0],
                                           sounding['temperature'][0],
                                           sounding['dewpoint'][0])
skew.ax.plot(lcl_temperature, lcl_pressure, marker="_", color='k', markersize=30, markeredgewidth=3)
# Calculate the LFC
lfc_pressure, lfc_temperature = mpcalc.lfc(sounding['pressure'],
                                           sounding['temperature'],
                                           sounding['dewpoint'])

# Calculate the EL
el_pressure, el_temperature = mpcalc.el(sounding['pressure'],
                                        sounding['temperature'],
                                        sounding['dewpoint'])
if lcl_pressure:
    skew.ax.plot(lcl_temperature, lcl_pressure, marker="_", color='orange', markersize=30, markeredgewidth=3)
    
if lfc_pressure:
    skew.ax.plot(lfc_temperature, lfc_pressure, marker="_", color='brown', markersize=30, markeredgewidth=3)
    
if el_pressure:
    skew.ax.plot(el_temperature, el_pressure, marker="_", color='blue', markersize=30, markeredgewidth=3)

# Set axis limits
skew.ax.set_xlim(-60, 30)
skew.ax.set_ylim(1000, 100)

# Add fiducial lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()
# Calculate surface based cape/cin
surface_cape, surface_cin = mpcalc.surface_based_cape_cin(sounding['pressure'],
                                                          sounding['temperature'],
                                                          sounding['dewpoint'])

# Print CAPE and CIN
print('CAPE: {}\tCIN: {}'.format(surface_cape, surface_cin))

# Shade CAPE
skew.shade_cape(sounding['pressure'],
                sounding['temperature'],
                sounding['profile'])

# Shade CIN
skew.shade_cin(sounding['pressure'],
               sounding['temperature'],
               sounding['profile'])

# Import the hodograph class
from metpy.plots import Hodograph

# Make a figure and axis
fig, ax = plt.subplots(1, 1, figsize=(6, 6))

# Create a hodograph
h = Hodograph(ax, component_range=60.)

# Add "range rings" to the plot
h.add_grid(increment=20)

# Plot the wind data
h.plot(sounding['u_wind'], sounding['v_wind'], color='tab:red')

#We can even add wind vectors, which is helpful for learning/teaching hodographs.

# Add vectors
#h.wind_vectors(sounding['u_wind'], sounding['v_wind'])

# Calculate the height above ground level (AGL)
sounding['height_agl'] = sounding['height'] - sounding['height'][0]

# Make an array of segment boundaries - don't forget units!
boundaries = [0, 1, 3, 5, 8] * units.km

# Make a list of colors for the segments
colors = ['tab:red', 'tab:green', 'tab:blue', 'tab:olive']
# Create a hodograph object/fiducial lines
h = Hodograph(ax, component_range=60.)
h.add_grid(increment=20)
wind_speed = df['speed'].values * units.knots
wind_dir = df['direction'].values * units.degrees

h.plot_colormapped(sounding['u_wind'], sounding['v_wind'], wind_speed)  # Plot a line colored by wind speed

plt.show()
