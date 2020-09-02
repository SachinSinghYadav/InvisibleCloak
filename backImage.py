import cv2
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,background=cam.read();
    if ret:
        cv2.imshow("Background",background)
    if(cv2.waitKey(2)==ord('q')):
        cv2.imwrite("./background.jpg",background)
        break
cam.release()
cv2.destroyAllWindows()              