occ = {}
fl = open("sat_cld_train.save")
gl = open("stat.csv","w")
cld = [line.strip() for line in fl.readlines()]
for item in cld:
 item = item.split("|")
 itm = item[1].split(" ")
 idx = itm.index("1")
 if occ.has_key(idx):
  occ[idx] = occ[idx]+1
 else:
  occ[idx] = 1
keylist = occ.keys()
keylist.sort()
for key in keylist:
 print key,occ[key]
 gl.write(str(key)+","+str(occ[key])+"\n")
