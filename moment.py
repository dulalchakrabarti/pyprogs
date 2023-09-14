import cv2
import sys
import numpy as np

if len(sys.argv)!=3:                  ## Check for error in usage syntax
    print "Usage : python moment.py <image_file1> <image_file2>"

else:
    img1 = cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_COLOR)  ## Read image1 file
    img2 = cv2.imread(sys.argv[2],cv2.CV_LOAD_IMAGE_COLOR)  ## Read image2 file

    if (img1 == None or img2 == None):                      ## Check for invalid input
        print "Could not open or find the image files"
    else:
        imgray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        imgray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        ret1,thresh1 = cv2.threshold(imgray1,160,240,0)
        ret2,thresh2 = cv2.threshold(imgray2,160,240,0)
        contours1, hierarchy1 = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        temp = []
        print len(contours1)
        print type(contours1)
        contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        print len(contours2)
        for i in range(len(contours1)):
         cont1 = contours1[i]
         x1,y1,w1,h1 = cv2.boundingRect(cont1)
         ar1 = float(w1)/h1
         area1 = cv2.contourArea(cont1)
         perimeter1 = cv2.arcLength(cont1,True)
         for j in range(len(contours2)):
          cont2 = contours2[j]
          x2,y2,w2,h2 = cv2.boundingRect(cont2)
          ar2 = float(w2)/h2
          area2 = cv2.contourArea(cont2)
          perimeter2 = cv2.arcLength(cont2,True)
          if ar1 == ar2 or perimeter1 == perimeter2 or area1 == area2:
           temp.append(cont1)
           break
        print len(temp)
        print type(contours1)
        for i in range(len(temp)):
         cont1 = temp[i]
         x1,y1,w1,h1 = cv2.boundingRect(cont1)
         ar1 = float(w1)/h1
         area1 = cv2.contourArea(cont1)
         perimeter1 = cv2.arcLength(cont1,True)
         for j in range(len(contours1)):
          cont2 = contours1[j]
          x2,y2,w2,h2 = cv2.boundingRect(cont2)
          ar2 = float(w2)/h2
          area2 = cv2.contourArea(cont2)
          perimeter2 = cv2.arcLength(cont2,True)
          if ar1 == ar2 or perimeter1 == perimeter2 or area1 == area2:
           del contours1[j]
           break
        print len(contours1)
        print type(contours1)
        mask = np.zeros(img1.shape,np.uint8)
        for i in range(len(contours1)):
         M = cv2.moments(contours1[i])
         if int(M['m00']) != 0.0:
          x = int(M['m10']/M['m00'])
          y = int(M['m01']/M['m00'])
          cv2.putText(img1, str(i), (x, y),cv2.FONT_HERSHEY_PLAIN, 2.0, (0,0,255),2)
          cv2.drawContours(mask,[contours1[i]],0,255,-1)
          maskc = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
          mean = cv2.mean(img1,mask = maskc)
          print mean
          #cv2.drawContours(img1,[contours1[i]],0,(0,255,0),2)
          cv2.namedWindow('Display Window')        ## create window for display
          im = cv2.resize(mask, (img1.shape[1]/2, img1.shape[0]/2 ))
          #im = cv2.resize(img1, (img1.shape[1]/2, img1.shape[0]/2 ))
          cv2.imshow('Display Window',im)         ## Show image in the window
          cv2.waitKey(0)                           ## Wait for keystroke
          cv2.destroyAllWindows()                  ## Destroy all windows


