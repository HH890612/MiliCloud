# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(598, 282)
        Widget.setMaximumSize(598, 282)
        Widget.setMinimumSize(598, 282)
        self.formLayoutWidget = QtGui.QWidget(Widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 521, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.taskLab = QtGui.QLabel(self.formLayoutWidget)
        self.taskLab.setObjectName("taskLab")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.taskLab)
        self.taskTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.taskTxt.setObjectName("taskTxt")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.taskTxt)
        self.pipLab = QtGui.QLabel(self.formLayoutWidget)
        self.pipLab.setObjectName("pipLab")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pipLab)
        self.pipTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.pipTxt.setObjectName("pipTxt")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pipTxt)
        self.creatorLab = QtGui.QLabel(self.formLayoutWidget)
        self.creatorLab.setObjectName("creatorLab")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.creatorLab)
        self.creatorTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.creatorTxt.setObjectName("creatorTxt")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.creatorTxt)
        self.shotLab = QtGui.QLabel(self.formLayoutWidget)
        self.shotLab.setObjectName("shotLab")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.shotLab)
        self.shotTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.shotTxt.setObjectName("shotTxt")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.shotTxt)
        self.cancelBtn = QtGui.QPushButton(Widget)
        self.cancelBtn.setGeometry(QtCore.QRect(490, 230, 71, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.creBtn = QtGui.QPushButton(Widget)
        self.creBtn.setGeometry(QtCore.QRect(400, 230, 71, 23))
        self.creBtn.setObjectName("creBtn")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "新建任务", None, QtGui.QApplication.UnicodeUTF8))
        self.taskLab.setText(QtGui.QApplication.translate("Widget", "任务名", None, QtGui.QApplication.UnicodeUTF8))
        self.pipLab.setText(QtGui.QApplication.translate("Widget", "步骤", None, QtGui.QApplication.UnicodeUTF8))
        self.creatorLab.setText(QtGui.QApplication.translate("Widget", "创建人", None, QtGui.QApplication.UnicodeUTF8))
        self.shotLab.setText(QtGui.QApplication.translate("Widget", "shot名称", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("Widget", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.creBtn.setText(QtGui.QApplication.translate("Widget", "新建", None, QtGui.QApplication.UnicodeUTF8))