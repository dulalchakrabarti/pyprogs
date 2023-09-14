from netCDF4 import Dataset
import numpy as np
from datetime import datetime, timedelta
import datetime
day = datetime.datetime.strptime("2015-12-1 12:0:0.0", '%Y-%m-%d %H:%M:%S.%f')
for i in range(1,100): 
 print str(day+timedelta(i))
