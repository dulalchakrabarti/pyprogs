import numpy as np

fl = open("sat_cld.csv","a+")
label_list = []
img_list =[]
stn_list = []

img = {}
chan = ['ir1','ir2','swir','mir','vis','wv']
for item in chan:
 gl = open('train_cloud'+item+'.csv')
 buf = [line.strip() for line in gl.readlines()]
 for dat in buf:
  dat = dat.split(',')
  if img.has_key(dat[0]):
   img[dat[0]].append(dat[4:])
  else:
   img[dat[0]] = [dat[1],dat[4:]]
 gl.close()
keylist = img.keys()
keylist.sort()
for key in keylist:
 stn = key
 lbl = img[key][0]
 lst = img[key][1:]
 ss = ''
 for item in lst:
  xx = item[0].split('[')
  item[0] = xx[1]
  xx = item[-1].split(']')
  item[-1] = xx[0]
  itm = ','.join(x for x in item)
  if len(ss) > 0:
   ss = ss+','+itm
  else:
   ss = itm
 ss = ss.split(',')
 ss = [int(x) for x in ss]
 arr = np.array(ss)
 label_list.append(int(lbl))
 img_list.append(arr)
 stn_list.append(stn)

def savetxt(fname, lbl, img):
        with open('/home/dulal/imgproc/'+fname, 'a+') as f:
            labels = list(map(' '.join, np.eye(1000, dtype=np.uint).astype(str)))
            for idx in range(len(lbl)):
                row_str = img[idx][:,].astype(str)
                label_str = labels[lbl[idx]]
                feature_str = ' '.join(row_str)
                f.write('|labels {} |features {}\n'.format(label_str, feature_str))
print ('Writing train text file...')
savetxt("sat_cld_train.txt", label_list, img_list)
for num in range(len(stn_list)):
 fl.write(stn_list[num]+','+str(label_list[num])+"\n")
