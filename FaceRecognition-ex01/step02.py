#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cv2
import os

# 얼굴 이미지
face_dir = "att_faces"

# 모델
model_eigenface = cv2.createEigenFaceRecognizer()
model_eigenface.load("eigenface.xml")

model_fisherface = cv2.createFisherFaceRecognizer()
model_fisherface.load("fisherface.xml")

model_lbphface = cv2.createLBPHFaceRecognizer()
model_lbphface.load("lbphface.xml")

names = {}
key = 0
for (subdirs, dirs, files) in os.walk(face_dir):
    for subdir in dirs:
        #print(key, "=>", subdir)
        names[key] = subdir
        key += 1

# 테스트 이미지
img_test1 = cv2.imread("test_faces/s3-4.pgm", 0)
img_test2 = cv2.imread("test_faces/s10-5.pgm", 0)
img_test3 = cv2.imread("test_faces/s24-9.pgm", 0)
img_test4 = cv2.imread("test_faces/s37-2.pgm", 0)

# 예측 - test1
print "[s3-4.pgm - test1]"
prediction_eigenface1 = model_eigenface.predict(img_test1)
print "[eigenface] prediction:", names[prediction_eigenface1[0]], ", confidence:", prediction_eigenface1[1]
prediction_fisherface1 = model_fisherface.predict(img_test1)
print "[fisherface] prediction:", names[prediction_fisherface1[0]], ", confidence:", prediction_fisherface1[1]
prediction_lbphface1 = model_lbphface.predict(img_test1)
print "[lbphface] prediction:", names[prediction_lbphface1[0]], ", confidence:", prediction_lbphface1[1]

# 예측 - test2
print "\n[s10-5.pgm - test2]"
prediction_eigenface2 = model_eigenface.predict(img_test2)
print "[eigenface] prediction:", names[prediction_eigenface2[0]], ", confidence:", prediction_eigenface2[1]
prediction_fisherface2 = model_fisherface.predict(img_test2)
print "[fisherface] prediction:", names[prediction_fisherface2[0]], ", confidence:", prediction_fisherface2[1]
prediction_lbphface2 = model_lbphface.predict(img_test2)
print "[lbphface] prediction:", names[prediction_lbphface2[0]], ", confidence:", prediction_lbphface2[1]

# 예측 - test3
print "\n[s24-9.pgm - test3]"
prediction_eigenface3 = model_eigenface.predict(img_test3)
print "[eigenface] prediction:", names[prediction_eigenface3[0]], ", confidence:", prediction_eigenface3[1]
prediction_fisherface3 = model_fisherface.predict(img_test3)
print "[fisherface] prediction:", names[prediction_fisherface3[0]], ", confidence:", prediction_fisherface3[1]
prediction_lbphface3 = model_lbphface.predict(img_test3)
print "[lbphface] prediction:", names[prediction_lbphface3[0]], ", confidence:", prediction_lbphface3[1]

# 예측 - test4
print "\n[s37-2.pgm - test4]"
prediction_eigenface4 = model_eigenface.predict(img_test4)
print "[eigenface] prediction:", names[prediction_eigenface4[0]], ", confidence:", prediction_eigenface4[1]
prediction_fisherface4 = model_fisherface.predict(img_test4)
print "[fisherface] prediction:", names[prediction_fisherface4[0]], ", confidence:", prediction_fisherface4[1]
prediction_lbphface4 = model_lbphface.predict(img_test4)
print "[lbphface] prediction:", names[prediction_lbphface4[0]], ", confidence:", prediction_lbphface4[1]

