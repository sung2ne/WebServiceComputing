#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cv2

# 얼굴 검출에 사용할 haar-cascade파일
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 이미지를 읽어와서 흑백으로 변환
img = cv2.imread('lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray, 1.5, 3)

# 검출한 얼굴에 파란색 테두리 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 얼굴 검출 이미지 보여주기
cv2.imshow("Faces found" ,img)

# 키 입력을 기다림
cv2.waitKey(0)

# 프로그램 종료
cv2.destroyAllWindows()
