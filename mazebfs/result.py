from PyQt4 import QtGui, QtCore
from busca import BFS
import os, sys, time

labi1 = [   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,0,0,-1,-1,0,0,0,0,0,0,0,-1],
		    [-1,0,-1,0,0,-1,0,-1,0,-1,-1,0,-1],
		    [-1,0,0,-1,0,-1,0,-1,0,0,0,-1,-1],
		    [-1,0,-1,0,-1,0,0,0,-1,-1,0,0,-1],
            [-1,0,0,0,-1,0,-1,0,0,0,-1,0,-1],
		    [-1,0,-1,0,0,0,0,0,0,-1,0,0,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] 
        ]

class Result(QtGui.QWidget):
    def __init__(self):
        super(Result, self).__init__()
        self.image = os.path.join(os.path.dirname(__file__), 'image')
        self.timer = QtCore.QBasicTimer()
        self.rato = [10, 6]
        self.quejo = (2, 1)
        self.lab = (8,13,labi1)
        self.solu = iter(BFS(self.lab, self.rato, self.quejo).buscar())
        self.fim = False
        self.initUI()
        self.start()
    
    def initUI(self):
        self.setStyleSheet("QWidget { background: #32CD32 }") 
        self.setFixedSize(13*45, 8*49)
        self.setWindowTitle('Jerry and Cheese')
        self.show()
    

    def start(self):
        self.timer.start(200, self)
        self.update()
    
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for i in range(8):
            for j in range(13):
                if labi1[i][j] == -1:
                    qp.drawPixmap(j*45, i*49, QtGui.QPixmap(os.path.join(self.image, 'block.png')))
        
        if self.rato[0] != self.quejo[0] or self.rato[1] != self.quejo[1]:
            qp.drawPixmap(self.quejo[0]*45, self.quejo[1]*51, QtGui.QPixmap(os.path.join(self.image, 'chase.png')))

        
        qp.drawPixmap(self.rato[0]*45, self.rato[1]*48.5, QtGui.QPixmap(os.path.join(self.image, 'player.png')))
        
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