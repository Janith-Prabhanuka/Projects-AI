#Project

!pip install facial-emotion-recognition
import cv2 
import tensorflow 

from facial_emotion_recognition import EmotionRecognition # This should work now that the package is installed

er = EmotionRecognition(device='cpu')

cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    frame = er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
