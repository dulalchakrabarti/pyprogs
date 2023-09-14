import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd

import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import Hodograph, SkewT
from metpy.units import units
# Create a datetime for our request - notice the times are from laregest (year) to smallest (hour)
from datetime import datetime
import requests

def temp(stn):
    '''
    '''
    
    request_time = datetime(2022, 4, 30, 0)
    # Store the station name in a variable for flexibility and clarity
    station = stn
    # Import the Wyoming simple web service and request the data
    # Don't worry about a possible warning from Pandas - it's related to our handling of units
    #print(station,request_time)
    from siphon.simplewebservice.wyoming import WyomingUpperAir
    try:
     df = WyomingUpperAir.request_data(request_time, station)
    except (ValueError, IndexError) as e:
     print("data not available")
     return 0
    except requests.exceptions.HTTPError:
     return 0
    # Drop any rows with all NaN values for T, Td, winds
    df = df.dropna(subset=('temperature', 'dewpoint', 'direction', 'speed'
                       ), how='all').reset_index(drop=True)

    # We will pull the data out of the example dataset into individual variables and
    # assign units.

    p = df['pressure'].values * units.hPa
    T = df['temperature'].values * units.degC
    Td = df['dewpoint'].values * units.degC
    wind_speed = df['speed'].values * units.knots
    wind_dir = df['direction'].values * units.degrees
    u, v = mpcalc.wind_components(wind_speed, wind_dir)

    # Calculate the LCL
    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])

    #print(lcl_pressure, lcl_temperature)

    # Calculate the parcel profile.
    parcel_prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
    # Calculate thermodynamics
    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0],
                                           T[0],
                                           Td[0])

    lfc_pressure, lfc_temperature = mpcalc.lfc(p,
                                           T,
                                           Td)

    el_pressure, el_temperature = mpcalc.el(p,
                                        T,
                                        Td)


    fig = plt.figure(figsize=(14, 14))
    fig.suptitle(sl[station], fontsize=20)
    skew = SkewT(fig, rotation=30)

    # Plot the data using normal plotting functions, in this case using
    # log scaling in Y, as dictated by the typical meteorological plot
    skew.plot(p, T, 'r')
    skew.plot(p, Td, 'g')
    skew.plot_barbs(p, u, v)
    skew.ax.set_ylim(1000, 50)
    skew.ax.set_xlim(-40, 60)

    # Plot LCL as black dot
    skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')

    # Plot the parcel profile as a black line
    skew.plot(p, parcel_prof, 'k', linewidth=2)

    # Shade areas of CAPE and CIN
    skew.shade_cin(p, T, parcel_prof)
    skew.shade_cape(p, T, parcel_prof)
    

    # Plot a zero degree isotherm
    skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    if not pd.isna(lcl_pressure):
     skew.ax.plot(lcl_temperature, lcl_pressure, marker="_", color='black', markersize=30, markeredgewidth=3)
     skew.ax.text(lcl_temperature+2*units.delta_degC, lcl_pressure,'Lifting Condensation Level',fontsize=10, verticalalignment='top',   bbox=props)
   
    if not pd.isna(lfc_pressure):
     skew.ax.plot(lfc_temperature, lfc_pressure, marker="_", color='brown', markersize=30, markeredgewidth=3)
     skew.ax.text(lfc_temperature+2*units.delta_degC, lfc_pressure,'Level of Free Convection',
             fontsize=10, verticalalignment='top', bbox=props)
    
    if not pd.isna(el_pressure):
     skew.ax.plot(el_temperature, el_pressure, marker="_", color='blue', markersize=30, markeredgewidth=3)
     skew.ax.text(el_temperature+2*units.delta_degC, el_pressure, 'Equilibrium Level', 
             fontsize=10, verticalalignment='top', bbox=props)
    if not pd.isna(lcl_pressure):
     if not pd.isna(lfc_pressure):
      if not pd.isna(el_pressure):
       # Calculate surface based cape/cin
       s_cape, s_cin = mpcalc.surface_based_cape_cin(p,T,Td)
       skew.ax.text(lfc_temperature-55*units.delta_degC, lfc_pressure-300*units.hPa,'CAPE='+str(s_cape),
             fontsize=10, verticalalignment='top', bbox=props)
       skew.ax.text(lfc_temperature-55*units.delta_degC, lfc_pressure-400*units.hPa,'CIN='+str(s_cin),
             fontsize=10, verticalalignment='top', bbox=props)
    # Create a hodograph
    # Create an inset axes object that is 50% width and height of the
    # figure and put it in the upper right hand corner.
    ax_hod = inset_axes(skew.ax, '40%', '40%', loc='upper right')
    h = Hodograph(ax_hod, component_range=90.)
    h.add_grid(increment=20)
    l = h.plot_colormapped(u, v, wind_speed)  # Plot a line colored by wind speed
    plt.colorbar(l)
    # Show the plot
    plt.savefig(sl[station])
    plt.show()
    return 1
sl = {'42182':'New Delhi','42809':'Kolkata','43279':'Chennai','43003':'Mumbai','42647':'Ahmadabad','43285':'Mangalore','42410':'Guwahati','42867':'Nagpur','43371':'Thiruvananthapuram'}
station1 = ['42182','42809','43279','43003','42647','43285','42410','42867','43371']
for item in station1:
 print(temp(item))
 

