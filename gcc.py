import math
from PIL import Image
im = Image.open("w5.jpeg","r")
pixels = list(im.getdata())
fl = open('gcc.csv','w')
fl.writelines('gcc'+','+'rcc'+','+'exg'+','+'grvi'+','+'DNR'+','+'DNG'+','+'DNB'+'\n')
for p  in  pixels:
 if sum(p) != 0 and (p[1] + p[0]) != 0:
  gcc = p[1]/float(sum(p))
  rcc = p[0]/float(sum(p))
  exg = 2*p[1] - (p[0] + p[2])
  grvi = (p[1] - p[0])/float((p[1] + p[0]))
 print round(gcc,2),round(rcc,2), round(exg,2), round(grvi,2),p[0],p[1],p[2]
 fl.writelines(str(round(gcc,2))+','+str(round(rcc,2))+','+str(round(exg,2))+','+str(round(grvi,2)) \
 +','+str(p[0])+','+str(p[1])+','+str(p[2])+'\n')
fl.close() 
