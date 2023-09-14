'''
#1..low....................... 100
#2..low...medium.............. 420
#3..low.........high.......... 501
#4........medium.............. 030
#5........medium...high....... 001
#6.................high....... 002
#7...low....medium...high..... 231
#8...........no cloud/no observation......... cloud group absent
#N -- Amount of low clouds covering sky, if no low clouds, the amount of the middle clouds
0 -- 0 eighths (clear)
1 -- 1/8th
2 -- 2/8ths
3 -- 3/8ths
4 -- 4/8ths
5 -- 5/8ths
6 -- 6/8ths
7 -- 7/8ths
8 -- 8/8ths (overcast)
9 -- sky obscured
/ -- no observation 
#CL -- Low cloud type

    0 -- no low clouds
    1 -- cumulus humulis or fractus (no vertical development)
    2 -- cumulus mediocris or congestus (moderate vertical development)
    3 -- cumulonimbus calvus (no outlines nor anvil)
    4 -- stratocumulus cumulogenitus (formed by spreading of cumulus)
    5 -- stratocumulus
    6 -- stratus nebulosus (continuous sheet)
    7 -- stratus or cumulus fractus (bad weather)
    8 -- cumulus and stratocumulus (multilevel)
    9 -- cumulonimbus with anvil
    / -- low clouds unobserved due to darkness or obscuration 

CM -- Middle cloud type

    0 -- no middle clouds
    1 -- altostratus translucidous (mostly transparent)
    2 -- altostratus opacus or nimbostratus
    3 -- altocumulus translucidous (mostly transparent)
    4 -- patches of altocumulus (irregular, lenticular)
    5 -- bands of altocumulus
    6 -- altocumulus cumulogenitus (formed by spreading of cumulus)
    7 -- altocumulus (multilayers)
    8 -- altocumulus castellanus (having cumuliform tufts)
    9 -- altocumulus of a chaotic sky
    / -- middle clouds unobserved due to darkness or obscuration 

CH -- High cloud type

    0 -- no high clouds
    1 -- cirrus fibratus (wispy)
    2 -- cirrus spissatus (dense in patches)
    3 -- cirrus spissatus cumulogenitus (formed out of anvil)
    4 -- cirrus unicus or fibratus (progressively invading sky)
    5 -- bands of cirrus or cirrostratus invading sky (less than 45 degree above horizon)
    6 -- bands of cirrus or cirrostratus invading sky (more than 45 degree above horizon)
    7 -- cirrostratus covering whole sky
    8 -- cirrostratus not covering sky but not invading
    9 -- cirrocumulus
    / -- high clouds unobserved due to darkness or obscuration 
#buf1 N from Nddff
#buf2 8Nclcmch
'''
def cldtype(buf1,buf2):
    '''
    '''
    #print(buf1,buf2)
    if buf1 == '0':
     return 7
    elif buf1 == '8':
     return 0
    elif buf1 > '0' and buf2[0] != '8':
     return 0
    elif buf2[0] == '8':
     if buf2[2] != '0'and buf2[3] != '0' and buf2[4] != '0':
      return 6
     elif buf2[2] == '0'and buf2[3] == '0' and buf2[4] != '0':
      return 5
     elif buf2[2] == '0'and buf2[3] != '0' and buf2[4] != '0':
      return 4
     elif buf2[2] == '0'and buf2[3] != '0' and buf2[4] == '0':
      return 3
     elif buf2[2] != '0'and buf2[3] == '0' and buf2[4] != '0':
      return 2
     elif buf2[2] != '0'and buf2[3] != '0' and buf2[4] == '0':
      return 1
     elif buf2[2] != '0'and buf2[3] == '0' and buf2[4] == '0':
      return 0
     elif buf2[2] == '0'and buf2[3] == '0' and buf2[4] == '0':
      return 7
    
import urllib.request
fl = open("obs_india.csv",'w')
gt = {}
coun = ['India']
rep = '' 
for item in coun:
 #urltxt = "https://www.ogimet.com/display_synopsc2.php?lang=en&estado="+item+"&tipo=ALL&ord=REV&nil=NO&fmt=txt&ano=2022&mes=07&day=07&hora=03&anof=2022&mesf=07&dayf=07&horaf=03&send=send"
 #print(urltxt)
 f1 = urllib.request.urlopen("https://www.ogimet.com/display_synopsc2.php?lang=en&estado="+item+"&tipo=ALL&ord=REV&nil=NO&fmt=txt&ano=2022&mes=07&day=07&hora=03&anof=2022&mesf=07&dayf=07&horaf=03&send=send")
 txt1 = f1.read()
 syn = txt1.split(b'\n')
 for item in syn:
  #print(item)
  txt = item.decode('utf-8')
  if txt[:2] == '# ':
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
    gt[idx] =[name,lat,lon]
  elif txt[:4] == '2022':
   rep = txt
   gt[idx].append(rep)
#print(gt)
f1.close()
keylist = gt.keys()
sorted(keylist)
for key in keylist:
 #print(gt[key])
 name = gt[key][0]
 lat = gt[key][1]
 lon = gt[key][2]
 buf = gt[key][3]
 buflist = buf.split()
 #print(key,name,lat,lon,len(buflist))
 #print(buflist)
 if len(buflist) > 5:
  buf1 = buflist[5][0]
  buf2 = buflist[-1]
  if buf1 != '/' and len(buflist) > 7 and len(buf2) == 5:
   out = cldtype(buf1,buf2)
   #print(buf1,buf2,out,buflist)
   #fl.write(str(key)+','+name+','+str(lat)+','+str(lon)+','+str(out)+'\n')
   print(key,name,lat,lon,buflist)

