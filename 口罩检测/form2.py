# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/10/30 15:50
Ⱥ��970353786
"""
#�����������������
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)

        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(0, 240, 1000, 560))
        self.label5.setObjectName("label5")
        self.label5.setStyleSheet(
            '''QLabel{background:#76789E}''')


        '''tableView���'''
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(180, 290, 820, 510))
        self.tableView.setObjectName("tableView")
        # �������ݲ�νṹ����ָ��n��n��,����(n,n)����
        self.model = QtGui.QStandardItemModel()
        # ����ˮƽ���������ͷ��ǩ�ı�����
        self.model.setHorizontalHeaderLabels(['����', 'ѧ��', 'ѧԺ', '����������','����'])
        self.tableView.setModel(self.model)
        # ˮƽ�����ǩ��չʣ�µĴ��ڲ��֣��������
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #���tableView����ʽ
        self.tableView.setStyleSheet(
            '''QTableView{
                    border:1px solid #74E9FF;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.tableView.horizontalHeader().setStyleSheet("QHeaderView::section{background:#87C9FF;}")#���ñ�ͷ��ɫ
        self.tableView.horizontalHeader().setSectionsClickable(False)#���ñ�ͷ���ɱ����
        self.tableView.verticalHeader().setSectionsClickable(False)#���ñ�ͷ���ɱ����
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)#���ò��ɱ༭
        #��ʼ��ʱ���һ������
        self.model.appendRow([
            QtGui.QStandardItem('��xx'),
            QtGui.QStandardItem('U2018XXXXX'),
            QtGui.QStandardItem('�˹��������Զ���ѧԺ'),
            QtGui.QStandardItem('δ������'),
            QtGui.QStandardItem(time.strftime('%Y.%m.%d', time.localtime(time.time()))),
        ])
        '''tableView��ƽ���'''



        '''LineEdit��������'''
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(40, 430, 100, 28))
        self.name.setObjectName("name")
        self.name.setPlaceholderText("��������")

        self.ID = QtWidgets.QLineEdit(Form)
        self.ID.setGeometry(QtCore.QRect(40, 490, 100, 28))
        self.ID.setObjectName("ID")
        self.ID.setPlaceholderText("����ѧ��")

        self.xueyuan = QtWidgets.QLineEdit(Form)
        self.xueyuan.setGeometry(QtCore.QRect(40, 550, 100, 28))
        self.xueyuan.setObjectName("xueyuan")
        self.xueyuan.setPlaceholderText("����ѧԺ")

        self.name.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.ID.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.xueyuan.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        '''LineEdit�������ƽ���'''

        '''QLabel���'''
        self.labelplay = QtWidgets.QLabel(Form)
        self.labelplay.setGeometry(QtCore.QRect(0, 0, 320, 240))
        self.labelplay.setObjectName("labelplay")
        self.labeldete = QtWidgets.QLabel(Form)
        self.labeldete.setGeometry(QtCore.QRect(680, 0, 320, 240))
        self.labeldete.setObjectName("labeldete")

        self.labelname = QtWidgets.QLabel(Form)
        self.labelname.setGeometry(QtCore.QRect(5, 430, 30, 28))
        self.labelname.setObjectName("labelname")
        self.labelid = QtWidgets.QLabel(Form)
        self.labelid.setGeometry(QtCore.QRect(5, 490, 30, 28))
        self.labelid.setObjectName("labelid")
        self.labelxy = QtWidgets.QLabel(Form)
        self.labelxy.setGeometry(QtCore.QRect(5, 550, 30, 28))
        self.labelxy.setObjectName("labelxueyuan")

        self.labelinfo = QtWidgets.QLabel(Form)
        self.labelinfo.setGeometry(QtCore.QRect(180, 260, 300, 28))
        self.labelinfo.setObjectName("labelinfo")




        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)

        self.labelpaddle = QtWidgets.QLabel(Form)
        self.labelpaddle.setGeometry(QtCore.QRect(320, 0, 360, 240))
        self.labelpaddle.setObjectName("labelpaddle")

        self.labell = QtWidgets.QLabel(Form)
        self.labell.setGeometry(QtCore.QRect(320, 0, 180, 30))
        self.labell.setObjectName("labell")
        self.labelr = QtWidgets.QLabel(Form)
        self.labelr.setGeometry(QtCore.QRect(500, 0, 180, 30))
        self.labelr.setObjectName("labell")


        self.labell.setFont(font)
        self.labelr.setFont(font)
        self.labell.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)       #�ı���ʾλ��
        self.labelr.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing) #�ı���ʾλ��

        self.labelplay.setStyleSheet(
            '''QLabel{
                    border:1px solid red;
            }''')
        self.labeldete.setStyleSheet(
            '''QLabel{
                    border:1px solid red;
            }''')
        self.labelpaddle.setStyleSheet(
            '''QLabel{
                    border:1px solid #E8B735;
            }''')
        self.labell.setStyleSheet("color:white")#����������ɫ
        self.labelr.setStyleSheet("color:white")#����������ɫ

        '''QLabel��ƽ���'''


        '''Button���'''
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.play = QtWidgets.QPushButton(Form)
        self.play.setGeometry(QtCore.QRect(10, 260, 100, 28))
        self.play.setObjectName("play")
        self.dete = QtWidgets.QPushButton(Form)
        self.dete.setGeometry(QtCore.QRect(10, 310, 100, 28))
        self.dete.setObjectName("dete")
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(10, 360, 100, 28))
        self.quit.setObjectName("quit")
        self.daochu = QtWidgets.QPushButton(Form)
        self.daochu.setGeometry(QtCore.QRect(5, 650, 150, 28))
        self.daochu.setObjectName("daochu")

        self.play.setFont(font)
        self.dete.setFont(font)
        self.quit.setFont(font)
        #self.daochu.setFont(font)

        self.play.setStyleSheet(
            '''QPushButton{background:#87C9FF;border-radius:5px;}QPushButton:hover{background:blue;}''')
        self.dete.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.quit.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.daochu.setStyleSheet(
            '''QPushButton{background:#F4605F;border-radius:5px;}QPushButton:hover{background:red;}''')

        self.retranslateUi(Form)
        self.play.clicked.connect(Form.shoot_play)
        self.dete.clicked.connect(Form.frame_detect)
        self.quit.clicked.connect(Form.detect_quit)
        self.daochu.clicked.connect(Form.getinfo)
        QtCore.QMetaObject.connectSlotsByName(Form)
        '''Button��ƽ���'''

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ѧ�����ּ��Ǽ�ϵͳ(����PaddleHub�Ŀ��ּ��ϵͳ)"))
        self.labelplay.setText(_translate("Form", "TextLabel"))
        self.labeldete.setText(_translate("Form", "TextLabel"))
        self.labell.setText(_translate("Form", "������"))
        self.labelr.setText(_translate("Form", "�����"))
        self.labelname.setText(_translate("Form", "����"))
        self.labelid.setText(_translate("Form", "ѧ��"))
        self.labelxy.setText(_translate("Form", "ѧԺ"))
        self.labelinfo.setText(_translate("Form", "ѧ��������������¼:"))
        self.labelpaddle.setText(_translate("Form", "paddle"))
        self.play.setText(_translate("Form", "��������"))
        self.dete.setText(_translate("Form", "������"))
        self.quit.setText(_translate("Form", "�������"))
        self.daochu.setText(_translate("Form", "���������Ϣ��"))