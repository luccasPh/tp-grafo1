from PyQt4 import QtGui, QtCore
from mazebfs.busca import BFS
import os, sys, time

class Result(QtGui.QWidget):
    def __init__(self, rato, queijo, lab):
        super(Result, self).__init__()

        #configura o caminho das imagems
        self.image = os.path.join(os.path.dirname(__file__), 'image')
        self.timer = QtCore.QBasicTimer()
        self.rato = rato
        self.queijo = queijo
        self.lab = lab

        #chamada do algoritimo da busca em profundidade
        self.solu = iter(BFS(self.lab, self.rato, self.queijo).buscar())
        self.fim = False
        self.r_z = 0

        if self.lab[3] == 1:
            self.r_z = 0.5
            
        self.initUI()
        self.start()
        self.show()
    
    def initUI(self):
        self.setStyleSheet("QWidget { background: #32CD32 }") 
        self.setFixedSize(self.lab[1]*45, self.lab[0]*49)
        self.setWindowTitle('Jerry and the Cheeses')
    

    def start(self):
        self.timer.start(300, self)
        self.update()
    
    #função que atualizar o mapa com novas informaçoes
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for i in range(self.lab[0]):
            for j in range(self.lab[1]):
                if self.lab[2][i][j] == -1:
                    qp.drawPixmap(j*45, i*49, QtGui.QPixmap(os.path.join(self.image, 'block.png')))

        if self.rato[0] != self.queijo[0] or self.rato[1] != self.queijo[1]:
            qp.drawPixmap(self.queijo[0]*45, self.queijo[1]*49, QtGui.QPixmap(os.path.join(self.image, 'chase.png')))

        
        qp.drawPixmap(self.rato[0]*45, self.rato[1]*(48 + self.r_z), QtGui.QPixmap(os.path.join(self.image, 'player.png')))

    #função que altera as cordenadas do ratinho no mapa e depois atualizara
    def timerEvent(self, event):
        try:
            cord = next(self.solu)
            self.rato[0] = cord.v_y
            self.rato[1] = cord.v_x

        except:
            self.timer.stop()
        
        self.repaint()
        

        
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	re = Result()	
	sys.exit(app.exec_())