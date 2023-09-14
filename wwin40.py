import urllib2
import pickle
url="http://tgftp.nws.noaa.gov/data/raw/ww/wwin40.dems..txt"
page =urllib2.urlopen(url)
data=page.read()
words = data.split()
for idx in range(len(words)):
 if words[idx] == 'IWB':
  name=words[idx]+words[idx+1]+words[idx+2]+words[idx+3]+words[idx+4]
store = {}
xx=data.split("(.)")
for x in range(len(xx)):
   store[x] = xx[x]
pickle.dump(store,open(name,"wb"))
txt = pickle.load(open(name,"rb"))
for key,value in txt.items():
 val = value.strip()
 print val.split("\n")
