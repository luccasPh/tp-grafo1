from PyQt4 import QtGui, QtCore
from mazebfs.result import Result
import os, sys, time

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Config(QtGui.QWidget):
    def __init__(self, num):
        super(Config, self).__init__()

        #abre um arquivo texto com os layouts
        with open(os.path.join(os.path.dirname(__file__),'layout/layout{}.txt'.format(num)),'r') as l:
            layout = l.readlines()
            alt = int(layout[0].split(' ')[0])
            lar = int(layout[0].split(' ')[1])
            tipo = int(layout[0].split(' ')[2])
            lab = []

            for i in range(1,len(layout)):
                lab.append([int(n) for n in layout[i].split(' ')])

        #configura o caminha das image
        self.image = os.path.join(os.path.dirname(__file__), 'image')

        self.rato = [999, 999, False]
        self.queijo = (999, 999, False)
        self.lab = (alt, lar, lab, tipo, num)
        self.r_x = 0
        self.r_y = 0
        self.r_z = 0
        self.button_rato = False
        self.button_queijo = False
        self.result = None

        if tipo == 1:
            self.r_x = 3
            self.r_y = 2
            self.r_z = 0.5
        
        self.initUI()
        
            
    
    def initUI(self):
        self.setStyleSheet("QWidget { background: #32CD32 }") 
        self.setFixedSize(self.lab[1]*(55 + self.r_x), self.lab[0]*49)
        self.setWindowTitle('Jerry and the Cheeses')
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(self.lab[1]*46, self.lab[0]*1, 42, 54))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.image,'player.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(42, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton.clicked.connect(self.press_button_rato)

        self.pushButton2 = QtGui.QPushButton(self)
        self.pushButton2.setGeometry(QtCore.QRect(self.lab[1]*(50 + self.r_y), self.lab[0]*1, 50, 54))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.image,'chase.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setIcon(icon)
        self.pushButton2.setIconSize(QtCore.QSize(44, 43))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton2.clicked.connect(self.press_button_queijo)

        self.pushButton3 = QtGui.QPushButton(self)
        self.pushButton3.setGeometry(QtCore.QRect(self.lab[1]*46, self.lab[0]*43, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setText(_translate("Form", "START", None))
        self.pushButton3.clicked.connect(self.press_button_start)


        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(self.lab[1]*46, self.lab[0]*10, 111, 191))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">CLIQUE </span></p><p><span style=\" font-size:10pt;\">NO RATO </span></p><p><span style=\" font-size:10pt;\">OU NO</span></p><p><span style=\" font-size:10pt;\">QUEIJO</span></p><p><span style=\" font-size:10pt;\">PARA </span></p><p><span style=\" font-size:10pt;\">SELECIONAR </span></p><p><span style=\" font-size:10pt;\">SUA POSIÇÃO</span></p></body></html>", None))

        self.show()
    
    #botão do rato
    def press_button_rato(self):
        self.pushButton.setStyleSheet("background-color: red;")
        self.button_rato = True
        self.pushButton2.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.button_queijo = False
    
    #botão do queijo
    def press_button_queijo(self):
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.button_rato = False
        self.pushButton2.setStyleSheet("background-color: red;")
        self.button_queijo = True
    
    #botão do start
    def press_button_start(self):
        if self.rato[2] and self.queijo[2]:
            self.close()
            self.result = Result(self.rato, self.queijo, self.lab)
        else:
            msg = QtGui.QMessageBox(self)
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Por favor selecione a posição do rato e do qeijo!")
            msg.setStyleSheet('background-color: white;')
            msg.exec_()
    
    
    #função que atualiza o mapa com novas configuraçoes
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for i in range(self.lab[0]):
            for j in range(self.lab[1]):
                if self.lab[2][i][j] == -1:
                    qp.drawPixmap(j*45, i*49, QtGui.QPixmap(os.path.join(self.image, 'block.png')))
      
        qp.drawPixmap(self.queijo[0]*45, self.queijo[1]*49, QtGui.QPixmap(os.path.join(self.image, 'chase.png')))

        qp.drawPixmap(self.rato[0]*45, self.rato[1]*(48 + self.r_z), QtGui.QPixmap(os.path.join(self.image, 'player.png')))
    
    #função para captura o clik do mouse
    def mousePressEvent(self, event):
        x = event.x() // 45
        y = event.y() // 49
        
        if self.button_rato:
            if x < self.lab[1]:
                if self.lab[2][y][x] != -1:
                    self.rato = [x,y, True]
                    self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.button_rato = False
                    self.repaint()
        
        if self.button_queijo:
            if x < self.lab[1]:
                if self.lab[2][y][x] != -1:
                    self.queijo = (x,y, True)
                    self.pushButton2.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.button_queijo = False
                    self.repaint()
        

"""        
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	re = Select()	
	sys.exit(app.exec_())
"""