fl = open('aaxx.csv')
lines = [line.strip() for line in fl.readlines()]
for item in lines:
 idx = item.index('[')
 lst = item[idx:]
 x = lst.split(',')
 x[0] = x[0][1:]
 x[-1] = x[-1][:-1]
 x = [int(i) for i in x]
 lst = item.split(',')
 print float(lst[1]),float(lst[2]),x

