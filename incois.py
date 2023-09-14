import urllib2

f = urllib2.urlopen("http://www.incois.gov.in/portal/osf/tidegraphphases.jsp?region=Vasai")
html = f.read()
lines = html.split('\n')
high_date=[]
high_val = []
low_date=[]
low_val = []
for item in lines:
 if item[0:3] == '<tr':
  item = item.split('<')
  if len(item) >= 10:
   x1 = item[3].strip().split('>')
   high_date.append(x1[1])
   x2 = item[5].strip().split('>')
   high_val.append(x2[1])
   x3 = item[7].strip().split('>')
   low_date.append(x3[1])
   x4 = item[9].strip().split('>')
   low_val.append(x4[1])
print high_date
print high_val
print low_date
print low_val
