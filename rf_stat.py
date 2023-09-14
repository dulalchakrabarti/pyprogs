import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('rfseason.csv')
tot = df['srf'].tolist()
less = []
norm = []
excs =[]
for item in tot:
 if item <= -19:
  less.append(item)
 elif item >= -19 and item <= 19:
  norm.append(item)
 else:
  excs.append(item)
print(len(less),len(norm),len(excs),len(tot))
print(len(less)*100/float(len(tot)),len(norm)*100/float(len(tot)),len(excs)*100/float(len(tot)))

