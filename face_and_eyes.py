#importing libreraies
import cv2
import imageio

#loading cascading
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')



#defining function for detecting faces and eyes
def detect(gray,frame):
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x-200,y-100),(int(x+w),int(y+h)),(255,0,0),2)
        #roi_gray=gray[x:x+w,y:y+h]
        #roi_color=frame[x:x+w,y:y+h]
        #eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
        #for(ex,ey,ew,eh) in eyes:
           # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame


#using web cam

    
video_capture=cv2.VideoCapture(0)
while True:
    _,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('video',canvas)
    
    if(cv2.waitKey(1)&0xff==ord('q')):
        break
video_capture.release()
cv2.destroyAllWindows()
    
    
    
            
    
