import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            app = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(app))
            objCor = len(app)
            x, y, w, h = cv2.boundingRect(app)

            if objCor == 3:
                object = "Triangle"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    object = "Square"
                else:
                    object= "Rectangle"
            elif objCor > 4:
                object = "Circles"
            else:
                object = "None"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 250), 1)
            cv2.putText(imgContour, object,
                        (x + (w // 2) -30, y + (h // 2) ), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)



img = cv2.imread("Shape/Shapes.jpg")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow("OutPut",imgContour )
cv2.waitKey(0)
