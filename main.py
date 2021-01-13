from PyQt5 import QtWidgets, QtCore, QtGui
from mazebfs.menu import Menu
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
