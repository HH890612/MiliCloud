# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(854, 692)
        Widget.setMaximumSize(854, 692)
        Widget.setMinimumSize(854, 692)
        self.shotGB = QtGui.QGroupBox(Widget)
        self.shotGB.setGeometry(QtCore.QRect(40, 130, 351, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shotGB.setFont(font)
        self.shotGB.setObjectName("shotGB")
        self.serchShots = QtGui.QLineEdit(self.shotGB)
        self.serchShots.setGeometry(QtCore.QRect(10, 30, 331, 20))
        self.serchShots.setObjectName("serchShots")
        self.shotScrollArea = QtGui.QScrollArea(self.shotGB)
        self.shotScrollArea.setGeometry(QtCore.QRect(10, 60, 331, 431))
        self.shotScrollArea.setWidgetResizable(True)
        self.shotScrollArea.setObjectName("shotScrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.shotScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget = QtGui.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 771, 99))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.projectNameEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.verticalLayout.addWidget(self.projectNameEdit)
        self.projectDescEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.projectDescEdit.setObjectName("projectDescEdit")
        self.verticalLayout.addWidget(self.projectDescEdit)
        self.tasksGB = QtGui.QGroupBox(Widget)
        self.tasksGB.setGeometry(QtCore.QRect(450, 130, 361, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tasksGB.setFont(font)
        self.tasksGB.setObjectName("tasksGB")
        self.searchTasks = QtGui.QLineEdit(self.tasksGB)
        self.searchTasks.setGeometry(QtCore.QRect(10, 30, 341, 20))
        self.searchTasks.setObjectName("searchTasks")
        self.tasksScrollArea = QtGui.QScrollArea(self.tasksGB)
        self.tasksScrollArea.setGeometry(QtCore.QRect(10, 60, 341, 431))
        self.tasksScrollArea.setWidgetResizable(True)
        self.tasksScrollArea.setObjectName("tasksScrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 339, 429))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tasksScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.myTaskCK = QtGui.QCheckBox(Widget)
        self.myTaskCK.setGeometry(QtCore.QRect(40, 650, 121, 21))
        self.myTaskCK.setObjectName("myTaskCK")
        self.createBtn = QtGui.QPushButton(Widget)
        self.createBtn.setGeometry(QtCore.QRect(450, 650, 75, 23))
        self.createBtn.setObjectName("createBtn")
        self.selBtn = QtGui.QPushButton(Widget)
        self.selBtn.setGeometry(QtCore.QRect(640, 650, 75, 23))
        self.selBtn.setObjectName("selBtn")
        self.cancelBtn = QtGui.QPushButton(Widget)
        self.cancelBtn.setGeometry(QtCore.QRect(740, 650, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "选择工作文件", None, QtGui.QApplication.UnicodeUTF8))
        self.shotGB.setTitle(QtGui.QApplication.translate("Widget", "Shots&&Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.projectNameEdit.setText(QtGui.QApplication.translate("Widget", "项目名字", None, QtGui.QApplication.UnicodeUTF8))
        self.projectDescEdit.setHtml(QtGui.QApplication.translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">项目描述</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tasksGB.setTitle(QtGui.QApplication.translate("Widget", "Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.myTaskCK.setText(QtGui.QApplication.translate("Widget", "仅显示我的任务", None, QtGui.QApplication.UnicodeUTF8))
        self.createBtn.setText(QtGui.QApplication.translate("Widget", "新建", None, QtGui.QApplication.UnicodeUTF8))
        self.selBtn.setText(QtGui.QApplication.translate("Widget", "选择", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("Widget", "取消", None, QtGui.QApplication.UnicodeUTF8))
