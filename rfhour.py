import pandas as pd
import numpy as np
data = ['aws.csv','arg.csv','agro.csv']
gl = open('out.csv','w')
gl.write("DT"+','+"LAT"+','+"LON"+','+"R1"+','+"R2"+'\n')
for item in data:
 dat = pd.read_csv(item)
 for index,row in dat.iterrows():
  if row["R2"] > 0.0:
   print row["DT"],row["LAT"],row["LON"],row["R1"],row["R2"]
   gl.write(row["DT"]+','+str(row["LAT"])+','+str(row["LON"])+','+str(row["R1"])+','+str(row["R2"])+'\n')

