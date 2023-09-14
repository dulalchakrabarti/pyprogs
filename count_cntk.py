import numpy as np
nval = 1024
def savetxt(fname, lbl, img):
        with open(fname, 'a') as f:
            labels = list(map(' '.join, np.eye(8, dtype=np.uint).astype(str)))
            for idx in range(len(lbl)):
                #print(img[idx])
                row_str = img[idx][:,].astype(str)
                label_str = labels[lbl[idx]]
                feature_str = ' '.join(row_str)
                f.write('|labels {} |features {}\n'.format(label_str, feature_str))
label_list = []
img_list =[]
wvlines = [line.rstrip('\n') for line in open('cloudwv.csv')]
mirlines = [line.rstrip('\n') for line in open('cloudmir.csv')]
ir2lines = [line.rstrip('\n') for line in open('cloudir2.csv')]
ir1lines = [line.rstrip('\n') for line in open('cloudir1.csv')]
for num in range(len(wvlines)):
 img = []
 wvline = wvlines[num].split(',')
 wvcnt = wvline[3:]
 mwvcnt = max(wvcnt)
 #print(mwvcnt,wvcnt)
 nwvcnt = [round((float(x)/float(mwvcnt))*nval) for x in wvcnt]
 img.extend(nwvcnt)
 mirline = mirlines[num].split(',')
 mircnt = mirline[3:]
 mmircnt = max(mircnt)
 #print(mmircnt,mircnt)
 nmircnt = [round((float(x)/float(mmircnt))*nval) for x in mircnt]
 img.extend(nmircnt)
 ir2line = ir2lines[num].split(',')
 ir2cnt = ir2line[3:]
 mir2cnt = max(ir2cnt)
 #print(mir2cnt,ir2cnt)
 nir2cnt = [round((float(x)/float(mir2cnt))*nval) for x in ir2cnt]
 img.extend(nir2cnt)
 ir1line = ir1lines[num].split(',')
 ir1cnt = ir1line[3:]
 mir1cnt = max(ir1cnt)
 #print(mir1cnt,ir1cnt)
 nir1cnt = [round((float(x)/float(mir1cnt))*nval) for x in ir1cnt]
 img.extend(nir1cnt)
 ss = [int(x) for x in img]
 arr = np.array(ss)
 img_list.append(arr)
 lbl = wvline[2]
 label_list.append(int(lbl))
#print(len(img_list))
#print(len(label_list))
savetxt("sat_cntk.txt", label_list, img_list)
print ('Writing train text file...')

