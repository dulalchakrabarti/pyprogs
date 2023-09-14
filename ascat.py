import urllib2
import pickle
url="http://opendap.jpl.nasa.gov/opendap/OceanWinds/ascat/preview/L2/metop_a/25km/2015/294/ascat_20151021_084500_metopa_46722_eps_o_250_2300_ovw.l2.nc.gz.ascii?"
page =urllib2.urlopen(url)
data=page.read()
line = data.split("\n")
for idx in range(len(line)):
 print line[idx]
"""
store = {}
xx=data.split("(.)")
for x in range(len(xx)):
   store[x] = xx[x]
pickle.dump(store,open(name,"wb"))
txt = pickle.load(open(name,"rb"))
for key,value in txt.items():
 val = value.strip()
 print val.split("\n")
"""
