from PyQt4 import QtCore, QtGui
from mazebfs.menu import Menu

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
