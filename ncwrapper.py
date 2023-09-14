#! /usr/bin/env python
# file: readnc.py
# $id: $

"""
SYNOPSIS:
Contains two functions which read and return
netCDF variables, variable attributes, and global
attributes to main program.

REQUIRES:
Python netCDF4 module. See:
http://code.google.com/p/netcdf4-python/

USAGE:
Requires usage of main program as follows:
% ncwrapper.py -f <filename>

"""

#import
from optparse import OptionParser
from netCDF4 import Dataset

# authorship
__author__     = "David Moroni"
__copyright__  = "Copyright 2012, California Institute of Technology"
__credits__    = ["Ed Armstrong and David Moroni"]
__license__    = "none"
__version__    = "1.0"
__maintainer__ = "David Moroni"
__email__      = "david.m.moroni at jpl dot nasa dot gov"
__status__     = "Release Candidate"

# ---------------------------
# read and return global_atts
# ---------------------------
def readGlobalAttrs( nc_file ):
  attr_list = []
  global_attr = []
  #print 'Global attributes:'
  for attr_name in nc_file.ncattrs():
      #print attr_name, '=', getattr(nc_file, attr_name)
      attr_list.append( attr_name )
      atts = getattr( nc_file, attr_name )
      global_attr.append( atts )
  return attr_list, global_attr 

# --------------------------------------------------
# read and return variables and their attributes 
# --------------------------------------------------
var_list = []
var_attr_list = []
var_data_list = []
def readVars ( nc_file ):
#print 'Variables:' 
#dictionary of variables:values
  vars =  nc_file.variables.keys()
  for var_name in vars:
      attr = nc_file.variables[var_name]
      vardata = nc_file.variables[var_name][:]
      var_attr_list.append( attr )
      var_data_list.append( vardata)
#      print var_name, ':', attr
#      print var_name, ' data sample[0:10]:', vardata[0:10]
  return vars, var_attr_list, var_data_list

#import
from optparse import OptionParser
import readnc
from netCDF4 import Dataset
# Read command line using optparse module
parser = OptionParser( )
parser.add_option( "-f", "--file", dest="filename",
                  help="filename to validate metadata and structure", metavar="FILE",
		  type = 'string' )
(options, args) = parser.parse_args()

if not options.filename :
    parser.error("Specify a NetCDF file name!")
else :
    ncfile = options.filename
wfl = open('/home/dulal/insat/ascat_'+ncfile[15:21]+'.csv','w')
# -----------------------------
# Open netCDF4 file for reading
# -----------------------------
try:
    nc_file = Dataset( ncfile, 'r' )
except IOError:
    print 'not a valid netCDF file'
[vars, var_attr_list, var_data_list] = readnc.readVars( nc_file )
count = 0
for i in range(0, len(var_data_list[1])):
 for j in range(0, len(var_data_list[1][0])):
  if var_data_list[1][i][j]>0.0 and var_data_list[1][i][j]<40.0:
   if var_data_list[2][i][j]>50.0 and var_data_list[2][i][j]<100.0:
    if var_data_list[9][i][j] != '--' and var_data_list[10][i][j] != '--':
     if count%11 == 0:
      if var_data_list[10][i][j] <= 180.0:
       var_data_list[10][i][j] = var_data_list[10][i][j] + 180.0
       wfl.write(str(var_data_list[1][i][j])+','+str(var_data_list[2][i][j])+','+str(2*var_data_list[9][i][j])+','+str(var_data_list[10][i][j])+'\n')
      else:
       var_data_list[10][i][j] = var_data_list[10][i][j] - 180.0
       wfl.write(str(var_data_list[1][i][j])+','+str(var_data_list[2][i][j])+','+str(2*var_data_list[9][i][j])+','+str(var_data_list[10][i][j])+'\n')
      count = count + 1
     else:
      count = count + 1

# close the file
nc_file.close()
wfl.close()

