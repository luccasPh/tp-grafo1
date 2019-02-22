# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lucas/Projetos/tp-grafo1/mazebfs/fim.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Fim(QtGui.QWidget):
    def __init__(self, other, num):
        super(Fim, self).__init__()
        self.num = num
        self.other = other
        self.config = None
        self.setupUi()
        self.show()

    def setupUi(self):
        image = os.path.join(os.path.dirname(__file__), 'image')
        self.setObjectName(_fromUtf8("Form"))
        self.resize(350, 290)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(350, 290))
        self.setMaximumSize(QtCore.QSize(350, 290))

        self.label = QtGui.QLabel(self)
        movie = QtGui.QMovie(os.path.join(image, 'fim.gif'))
        self.label.setGeometry(QtCore.QRect(10, 40, 331, 201))
        #self.label.setText(_fromUtf8(""))
        self.label.setMovie(movie)
        movie.start()
        self.label.setObjectName(_fromUtf8("label"))

        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 88, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.press_button_menu)

        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 250, 88, 29))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.press_button_config)

        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def press_button_menu(self):
        self.close()
        from mazebfs.menu import Menu
        self.tela = QtGui.QWidget()
        self.menu = Menu()
        self.menu.setupUi(self.tela)
        self.tela.show()
    
    def press_button_config(self):
        self.close()
        from mazebfs.config import Config
        self.config = Config(self.num)

    
    def closeEvent(self, event):
        self.other.close()
        event.accept()

    def retranslateUi(self):
        self.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Menu", None))
        self.pushButton_2.setText(_translate("Form", "Configura", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">FIM</span></p></body></html>", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Fim()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""

