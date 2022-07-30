import cv2
import os

cacsPath = os.path.dirname(cv2.__file__)+'/data/haarcascade_frontalface_default.xml'
cacsPath1 = os.path.dirname(cv2.__file__)+'/data/haarcascade_eye.xml'
def detect():
    face_cascade =cv2.CascadeClassifier(cacsPath)
    eye_cascade =cv2.CascadeClassifier(cacsPath1)
    camera = cv2.VideoCapture(0)
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            center_coordinates = x + w // 2, y + h // 2
            img = cv2.circle(frame,center_coordinates,200,(0,255,0),2)
            'img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)'
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xff == 113:
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    detect()        
