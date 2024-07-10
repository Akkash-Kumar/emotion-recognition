from facial_emotion_recognition import EmotionRecognition    #import EmotionRecognition module from facial_emotion_recognition library

import cv2    #opencv library

er = EmotionRecognition(device = 'cpu')    #initialise module with device =cpu

camera = cv2.VideoCapture(0)   #primary camera initialise

while True :    #infinite loop to run camera continuously

    _ , img = camera.read()    #to read frame from camera

    img = er.recognise_emotion(img,return_type = 'BGR')   #call recognise_emotion method with return type = bgr which is color img

    cv2.imshow("Emotion",img)   #display image

    key = cv2.waitKey(10)   #wait for 10 frames

    if key ==27:          #when esc key is pressed,close camera
        break

camera.release()    #release camera

cv2.destroyAllWindows()   #close window

    
        
