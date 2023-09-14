#1..low....................... 100
#2..low...medium.............. 420
#3..low.........high.......... 501
#4........medium.............. 030
#5........medium...high....... 001
#6.................high....... 002
#7...low....medium...high..... 231
#8...........no cloud......... cloud group absent
stn = {}
fl = open('india_station.csv')
gl = open('class.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
 lst = inp.split()
 #print(len(lst),len(lst[0]))
 if len(lst)>0 and len(lst[0])==5:
  idx = lst[0]
  gr = 1
  #print(idx,'---------------------------------')
  flag = False
  lc = ''
  mc = ''
  hc = ''
  for word in lst[gr:]:
   if gr == 1:
    #print 'irixhvv',word,word[2]
    gr+=1
   elif gr == 2:
    #print 'nddff',word,word[0]
    if word[0] == '0':
     cl = 7
     stn[idx].append(str(cl))
    gr+=1
   elif word[:1] == '7':
    #print '7wwW1W2',word,word[1:3],word[3:]
    gr+=1
   elif word[:1] == '8'and not flag:
    #print('8NhCLCMCH',word,word[1],word[2],word[3],word[4])
    if word[2:].isdigit():
     if word[2] == '0':
      if word[3] == '0':
       #print('.................high.......',word[2:])
       cl = 5
       stn[idx].append(str(cl))
      elif word[4] == '0':
       #print('...........medium.......',word[2:])
       cl = 3
       stn[idx].append(str(cl))
      else:
       #print('........medium...high.......',word[2:])
       cl = 4
       stn[idx].append(str(cl))
     elif word[3] == '0':
      if word[4] == '0':
       #print('..low.......................',word[2:])
       cl = 0
       stn[idx].append(str(cl))
      else:
       #print('..low.........high..........',word[2:])
       cl = 2
       stn[idx].append(str(cl))
     elif word[4] == '0':
      #print('..low...medium..............',word[2:])
      cl = 1
      stn[idx].append(str(cl))
     else:
      #print('...low....medium...high',word[2:])
      cl = 6
      stn[idx].append(str(cl))
    elif word[2].isdigit():
     if word[3].isdigit():
      #print('...low.....medium.......',word[4:])
      cl = 1
      stn[idx].append(str(cl))
     else:
      #print('......low.........',word[3:])
      cl = 0
      stn[idx].append(str(cl))
    else:
     print(word[2:])
    gr+=1
   elif word == '333':
    #print('333')
    flag = True
    gr+=1
   elif flag and word[:1] == '8':
    #print '8NsChshs',word,word[1],word[2],word[3:]
    gr+=1
   else:
    gr+=1
count = 0
for key,val in  stn.items():
 if len(stn[key]) > 3:
  count+=1
  lst =[ str(x) for x in stn[key]]
  txt = key+','+','.join(lst)
  gl.writelines(txt +'\n')
  #print(txt,count)

