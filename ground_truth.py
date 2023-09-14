#1..low....................... 100
#2..low...medium.............. 420
#3..low.........high.......... 501
#4........medium.............. 030
#5........medium...high....... 001
#6.................high....... 002
#7...low....medium...high..... 231
#8...........no cloud......... cloud group absent
def cldtype(buf1,buf2):
    '''
    '''
    #print(buf1,buf2)
    if buf1 == '/':
     return 0
    elif int(buf1) == 0:
     return 7
    elif '/' in buf2:
     ptr = buf2.find('/')
     if ptr >= 1:
      return 1
    elif buf2[1] == '/' or int(buf2[1]) == 8 or int(buf2[1]) == 9:
     return 6
    elif int(buf2[2]) > 0 and buf2[3] == '/' and buf2[4] == '/':
     return 0
    elif int(buf2[2]) > 0 and int(buf2[3]) == 0 and buf2[4] == '/':
     return 0
    elif int(buf2[2]) > 0 and int(buf2[3]) == 0 and int(buf2[4]) == 0:
     return 0
    elif int(buf2[2]) > 0 and int(buf2[3]) > 0 and buf2[4] == '/':
     return 1
    elif int(buf2[2]) > 0 and int(buf2[3]) > 0 and int(buf2[4]) == 0:
     return 1
    elif int(buf2[2]) > 0 and int(buf2[3]) == 0 and int(buf2[4]) > 0:
     return 2
    elif int(buf2[2]) == 0 and int(buf2[3]) > 0 and int(buf2[4]) == 0:
     return 3
    elif int(buf2[2]) == 0 and int(buf2[3]) > 0 and int(buf2[4]) > 0:
     return 4
    elif int(buf2[2]) == 0 and int(buf2[3]) == 0 and int(buf2[4]) > 0:
     return 5
    elif int(buf2[2]) > 0 and int(buf2[3]) > 0 and int(buf2[4]) > 0:
     return 6
    else:
     return 1
    
import urllib.request
fl = open("class.csv",'w')
gt = {}
coun = ['Bang','India','Mald','Myan','Nep','Pak','Sri+L']
rep = '' 
for item in coun:
 f1 = urllib.request.urlopen("https://www.ogimet.com/display_synopsc2.php?lang=en&estado="+item+"&tipo=ALL&ord=REV&nil=NO&fmt=txt&ano=2021&mes=11&day=16&hora=18&anof=2021&mesf=11&dayf=16&horaf=18&send=send")
 txt1 = f1.read()
 syn = txt1.split(b'\n')
 for item in syn:
  #print(item)
  txt = item.decode('utf-8')
  if txt[:4] == '2021':
   rep = txt
  elif txt[:2] == '# ':
   txt = txt.split('|')
   if len(txt) > 2:
    stn = txt[0].split(',')
    name = stn[1].strip().split()
    name = name[0]
    #print(name)
    num = stn[0].split()
    idx = num[-1]
    lat = txt[1].strip().split('-')
    lon = txt[2].strip().split('-')
    mlat = round(float(lat[1][:2])/60.0,2)
    mlon = round(float(lon[1][:2])/60.0,2)
    lat = float(lat[0][:2])+mlat
    lon = float(lon[0][:3])+mlon
    #print(idx,lat,lon,rep)
    gt[idx] =[name,lat,lon,rep]
#print(gt)
f1.close()
keylist = gt.keys()
sorted(keylist)
for key in keylist:
 name = gt[key][0]
 lat = gt[key][1]
 lon = gt[key][2]
 buf = gt[key][3]
 buflist = buf.split()
 #print(buflist)
 if len(buflist) > 5:
  buf1 = buflist[5][1]
  buf2 = buflist[-1]
  out = cldtype(buf1,buf2)
  fl.write(str(key)+','+name+','+str(lat)+','+str(lon)+','+str(out)+'\n')
  #print(key,name,lat,lon,out)

