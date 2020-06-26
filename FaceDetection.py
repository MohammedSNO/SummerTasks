import cv2



Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Vid=cv2.VideoCapture(0)

while 1:
    success,image=Vid.read()
    GrayFaces = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    DetectedFaces = Cascade.detectMultiScale(GrayFaces, 1.1, 4)

    for (x, y, w, h) in DetectedFaces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (240, 0, 0), 3)

    cv2.imshow("Output", image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break







