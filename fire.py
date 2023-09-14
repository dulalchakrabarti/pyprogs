import pandas as pd
import numpy as np
fl = open('fire.csv','w')
df = pd.read_csv('fire_india.csv')
for k,row in df.iterrows():
 fire = row.tolist()
 if fire[5] == '2022-11-04':
  #print(fire[0],fire[1],fire[2],fire[10])
  if float(fire[0]) > 5 and float(fire[0]) < 40 and float(fire[1])>60 and float(fire[1]) < 95:
   print(fire[0],fire[1])
   fl.write(str(fire[0])+','+str(fire[1])+'\n')
fl.close()
