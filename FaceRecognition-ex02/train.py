#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
import cv2
import os

# 얼굴 이미지
face_dir = "att_faces"

# 모델
model_eigenface = cv2.createEigenFaceRecognizer()
model_fisherface = cv2.createFisherFaceRecognizer()
model_lbphface = cv2.createLBPHFaceRecognizer()

imgs = []
tags = []
index = 0

for (subdirs, dirs, files) in os.walk(face_dir):
    for subdir in dirs:
        img_path = os.path.join(face_dir, subdir)
        for fn in os.listdir(img_path):
            path = img_path + '/' + fn
            print("path: " + path)
            tag = index
            imgs.append(cv2.imread(path, 0))
            tags.append(int(tag))
        index += 1

(imgs, tags) = [np.array(item) for item in [imgs, tags]]

# 학습/저장
model_eigenface.train(imgs, tags)
model_eigenface.save('eigenface.xml')

model_fisherface.train(imgs, tags)
model_fisherface.save('fisherface.xml')

model_lbphface.train(imgs, tags)
model_lbphface.save('lbphface.xml')

print("Training completed successfully")
