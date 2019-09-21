# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lucas/Projetos/tp-grafo1/menu.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets,QtCore, QtGui
from mazebfs.config import Config
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Menu(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Jerry and the Cheeses"))
        Form.resize(730, 389)
        self.config = None
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 61))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__),'image/logo.png')))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 181, 191))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 181, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__),'image/layout1.png')))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 88, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 100, 131, 291))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 131, 211))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__),'image/layout2.png')))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 81, 29))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 100, 201, 211))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 201, 141))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__),'image/layout3.png')))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 30, 81, 29))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(579, 100, 131, 291))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 131, 211))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__),'image/layout4.png')))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 30, 91, 29))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox.raise_()
        self.label.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()

        self.pushButton.clicked.connect(lambda:self.press_button(Form, 1))
        self.pushButton_2.clicked.connect(lambda:self.press_button(Form, 2))
        self.pushButton_3.clicked.connect(lambda:self.press_button(Form, 3))
        self.pushButton_4.clicked.connect(lambda:self.press_button(Form, 4))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def press_button(self, Form, num):
        Form.close()
        self.config = Config(num)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "LABIRINTO 1", None))
        self.pushButton.setText(_translate("Form", "SELECT", None))
        self.groupBox_2.setTitle(_translate("Form", "LABRINTO 2", None))
        self.pushButton_2.setText(_translate("Form", "SELECT", None))
        self.groupBox_3.setTitle(_translate("Form", "LABIRINTO 3", None))
        self.pushButton_3.setText(_translate("Form", "SELECT", None))
        self.groupBox_4.setTitle(_translate("Form", "LABIRINTO 4", None))
        self.pushButton_4.setText(_translate("Form", "SELECT", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""

