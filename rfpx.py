import pandas as pd
import numpy as np
date = raw_input('Input date(2018-05-29)?')
gl = open('monsoon'+'/'+date+'.csv','w')
rf = {}
dat = pd.read_csv("out.csv")
for index,row in dat.iterrows():
 pix = (row["29MAY201_1"]+row["29MAY201_2"]+row["29MAY201_3"])/3
 if row["field_4"] > 0.0:
  print row["field_1"],row["field_2"],row["field_3"],row["field_4"],pix
  gl.write(str(row["field_1"])+','+str(row["field_2"])+','+str(row["field_3"])+','+str(row["field_4"])+','+str(pix)+'\n')
