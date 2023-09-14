import numpy as np
def savetxt(fname, lbl, img):
        with open('/home/dc/rapidnew/'+fname, 'a+') as f:
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
wvlines = [line.rstrip('\n') for line in open('cloudwv.txt')]
mirlines = [line.rstrip('\n') for line in open('cloudmir.txt')]
ir2lines = [line.rstrip('\n') for line in open('cloudir2.txt')]
ir1lines = [line.rstrip('\n') for line in open('cloudir1.txt')]
swirlines = [line.rstrip('\n') for line in open('cloudswir.txt')]
vislines = [line.rstrip('\n') for line in open('cloudvis.txt')]
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
 swirline = swirlines[num].split(',')
 #print(len(swirline[4:]),swirline[4:])
 img.extend(swirline[4:])
 visline = vislines[num].split(',')
 #print(len(visline[4:]),visline[4:])
 img.extend(visline[4:])
 ss = [int(x) for x in img]
 arr = np.array(ss)
 img_list.append(arr)
 lbl = visline[3]
 label_list.append(int(lbl))
 stn_list.append(visline[0])
print(len(img_list))
print(len(label_list))
print(len(stn_list))
savetxt("sat_cntk.txt", label_list, img_list)
print ('Writing train text file...')
