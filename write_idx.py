# Import required modules
import numpy as np
import pandas as pd
import pickle
stn = {}
fl = open('india_rsrw.csv')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]+line[1]]=line[2:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()

def brn2class(brn):
    '''
    '''
    if brn < 45 and brn > 10:
     return 1
    else:
     return 0
def cape2class(cape):
    '''
    '''
    if cape  > 1500:
     return 1
    else:
     return 0
def cin2class(cin):
    '''
    '''
    if  cin > 500:
     return 0
    else:
     return 1
def k2class(k):
    '''
    '''
    if k > 35:
     return 1
    else:
     return 0
def li2class(li):
    '''
    '''
    if li < -5:
     return 1
    else:
     return 0
def sweat2class(sweat):
    '''
    '''
    if sweat > 150:
     return 1
    else:
     return 0
def tot2class(tot):
    '''
    '''
    if tot > 50:
     return 1
    else:
     return 0

df = pd.read_csv("idx.csv")
df1 = df.dropna()


col_list = ['Lift','SWEAT', 'K','Total','CAPE', 'CIN','BulkR','lat','lon','pl']

x = df1[col_list].values
df2 = pd.DataFrame(x, columns=col_list)
num,par = df2.shape
ltn=''
snap = []
rsrw = {}
gl = open('thresh','wb')
for item in range(num):
 if ltn == df2.iloc[item,9]:
  snap.append([li2class(df2.iloc[item,0]),sweat2class(df2.iloc[item,1]),k2class(df2.iloc[item,2]),tot2class(df2.iloc[item,3]),cape2class(df2.iloc[item,4]),cin2class(df2.iloc[item,5]),brn2class(df2.iloc[item,6])])
 elif ltn == '':
  ltn = df2.iloc[item,9]
  snap.append([li2class(df2.iloc[item,0]),sweat2class(df2.iloc[item,1]),k2class(df2.iloc[item,2]),tot2class(df2.iloc[item,3]),cape2class(df2.iloc[item,4]),cin2class(df2.iloc[item,5]),brn2class(df2.iloc[item,6])])
 elif ltn != df2.iloc[item,9]:
  rsrw[ltn] = snap
  snap = []
  ltn = df2.iloc[item,9]
  snap.append([li2class(df2.iloc[item,0]),sweat2class(df2.iloc[item,1]),k2class(df2.iloc[item,2]),tot2class(df2.iloc[item,3]),cape2class(df2.iloc[item,4]),cin2class(df2.iloc[item,5]),brn2class(df2.iloc[item,6])])
for key in rsrw.keys():
 pickle.dump([key,rsrw[key]],gl)
