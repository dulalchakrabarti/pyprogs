def cldtype(buf1,buf2):
    '''
    '''
    #print(buf1,buf2)
    if buf1=='' or buf2 == '':
     return 0
    elif buf1 == '/' and '/' in buf2:
     return 0
    elif '/' in buf1:
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
add = "https://www.wis-jma.go.jp/d/o/DEMS/Alphanumeric/Surface/SHIP/20211115/180000/"
f1 = urllib.request.urlopen(add)
txt1 = f1.read()
syn = txt1.split(b'\n')
lst = []
fl = open('class.csv','a')
#fl.write('stn'+','+'stn'+','+'lat'+','+'lon'+','+'cldtype'+'/n')
for item in syn:
 txt = item.decode('utf-8')
 txt = txt.split('<')
 if len(txt) > 3:
  txt = txt[2].split('>')
  lst.append(txt[-1])
lst = lst[1:]
#print(lst)
f1.close()
buf=''
shp = {}
for item in lst:
 f1 = urllib.request.urlopen(add+item)
 txt1 = f1.read()
 syn = txt1.split(b'\n')
 txt = [x.decode('utf-8').strip() for x in syn]
 buf = buf + ' '.join(txt[2:])
 f1.close()
lst = buf.split('=')
for item in lst:
 lst_ = item.split(' ')
 lst_ = [val for val in lst_ if val != '']
 if len(lst_)>5:
  #print(lst_)
  count = 0
  stn = ''
  lat = ''
  lon = ''
  four = ''
  five = ''
  six = ''
  for word in lst_:
   if count == 0:
    stn = word
   if count == 2:
    lat = word
    lat_=lat[2:4]+'.'+lat[4]
   elif count == 3:
    lon = word
    lon_=lon[2:4]+'.'+lon[4]
   elif count == 4:
    four = word[2]
   elif count == 5:
    five = word[0]
   elif word[0] == '8':
    six = word
    print(five,six)
    print(stn+','+lat_,lon_, cldtype(five,six))
    if float(lon_)>60:
     fl.write(stn+','+stn+','+lat_+','+lon_+','+ str(cldtype(five,six))+'\n')
    print('----------------')
   #print(count)
   else:
    pass
   count+=1
   
