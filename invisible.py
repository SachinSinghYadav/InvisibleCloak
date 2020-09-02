import cv2
import numpy as np
background=cv2.imread("background.jpg")
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,current=cam.read()
    if ret:
        hsv=cv2.cvtColor(current,cv2.COLOR_BGR2HSV)
        low_red=np.array([110,50,50])
        high_red=np.array([130,255,255])
        mask1=cv2.inRange(hsv,low_red,high_red)
       # low_red=np.array([170,120,70])
       # high_red=np.array([180,255,255])
        #mask2=cv2.inRange(hsv,low_red,high_red)
       # mask1=mask1+mask2
        mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
        mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
        mask2=cv2.bitwise_not(mask1)
        res1=cv2.bitwise_and(current,current,mask=mask2)
        res2=cv2.bitwise_and(background,background,mask=mask1)
        cv2.imshow("s",res1+res2)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()