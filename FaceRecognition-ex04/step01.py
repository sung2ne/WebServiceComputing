#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import cv2

# 얼굴 검출에 사용할 haar-cascade 파일
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 얼굴 이미지가 있는 디렉터리
face_dir = "original"

for (subdirs, dirs, files) in os.walk(face_dir):
    for subdir in dirs:
        print "\n현재 디렉터리:", subdir

        # 디렉터리 생성
        if not os.path.isdir("crop/" + subdir):
            os.mkdir("crop/" + subdir)

        img_path = os.path.join(face_dir, subdir)
        for filename in os.listdir(img_path):
            path = img_path + '/' + filename
            #print "현재 파일:", path

            # grayscale로 이미지 읽어오기
            img_original = cv2.imread(path, 0)

            # 이미지 보여주기
            #cv2.imshow("face", img_original)

            # 얼굴 검출
            faces = face_cascade.detectMultiScale(img_original, 1.3, 4);

            # 검출한 얼굴이 하나일때만 보여주기
            if len(faces) == 1:
                print path, "- 검출 완료(O)"

                # 얼굴에 테두리 그리기
                (x, y, w, h) = faces[0]
                cv2.rectangle(img_original, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # 검출한 이미지 보여주기
                #cv2.imshow("face", img_original)

                # 얼굴 부분만 자르기
                img_crop = img_original[y:y+h, x:x+w]

                # 얼굴 부분 보여주기
                #cv2.imshow("face", img_crop)

                # 이미지 크기 조절
                dim = (128, 128)
                img_resize = cv2.resize(img_crop, dim)

                # 크기 조절된 이미지 보여주기
                #cv2.imshow("face", img_resize)

                # 얼굴 부분 저장
                cv2.imwrite("crop/" + subdir + "/" + filename, img_resize)

                # 키 입력을 기다림
                #cv2.waitKey(0)
            else:
                print path, "- 검출 안됨(X)"

# 프로그램 종료
cv2.destroyAllWindows()
