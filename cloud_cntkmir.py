import pandas as pd
def line2cloud(line):
    '''
    '''
    layers=''
    line = ''.join(xx for xx in line)
    line = line.split('(')
    for item in line:
     item = item.split(')')
     if len(item[0]) == 2:
      if item[0] not in layers:
       layers = layers+item[0]
    if len(layers) > 0:
     return layers
pair_cld = {}
pair_pix = {}
pair_lr = {}
count = 1
hl = pd.read_csv("layersmir.csv")
for index,row in hl.iterrows():
 pair_lr[row["type"]] = count
 count = count + 1
fl = open("zzxxmir.csv")
gl = open("nchhmir.csv")
cld = [line.strip() for line in gl.readlines()]
pix = [line.strip() for line in fl.readlines()]
for idx in range(len(cld)):
 items = cld[idx].split(',')
 pair_cld[items[0]] =items[1:]
for idx in range(len(pix)):
 items = pix[idx].split(',')
 if pair_cld.has_key(items[0]):
  pair_pix[items[0]] =items[1:]
for key in pair_cld.keys():
 lr = line2cloud(pair_cld[key])
 if lr != None and lr != 'nan':
  if pair_lr.has_key(lr):
   pass
  else:
   pair_lr[lr] = count
   count = count + 1
keylist = pair_lr.keys()
keylist.sort()
il = open("layersmir.csv","w")
il.write('type'+','+'class'+'\n')
jl = open("train_cloudmir.csv","w")
for key in keylist:
 il.write(str(key)+','+str(pair_lr[key])+'\n')
for key in pair_cld.keys():
 if key != '' and len(pair_cld[key]) > 2:
  lr = line2cloud(pair_cld[key])
  jl.write(key+','+str(pair_lr[lr])+','+pair_pix[key][0]+','+pair_pix[key][1]+','+(','.join(x for x in pair_pix[key][2:]))+'\n')
