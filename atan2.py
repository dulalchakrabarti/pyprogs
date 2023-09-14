
# Python3 program to demonstrate 
# the atan2() method  
  
# imports math  
import math 
  
print 'u=10,v=10 ',(270 - (math.atan2(10,10)/3.14)*180)%360
print 'u=-10,v=-10 ',(270 - (math.atan2(-10,-10)/3.14)*180)%360

