lines = [line.rstrip('\n') for line in open('cloudgr.csv')]
for item in lines:
 print '.................'
 m = 0
 x = len(item)
 print len(item)
 print '+++++++++++++++++'
 try:
    for itm in item:
     n = item.index('8nchh',m,x)
     m = m + n + 1
     print m
 except:
    print -1
