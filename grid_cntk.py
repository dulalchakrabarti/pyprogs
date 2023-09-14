import numpy as np
def savetxt(fname, lbl, img):
        with open('/home/dc/rapidnight/'+fname, 'w') as f:
            labels = list(map(' '.join, np.eye(8, dtype=np.uint).astype(str)))
            for idx in range(len(lbl)):
                #print(img[idx])
                row_str = img[idx][:,].astype(str)
                label_str = labels[lbl[idx]]
                feature_str = ' '.join(row_str)
                f.write('|labels {} |features {}\n'.format(label_str, feature_str))
label_list = []
img_list =[]
stn_list = []
wvlines = [line.rstrip('\n') for line in open('gridwv.txt')]
mirlines = [line.rstrip('\n') for line in open('gridmir.txt')]
ir2lines = [line.rstrip('\n') for line in open('gridir2.txt')]
ir1lines = [line.rstrip('\n') for line in open('gridir1.txt')]
for num in range(len(wvlines)):
 img = []
 wvline = wvlines[num].split(',')
 #print(len(wvline[4:]),wvline[4:])
 img.extend(wvline[4:])
 mirline = mirlines[num].split(',')
 #print(len(mirline[4:]),mirline[4:])
 img.extend(mirline[4:])
 ir2line = ir2lines[num].split(',')
 #print(len(ir2line[4:]),ir2line[4:])
 img.extend(ir2line[4:]) 
 ir1line = ir1lines[num].split(',')
 #print(len(ir1line[4:]),ir1line[4:])
 img.extend(ir1line[4:])
 ss = [int(x) for x in img]
 arr = np.array(ss)
 img_list.append(arr)
 lbl = wvline[3]
 label_list.append(int(lbl))
 stn_list.append(wvline[0])
print(len(img_list))
print(len(label_list))
print(len(stn_list))
savetxt("grid_sat_cntk.txt", label_list, img_list)
print ('Writing train text file...')

