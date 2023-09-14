import numpy as np

def typ(idx):
    labels = list(map(' '.join, np.eye(4, dtype=np.uint).astype(str)))
    if idx < 70:
     label = 2
    elif idx > 69 and idx < 91:
     label = 4
    elif idx > 90 and idx < 110:
     label = 2
    elif idx > 109 and idx < 132:
     label = 3
    elif idx > 131 and idx < 187:
     label = 2
    else:
     label = 1
    return labels[label-1]

occ = {}
fl = open("sat_cld_train.txt")
gl = open("reclass.txt","w")
label_list = []
img_list =[]
cld = [line.strip() for line in fl.readlines()]
for item in cld:
 item = item.split("|")
 itm = item[1].split(" ")
 idx = itm.index("1")
 #print '|labels '+typ(idx)+' |'+item[2]
 gl.write('|labels '+typ(idx)+' |'+item[2]+'\n')

