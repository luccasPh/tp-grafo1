from PyQt4 import QtCore, QtGui
from mazebfs.menu import Menu
import sys


def main():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
