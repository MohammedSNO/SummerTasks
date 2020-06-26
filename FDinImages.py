import cv2

CascadeFaces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image=cv2.imread('Seinfeld.png')
imagegray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
Faces=CascadeFaces.detectMultiScale(imagegray,1.1,4)

for (x,y,w,h) in Faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,200),2)


cv2.imshow("Output",image)
cv2.waitKey(0)


