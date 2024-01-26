# pyinstaller -w -F Change.py
# C:\Users\hckim\PycharmProjects\pythonProject1\dist
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from glob import glob
from PIL import Image
import os
import glob
import os.path
import cv2 # opencv 모듈 pip install opencv-python
import numpy as np
import matplotlib.pyplot as plt

abs_path = os.path.dirname(os.path.abspath('__file__'))

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ren_group
        self.ren_group = QGroupBox('JPEG->JPG')
        self.ren_label = QLabel('소스폴더:')
        self.ren_le = QLineEdit()
        self.ren_le.setPlaceholderText('c:\\이미지')
        self.ren_le.setFocus()
        self.ren_btn = QPushButton('&실행')
        self.ren_btn.clicked.connect(self.ren_btn_click)

        # chg_group
        self.chg_group = QGroupBox('PNG->JPG')
        self.chg_label = QLabel('소스폴더:')
        self.chg_le = QLineEdit()
        self.chg_le.setPlaceholderText('c:\\이미지')
        self.chg_le.setFocus()
        self.chg_btn = QPushButton('&실행')
        self.chg_btn.clicked.connect(self.chg_btn_click)

        # cut_group
        self.cut_group = QGroupBox('JPG자르기')
        self.cut_label = QLabel('소스폴더:')
        self.cut_le = QLineEdit()
        self.cut_le.setPlaceholderText('c:\\이미지')
        self.cut_le.setFocus()
        self.cut_label2 = QLabel('대상폴더:')
        self.cut_le2 = QLineEdit()
        self.cut_le2.setPlaceholderText('c:\\이미지')
        self.cut_btn = QPushButton('&실행')
        self.cut_btn.clicked.connect(self.cut_btn_click)

        # num_group
        self.num_group = QGroupBox('파일명 변경')
        self.num_label = QLabel('소스폴더:')
        self.num_le = QLineEdit()
        self.num_le.setPlaceholderText('c:\\이미지')
        self.num_le.setFocus()
        self.num_btn = QPushButton('&실행')
        self.num_btn.clicked.connect(self.num_btn_click)

        # cut2_group
        self.cut2_group = QGroupBox('JPG오리기')
        self.cut2_label = QLabel('소스폴더:')
        self.cut2_le = QLineEdit()
        self.cut2_le.setPlaceholderText('c:\\이미지')
        self.cut2_le.setFocus()
        self.cut2_label2 = QLabel('대상폴더:')
        self.cut2_le2 = QLineEdit()
        self.cut2_le2.setPlaceholderText('c:\\이미지')

        self.cut2_label_sh = QLabel('시작 Height:')
        self.cut2_le_sh = QLineEdit()
        self.cut2_label_sw = QLabel('시작 Width :')
        self.cut2_le_sw = QLineEdit()

        self.cut2_label_eh = QLabel('끝   Height:')
        self.cut2_le_eh = QLineEdit()
        self.cut2_label_ew = QLabel('끝   Width :')
        self.cut2_le_ew = QLineEdit()

        self.cut2_btn = QPushButton('&실행')
        self.cut2_btn.clicked.connect(self.cut2_btn_click)

        # ren_layout
        self.ren_layout = QGridLayout()
        self.ren_layout.addWidget(self.ren_label, 0, 0)
        self.ren_layout.addWidget(self.ren_le, 0, 1)
        self.ren_layout.addWidget(self.ren_btn, 1, 0, 1, 2)
        self.ren_group.setLayout(self.ren_layout)

        # chg_layout
        self.chg_layout = QGridLayout()
        self.chg_layout.addWidget(self.chg_label, 0, 0)
        self.chg_layout.addWidget(self.chg_le, 0, 1)
        self.chg_layout.addWidget(self.chg_btn, 1, 0, 1, 2)
        self.chg_group.setLayout(self.chg_layout)

        # cut_layout
        self.cut_layout = QGridLayout()
        self.cut_layout.addWidget(self.cut_label, 0, 0)
        self.cut_layout.addWidget(self.cut_le, 0, 1)
        self.cut_layout.addWidget(self.cut_label2, 1, 0)
        self.cut_layout.addWidget(self.cut_le2, 1, 1)
        self.cut_layout.addWidget(self.cut_btn, 2, 0, 1, 2)
        self.cut_group.setLayout(self.cut_layout)

        # num_layout
        self.num_layout = QGridLayout()
        self.num_layout.addWidget(self.num_label, 0, 0)
        self.num_layout.addWidget(self.num_le, 0, 1)
        self.num_layout.addWidget(self.num_btn, 1, 0, 1, 2)
        self.num_group.setLayout(self.num_layout)

        # cut2_layout
        self.cut2_layout = QGridLayout()
        self.cut2_layout.addWidget(self.cut2_label, 0, 0)
        self.cut2_layout.addWidget(self.cut2_le, 0, 1)
        self.cut2_layout.addWidget(self.cut2_label2, 1, 0)
        self.cut2_layout.addWidget(self.cut2_le2, 1, 1)

        self.cut2_layout.addWidget(self.cut2_label_sh, 2, 0)
        self.cut2_layout.addWidget(self.cut2_le_sh, 2, 1)
        self.cut2_layout.addWidget(self.cut2_label_eh, 3, 0)
        self.cut2_layout.addWidget(self.cut2_le_eh, 3, 1)
        self.cut2_layout.addWidget(self.cut2_label_sw, 4, 0)
        self.cut2_layout.addWidget(self.cut2_le_sw, 4, 1)
        self.cut2_layout.addWidget(self.cut2_label_ew, 5, 0)
        self.cut2_layout.addWidget(self.cut2_le_ew, 5, 1)

        self.cut2_layout.addWidget(self.cut2_btn, 6, 0, 1, 2)
        self.cut2_group.setLayout(self.cut2_layout)

        # layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.ren_group, 0, 0)
        self.layout.addWidget(self.chg_group, 0, 1)
        self.layout.addWidget(self.cut_group, 1, 0)
        self.layout.addWidget(self.num_group, 1, 1)
        self.layout.addWidget(self.cut2_group, 2, 0)
        self.setLayout(self.layout)

        self.setWindowTitle('파일변환')
        self.show()

    def ren_btn_click(self):
        fpath = self.ren_le.text() + '\\*.jpeg'
        files = glob.glob(fpath)
        for x in files:
            if not os.path.isdir(x):
                #filename = os.path.splitext(x)
                #os.rename(x, filename[0] + '.jpg')

                f_pt = os.path.dirname(x)
                f_nm = os.path.splitext(os.path.basename(x))
                f_ln = len(f_nm[0])
                if f_ln == 1:
                    n_nm = "00"+f_nm[0]
                elif f_ln == 2:
                    n_nm = "0" + f_nm[0]
                else:
                    n_nm = f_nm[0]
                os.rename(x, f_pt + '\\' + n_nm + '.jpg')

    def chg_btn_click(self):
        fpath = self.chg_le.text() + '\\*.png'
        files = glob.glob(fpath)
        for x in files:
            if not os.path.isdir(x):
                im = Image.open(x)
                rgb_im = im.convert('RGB')
                #rgb_im.save(x.split('.')[0]+".jpg")

                f_pt = os.path.dirname(x)
                f_nm = os.path.splitext(os.path.basename(x))
                f_ln = len(f_nm[0])
                if f_ln == 1:
                    n_nm = "00"+f_nm[0]
                elif f_ln == 2:
                    n_nm = "0" + f_nm[0]
                else:
                    n_nm = f_nm[0]
                rgb_im.save(f_pt + '\\' + n_nm + ".jpg")

    def cut_btn_click(self):
        fpath = self.cut_le.text() + '\\*.jpg'
        fpath2 = self.cut_le2.text()
        files = glob.glob(fpath)
        for x in files:
            if not os.path.isdir(x):
                # 이미지 읽기
                #im = cv2.imread(x)
                # imread 한글경로 인식문제
                with open(x, 'rb') as stream:
                    bytes = bytearray(stream.read())
                    numpyarray = np.asarray(bytes, dtype=np.uint8)
                    im = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

                # 이미지 정보
                h, w, c = im.shape
                # 이미지 자르기
                im = im.copy()
                im_1 = im[int(h*0.0):int(h*1.0), int(w*0.0):int(w*0.5)]  # [시작 height : 끝 height, 시작 width : 끝 width]
                im_2 = im[int(h*0.0):int(h*1.0), int(w*0.5):int(w*1.0)]  # [시작 height : 끝 height, 시작 width : 끝 width]

                plt.imshow(cv2.cvtColor(im_1, cv2.COLOR_BGR2RGB))
                plt.imshow(cv2.cvtColor(im_2, cv2.COLOR_BGR2RGB))

                # 이미지 저장
                f_pt = os.path.dirname(x)
                f_nm = os.path.splitext(os.path.basename(x))

                # 좌측 이미지 저장
                result_path = fpath2 + '\\' + f_nm[0] + "_1" + ".jpg"
                # 한글경로 인식문제
                #cv2.imwrite(result_path, im_1)  # 파일로 저장, 포맷은 확장자에 따름
                retval, buffer = cv2.imencode('.jpg', im_1)
                if (retval):
                    with open(result_path, 'wb') as f_write:
                        f_write.write(buffer)

                # 우측 이미지 저장
                result_path = fpath2 + '\\' + f_nm[0] + "_2" + ".jpg"
                #cv2.imwrite(result_path, im_2)  # 파일로 저장, 포맷은 확장자에 따름
                # 한글경로 인식문제
                retval, buffer = cv2.imencode('.jpg', im_2)
                if (retval):
                    with open(result_path, 'wb') as f_write:
                        f_write.write(buffer)

    def num_btn_click(self):
        fpath = self.num_le.text() + '\\*.*'
        files = glob.glob(fpath)
        idx = 0
        for x in files:
            if not os.path.isdir(x):
                f_pt = os.path.dirname(x)
                f_nm = os.path.splitext(os.path.basename(x))
                idx = idx + 1;
                n_nm = str(idx).rjust(3, '0')
                os.rename(x, f_pt + '\\' + n_nm + f_nm[1])

    def cut_btn_click(self):
        fpath = self.cut_le.text() + '\\*.jpg'
        fpath2 = self.cut_le2.text()
        files = glob.glob(fpath)
        for x in files:
            if not os.path.isdir(x):
                # 이미지 읽기
                #im = cv2.imread(x)
                # imread 한글경로 인식문제
                with open(x, 'rb') as stream:
                    bytes = bytearray(stream.read())
                    numpyarray = np.asarray(bytes, dtype=np.uint8)
                    im = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

                # 이미지 정보
                h, w, c = im.shape
                # 이미지 자르기
                im = im.copy()
                im_1 = im[int(h*0.0):int(h*1.0), int(w*0.0):int(w*0.5)]  # [시작 height : 끝 height, 시작 width : 끝 width]

                plt.imshow(cv2.cvtColor(im_1, cv2.COLOR_BGR2RGB))

                # 이미지 저장
                f_pt = os.path.dirname(x)
                f_nm = os.path.splitext(os.path.basename(x))

                # 이미지 저장
                result_path = fpath2 + '\\' + f_nm[0] + ".jpg"
                # 한글경로 인식문제
                #cv2.imwrite(result_path, im_1)  # 파일로 저장, 포맷은 확장자에 따름
                retval, buffer = cv2.imencode('.jpg', im_1)
                if (retval):
                    with open(result_path, 'wb') as f_write:
                        f_write.write(buffer)

    def cut2_btn_click(self):
        sh = int(self.cut2_le_sh.text())
        sw = int(self.cut2_le_sw.text())
        eh = int(self.cut2_le_eh.text())
        ew = int(self.cut2_le_ew.text())

        fpath = self.cut2_le.text() + '\\*.jpg'
        fpath2 = self.cut2_le2.text()
        files = glob.glob(fpath)
        for x in files:
            if not os.path.isdir(x):
                # 이미지 읽기
                # im = cv2.imread(x)
                # imread 한글경로 인식문제
                with open(x, 'rb') as stream:
                    bytes = bytearray(stream.read())
                    numpyarray = np.asarray(bytes, dtype=np.uint8)
                    im = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

                # 이미지 정보
                h, w, c = im.shape
                # 이미지 자르기
                im = im.copy()
                im_1 = im[int(sh):int(eh), int(sw):int(ew)]  # [시작 height : 끝 height, 시작 width : 끝 width]

                plt.imshow(cv2.cvtColor(im_1, cv2.COLOR_BGR2RGB))

                # 이미지 저장
                f_pt = os.path.dirname(x)
                f_nm = os.path.splitext(os.path.basename(x))

                # 이미지 저장
                result_path = fpath2 + '\\' + f_nm[0] + ".jpg"
                # 한글경로 인식문제
                # cv2.imwrite(result_path, im_1)  # 파일로 저장, 포맷은 확장자에 따름
                retval, buffer = cv2.imencode('.jpg', im_1)
                if (retval):
                    with open(result_path, 'wb') as f_write:
                        f_write.write(buffer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())