import pandas as pd
import glob
import matplotlib.pyplot as plt

# set search path and glob for files
# here we want to look for csv files in the input directory
cn = pd.read_csv('cnn1.csv')
mnb = cn['Minibatch'].tolist()
err = cn['%Error'].tolist()
#print(mnb)
#print(err)
files = glob.glob('*grid.csv')
lst1=[]
lst2=[]
lst3=[]
lst4=[]
lst5=[]
for item in files:
 #print(item[2:5])
 if item[2:5] == '09_':
  lst3.append(item)
 elif item[2:5] == '10_':
  lst4.append(item)
 elif item[2:4] == '09':
  lst1.append(item)
 elif item[2:4] == '10':
  lst2.append(item)
lst1.sort()
lst2.sort()
lst1.extend(lst2)
lst3.sort()
lst4.sort()
lst3.extend(lst4)
x = zip(lst1,lst3)
y = [i for i in x]
lst5 = list(sum(y,()))
# create empty list to store dataframes
grds24 = {}
for num in range(1521):
 grds24[num] = []
cld24 = []
# loop through list of files and read each one into a dataframe and append to list
for f in lst1:
    # read in csv
    temp_df = pd.read_csv(f)
    cld24 = temp_df['cloudtype'].tolist()
    for num in range(1521):
     grds24[num].append(cld24[num])
     #print(num,grds[num])
keylist24 = grds24.keys()
t24 = range(len(lst1))
grds12 = {}
for num in range(1521):
 grds12[num] = []
cld12 = []
# loop through list of files and read each one into a dataframe and append to list
for f in lst5:
    # read in csv
    temp_df = pd.read_csv(f)
    cld12 = temp_df['cloudtype'].tolist()
    for num in range(1521):
     grds12[num].append(cld12[num])
     #print(num,grds[num])
keylist12 = grds12.keys()
t12 = range(len(lst5))
#for n in [0, 300, 700, 1400]:
grdsnight24 = {}
for num in range(1521):
 grdsnight24[num] = []
cldnight24 = []
# loop through list of files and read each one into a dataframe and append to list
for f in lst3:
    # read in csv
    temp_df = pd.read_csv(f)
    cldnight24 = temp_df['cloudtype'].tolist()
    for num in range(1521):
     grdsnight24[num].append(cldnight24[num])
     #print(num,grds[num])
keylistnight24 = grdsnight24.keys()
tnight24 = range(len(lst3))

fig, axs = plt.subplots(2, 2)
fig.suptitle('CNN Model outputs')
axs[0, 0].plot(mnb, err)
axs[0, 0].set_xlabel('Iteration')
axs[0, 0].set_ylabel('%Error')
axs[0, 0].set_title('(a)CNN Model Error Graph')
axs[0, 1].plot(t24, grds24[899], 'tab:orange')
axs[0, 1].set_xlabel('Day')
axs[0, 1].set_ylabel('Cloud Type')
axs[0, 1].set_title('(b)24 Hour Cloud Type Variation\nat 06 UTC at Grid No.899')
axs[1, 0].plot(tnight24, grdsnight24[899], 'tab:green')
axs[1, 0].set_xlabel('Day')
axs[1, 0].set_ylabel('Cloud Type')
axs[1, 0].set_title('(c)24 Hour Cloud Type Variation\nat 18 UTC at Grid No.899')
axs[1, 1].plot(t12, grds12[899], 'tab:red')
axs[1, 1].set_xlabel('Day')
axs[1, 1].set_ylabel('Cloud Type')
axs[1, 1].set_title('(d)12 Hour Cloud Type Variation\nat Grid No.899')

#for ax in axs.flat:
    #ax.set(xlabel='Days', ylabel='Cloud Type')

# Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
    #ax.label_outer()
fig.tight_layout()
plt.savefig('out.png')
plt.show()
a = input('Press any key to exit:')
if a:
 exit(0)     

