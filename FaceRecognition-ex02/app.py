#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import cv2

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = os.getcwd()

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


@app.route('/', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
			test = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename), 0)
            
			prediction_eigenface = model_eigenface.predict(test)
			prediction_fisherface = model_fisherface.predict(test)
			prediction_lbphface = model_lbphface.predict(test)
            
			return render_template('result.html', 
				result_eigenface=names[prediction_eigenface[0]], 
				result_fisherface=names[prediction_fisherface[0]], 
				result_lbphface=names[prediction_lbphface[0]]
			)

	return render_template('upload.html')


if __name__ == '__main__':
	app.run()
