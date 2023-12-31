import cv2
import numpy as np

print ''' Simple Linear Blender
------------------------------------------
Enter value of alpha [0:1] :'''

alpha = float(input())                 # Ask the value of alpha

if 0<=alpha<=1:                        # Check if 0<= alpha <=1
    beta = 1.0 - alpha                 # Calculate beta = 1 - alpha
    gamma = 0.0                        # parameter gamma = 0

    img1 = cv2.imread('lena.jpg')
    img2 = cv2.imread('res.jpg')

    if img1==None:
        print "img1 not ready"
    elif img2==None:
        print "img2 not ready"
    else:
        dst = cv2.addWeighted(img1,alpha,img2,beta,gamma)  # Get weighted sum of img1 and img2
        #dst = np.uint8(alpha*(img1)+beta*(img2))    # This is simple numpy version of above line. But cv2 function is around 2x faster
        cv2.imshow('dst',dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print "value of alpha should be 0 and 1"
