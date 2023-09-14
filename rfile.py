import numpy as np
def savetxt(fname, lbl, img):
        with open('/home/dc/rapid/'+fname, 'a+') as f:
            labels = list(map(' '.join, np.eye(8, dtype=np.uint).astype(str)))
            for idx in range(len(lbl)):
                row_str = img[idx][:,].astype(str)
                label_str = labels[lbl[idx]]
                feature_str = ' '.join(row_str)
                f.write('|labels {} |features {}\n'.format(label_str, feature_str))
label_list = []
img_list =[]
stn_list = []
lines = [line.rstrip('\n') for line in open('cloud.txt')]
count = 0
for line in lines:
 lst = line.split(',')
 lbl = lst[3]
 ss = [int(x) for x in lst[4:]]
 arr = np.array(ss)
 label_list.append(int(lbl)-1)
 img_list.append(arr)
 stn_list.append(lst[0])
 count+=1
print(count)
savetxt("sat_cntk.txt", label_list, img_list)
print ('Writing train text file...')

