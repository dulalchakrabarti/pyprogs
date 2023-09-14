import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('data_factory.csv')
c1 = df['time'].tolist()
c2 = df['ir1'].tolist()
lst1 = c1[:868]
lst2 = c2[:868]
lst3 =[]
for n in range(0,len(lst1),40):
 lst3.append(lst1[n])
#print(lst3)
plt.figure(figsize=(14,12))
plt.plot(lst1, lst2)
plt.xticks(lst3,rotation=20,size=10)
plt.show()

