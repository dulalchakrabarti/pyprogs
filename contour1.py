import cv2
import sys
import numpy as np

if len(sys.argv)!=2:                  ## Check for error in usage syntax
    print "Usage : python display_image.py <image_file>"

else:
    img = cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file

    if (img == None):                      ## Check for invalid input
        print "Could not open or find the image"
    else:
        imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,100,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #for h,cnt in enumerate(contours):
        cv2.drawContours(img,contours,-1,(0,255,0),2)
        cv2.namedWindow('Display Window')        ## create window for display
        im = cv2.resize(img, (img.shape[1] / 2, img.shape[0] / 2))
        cv2.imshow('Display Window',im)         ## Show image in the window
        cv2.waitKey(0)                           ## Wait for keystroke
        cv2.destroyAllWindows()                  ## Destroy all windows

