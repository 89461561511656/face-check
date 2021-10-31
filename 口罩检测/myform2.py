# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/10/30 15:52
Ⱥ��970353786
"""
#��Ƶ���ϵͳ�߼��������
from form2 import Ui_Form
import numpy
import cv2
import csv
import sys, time
from detection import Mask_detect
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyDesiger(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)
        self.star_show()
        self.info = [["����","ѧ��","ѧԺ","����������","����"]]
        self.VideoTimer = Video()
        self.VideoTimer.changePixmap.connect(self.setImage)   #�ź���ۺ�������
        self.VideoTimer.detectPixmap.connect(self.setDetect)  #�ź���ۺ�������
        self.VideoTimer.run_over.connect(self.finish_detect)  #�ź���ۺ�������
        self.VideoTimer.update_data.connect(self.add_data)    #�ź���ۺ�������

    def shoot_play(self):#����ͷչʾ
        if self.name.text()=='' or self.ID.text()=='' or self.xueyuan.text()=='':#ѧ����Ϣ��д���������޷���ʼ���
            QMessageBox.information(self, '��Ϣ������', '����ȷ��д������Ϣ',QMessageBox.Yes)
        else:
            self.VideoTimer.working = True  # ʹ����ͼ���߳��ܹ���
            self.VideoTimer.start()

    def frame_detect(self):#���ÿһ֡
        if self.VideoTimer.working:
            self.VideoTimer.setDetect()

    def detect_quit(self):#�������
        self.close()

    def getinfo(self):#�����������Ǽ��ļ�
        with open('resource\\info.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.info:
                writer.writerow(row)
        QMessageBox.information(self, '�����ɹ�', '�ļ�����·��Ϊ:resource\\info.csv', QMessageBox.Yes)

    def star_show(self):#��ʼ����ʾ����
        frame = QPixmap('resource\\sample.jpg').scaled(self.labelplay.width(), self.labelplay.height())
        self.labelplay.setPixmap(frame)#��ʾʾ��ͼƬ
        image = QPixmap('resource\\sample_detection.jpg').scaled(self.labeldete.width(), self.labeldete.height())
        self.labeldete.setPixmap(image)#��ʾʾ��ͼƬ
        paddlehub = QPixmap('resource\\paddlehub.png').scaled(self.labelpaddle.width(), self.labelpaddle.height())
        self.labelpaddle.setPixmap(paddlehub)#��ʾʾ��ͼƬ

    def finish_detect(self,kz):#�����ϣ������������Ϣ��ʾ
        self.star_show()
        QMessageBox.information(self, '�����:', kz+'!!', QMessageBox.Yes)
        self.name.clear()
        self.ID.clear()
        self.xueyuan.clear()

    def add_data(self,kz):#�����ϣ���¼����Ϣ����
        self.model.appendRow([
            QStandardItem(self.name.text()),
            QStandardItem(self.ID.text()),
            QStandardItem(self.xueyuan.text()),
            QStandardItem(kz),
            QStandardItem(time.strftime('%Y.%m.%d',time.localtime(time.time()))),
        ])
        self.info.append([self.name.text(), self.ID.text(), self.xueyuan.text(),kz,time.strftime('%Y.%m.%d',time.localtime(time.time()))])

    def setImage(self, frame):   #��������ͷͼ��
        self.labelplay.setPixmap(QPixmap.fromImage(QImage(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),640/2,480/2,13)))

    def setDetect(self, image):  #���ͼ�����ͼ��
        self.labeldete.setPixmap(QPixmap.fromImage(QImage(cv2.cvtColor(image, cv2.COLOR_BGR2RGB),640/2,480/2,13)))

class Video(QThread):
    changePixmap = pyqtSignal(numpy.ndarray)  #��������ͷͼ�񴥷��ź�
    detectPixmap = pyqtSignal(numpy.ndarray)  #���ü��ͼ�񴥷��ź�
    update_data = pyqtSignal(str)             #������Ϣ�����ź�
    run_over = pyqtSignal(str)                #���ü������ź�
    def __init__(self):
        QThread.__init__(self)
        self.detect = False   #�Ƿ��ܼ��
        self.working = False  #�Ƿ��ܹ���
        self.count = 0        #��⵽�����Ĵ���

    def run(self):
        cap = cv2.VideoCapture(0)  #������ͷ
        while self.working:        #ѭ����ȡͼ��
            ret, frame = cap.read()
            frame = cv2.resize(frame,(320,240))
            self.changePixmap.emit(frame)  #��ʾͼ��
            if self.detect:
                img = frame.copy()
                detected_image,num,kz=Mask_detect(img)#���ּ��
                self.detectPixmap.emit(detected_image)#��ʾ���ּ����
                if num > 0:
                    self.count += 1
            if self.count >= 6:#����6֡��⵽������ֹͣ���
                self.detect = False
                self.working = False
                self.count = 0  #��������
                self.run_over.emit(kz)#����������ź�
                self.update_data.emit(kz)#������Ϣ�����ź�
        cap.release()#�ͷ�����ͷ��Դ

    def setDetect(self):
        self.detect = True
    def setquit(self):
        self.detect = False
        self.working = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyDesiger()
    ui.show()
    sys.exit(app.exec_())
