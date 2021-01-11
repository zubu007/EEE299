import cv2

img = cv2.imread('myphoto.jpeg')

webcam = cv2.VideoCapture('http://192.168.0.100:8000/mjpegfeed?640x480')

trained_data = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

while True:
    rec, frame = webcam.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = trained_data.detectMultiScale(gray_img, scaleFactor=1.1)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('lol', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()

print("code completed")

