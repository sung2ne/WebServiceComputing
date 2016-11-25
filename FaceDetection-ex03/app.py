#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import cv2
import base64
import imghdr

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = os.getcwd()

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # 얼굴 검출에 사용할 haar-cascade파일
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            # 이미지를 읽어와서 흑백으로 변환
            img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 얼굴 검출
            faces = face_cascade.detectMultiScale(gray, 1.1, 2)

            # 검출한 얼굴에 파란색 테두리 그리기
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 이미지 파일 타입
            filetype = imghdr.what(filename)
            #print "filetype:", filetype

            if filetype == 'png':
                # 이미지를 base64로 인코딩
                _, data = cv2.imencode('.png', img)
                data_uri = 'data:image/png;base64,' + base64.b64encode(data.tostring())

            elif filetype == 'jpeg':
                # 이미지를 base64로 인코딩
                _, data = cv2.imencode('.jpg', img)
                data_uri = 'data:image/jpeg;base64,' + base64.b64encode(data.tostring())

            elif filetype == 'pgm':
                # 이미지를 base64로 인코딩
                _, data = cv2.imencode('.pgm', img)
                data_uri = 'data:image/pgm;base64,' + base64.b64encode(data.tostring())

            elif filetype == 'bmp':
                # 이미지를 base64로 인코딩
                _, data = cv2.imencode('.bmp', img)
                data_uri = 'data:image/bmp;base64,' + base64.b64encode(data.tostring())

        return render_template('result.html', data_uri=data_uri)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
