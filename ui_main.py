# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainnCGbuQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources

class DragAndDropLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(DragAndDropLineEdit, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            file_path = url.toLocalFile()
            self.setText(file_path)  # Set the file path as the QLineEdit text

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1225, 584)
        Form.setStyleSheet(u"*{\n"
"font-family : \"Malgun Gothic\";\n"
"}\n"
"\n"
"QFrame#frame, #frame_2{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame#frame{\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 10px;\n"
"}\n"
"\n"
"QFrame#frame_2{\n"
"border-bottom-left-radius : 10px;\n"
"border-bottom-right-radius : 10px;\n"
"}\n"
"\n"
"QFrame#frame_6, #frame_16{\n"
"border-top : 1px solid #e7e7e7;\n"
"background-color : transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"border-bottom : 1px solid #e7e7e7;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Malgun Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(55, 95, 245);")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(393, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_process = QPushButton(self.frame_4)
        self.btn_process.setObjectName(u"btn_process")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_process.sizePolicy().hasHeightForWidth())
        self.btn_process.setSizePolicy(sizePolicy)
        self.btn_process.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamily(u"Malgun Gothic")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setLegacyWeight(75)
        self.btn_process.setFont(font1)
        self.btn_process.setStyleSheet(u"border : none;\n"
"border-bottom : 2px solid rgb(55, 95, 245)")

        self.horizontalLayout_3.addWidget(self.btn_process)

        self.btn_mapping = QPushButton(self.frame_4)
        self.btn_mapping.setObjectName(u"btn_mapping")
        sizePolicy.setHeightForWidth(self.btn_mapping.sizePolicy().hasHeightForWidth())
        self.btn_mapping.setSizePolicy(sizePolicy)
        self.btn_mapping.setMaximumSize(QSize(150, 16777215))
        self.btn_mapping.setFont(font1)
        self.btn_mapping.setStyleSheet(u"border : none;")

        self.horizontalLayout_3.addWidget(self.btn_mapping)


        self.horizontalLayout.addWidget(self.frame_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_mini = QPushButton(self.frame_11)
        self.btn_mini.setObjectName(u"btn_mini")
        self.btn_mini.setStyleSheet(u"border : none;")
        icon = QIcon()
        icon.addFile(u":/images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mini.setIcon(icon)
        self.btn_mini.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.btn_mini)

        self.btn_close = QPushButton(self.frame_11)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setStyleSheet(u"border : none;")
        icon1 = QIcon()
        icon1.addFile(u":/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_11, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 3)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(250, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 9, -1)
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"padding-right : 10px;")
        self.label_3.setPixmap(QPixmap(u":/images/upload.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_upload = QPushButton(self.frame_12)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setMinimumSize(QSize(0, 40))
        self.btn_upload.setFont(font1)
        self.btn_upload.setStyleSheet(u"background-color: rgb(55, 95, 245);\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px 20px 20px 20px;")

        self.horizontalLayout_8.addWidget(self.btn_upload)


        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignBottom)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_4)

        self.tableWidget = QTableWidget(self.frame_10)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_6.addWidget(self.tableWidget)


        self.horizontalLayout_6.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 40))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(55, 95, 245);\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px 20px 20px 20px;")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.btn_run = QPushButton(self.frame_8)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setMinimumSize(QSize(100, 40))
        self.btn_run.setFont(font1)
        self.btn_run.setStyleSheet(u"background-color: rgb(55, 95, 245);\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px 20px 20px 20px;")

        self.horizontalLayout_5.addWidget(self.btn_run)


        self.verticalLayout_4.addWidget(self.frame_8, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_fileName = QLabel(self.frame_6)
        self.lbl_fileName.setObjectName(u"lbl_fileName")
        font2 = QFont()
        font2.setFamily(u"Malgun Gothic")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setLegacyWeight(75)
        self.lbl_fileName.setFont(font2)

        self.verticalLayout_3.addWidget(self.lbl_fileName)

        self.progressBar = QProgressBar(self.frame_6)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar::chunk{\n"
"background: qlineargradient(spread:pad, x1:1, y1:0.540273, x2:0, y2:0.579727, stop:0 rgba(55, 95, 245, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius : 10px;\n"
"\n"
"}\n"
"QProgressBar{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style : none;\n"
"border-radius : 10px;\n"
"border : 1px solid #e7e7e7;\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 9)
        self.frame_14 = QFrame(self.page_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 15, -1)
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 3, 0, 3)
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_5)


        self.verticalLayout_9.addWidget(self.frame_19, 0, Qt.AlignLeft)

        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_load_file = QPushButton(self.frame_20)
        self.btn_load_file.setObjectName(u"btn_load_file")
        self.btn_load_file.setStyleSheet(u"border : none;")
        icon2 = QIcon()
        icon2.addFile(u":/images/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load_file.setIcon(icon2)
        self.btn_load_file.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.btn_load_file)

        # self.lineEdit_mapping = QLineEdit(self.frame_20)
        self.lineEdit_mapping = DragAndDropLineEdit(self.frame_20)
        self.lineEdit_mapping.setObjectName(u"lineEdit_mapping")
        self.lineEdit_mapping.setMinimumSize(QSize(0, 40))
        self.lineEdit_mapping.setStyleSheet(u"font-size: 13px;\n"
"padding: 6px;\n"
"border: 2px solid #ccc;\n"
"border-radius: 8px;\n"
"background-color: white;\n"
"color: rgb(106, 106, 106);")

        self.horizontalLayout_11.addWidget(self.lineEdit_mapping)


        self.verticalLayout_9.addWidget(self.frame_20)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(15, 0, 15, 0)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_mapping = QTableWidget(self.frame_17)
        self.tableWidget_mapping.setObjectName(u"tableWidget_mapping")
        self.verticalLayout_12.addWidget(self.tableWidget_mapping)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_delete = QPushButton(self.frame_18)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(100, 40))
        self.btn_delete.setFont(font1)
        self.btn_delete.setStyleSheet(u"background-color: rgb(55, 95, 245);\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px 20px 20px 20px;")

        self.horizontalLayout_9.addWidget(self.btn_delete)

        self.btn_run_mapping = QPushButton(self.frame_18)
        self.btn_run_mapping.setObjectName(u"btn_run_mapping")
        self.btn_run_mapping.setMinimumSize(QSize(100, 40))
        self.btn_run_mapping.setFont(font1)
        self.btn_run_mapping.setStyleSheet(u"background-color: rgb(55, 95, 245);\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px 20px 20px 20px;")

        self.horizontalLayout_9.addWidget(self.btn_run_mapping)


        self.verticalLayout_10.addWidget(self.frame_18, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.progressBar_2 = QProgressBar(self.frame_16)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"QProgressBar::chunk{\n"
"background: qlineargradient(spread:pad, x1:1, y1:0.540273, x2:0, y2:0.579727, stop:0 rgba(55, 95, 245, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius : 10px;\n"
"\n"
"}\n"
"QProgressBar{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style : none;\n"
"border-radius : 10px;\n"
"border : 1px solid #e7e7e7;\n"
"}\n"
"\n"
"")
        self.progressBar_2.setValue(24)
        self.progressBar_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.progressBar_2)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\ub3c4\ub85c\uba85 \uc9c0\ubc88\ubcc0\ud658", None))
        self.btn_process.setText(QCoreApplication.translate("Form", u"\uc804\ucc98\ub9ac", None))
        self.btn_mapping.setText(QCoreApplication.translate("Form", u"\ub9e4\ud551", None))
        self.btn_mini.setText("")
        self.btn_close.setText("")
        self.label_3.setText("")
        self.btn_upload.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c \uc5c5\ub85c\ub4dc", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c \ubaa9\ub85d", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\uc804\uccb4\uc120\ud0dd", None))
        self.btn_run.setText(QCoreApplication.translate("Form", u"\uc2e4\ud589", None))
        self.lbl_fileName.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c\uc774\ub984", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Mapping List", None))
        self.btn_load_file.setText("")
        self.btn_delete.setText(QCoreApplication.translate("Form", u"\uc0ad\uc81c", None))
        self.btn_run_mapping.setText(QCoreApplication.translate("Form", u"\uc2e4\ud589", None))
    # retranslateUi

