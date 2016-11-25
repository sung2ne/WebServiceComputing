#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import cv2
import base64

from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = os.getcwd()

@app.route('/')
def index():

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

    # 이미지를 base64로 인코딩
    _, data = cv2.imencode('.png', img)
    data_uri = base64.b64encode(data.tostring())
    print(data_uri)

    return render_template('index.html', data_uri=data_uri.decode('utf-8'))


if __name__ == '__main__':
    app.run()
