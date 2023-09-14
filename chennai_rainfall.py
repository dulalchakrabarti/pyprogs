import string
stn = {}
fl = open('/home/dulal/synop/india_station.csv')
gl = open('/home/dulal/synop/chennai_rainfall.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[1]]=line[0]+' '+line[2]+' '+line[3]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('/home/dulal/synop/chennai.txt')]
for inp in lines:
   lst = inp.split()
   if lst != []:
    flag = True
    for word in lst:
     if flag:
       rf = lst[-1]
       if stn.get(word) != None:
        xx = stn[word]+' '+ rf
        stn[word]=xx
        flag = False
        xx=stn[word].split(' ')
        gl.writelines( xx[1]+','+xx[2]+','+xx[3]+'\n' ) 
gl.close()
