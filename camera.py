#coding=utf8
import cv2
# работа с вебкой , изображение в реальном времени

cap =cv2.VideoCapture(0)
# зададим ширину кадра в видеопотоке
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
#  зададим ывысоту кадров видеопотоке
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1480)
#
while True:
    ret, img = cap.read()
    #  преобразуем кадр в градацию серовго
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera", gray)
    #cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
       break
cap.release()
cv2.destroyAllWindows()

