from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.Qt import QMainWindow
import random as r
import QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.onClicked)
        self.flag = False

    def onClicked(self):
        self.flag = True
        self.update()


    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def drawRectangles(self, qp):
        a = r.randint(10, 100)
        rndm = r.choice((1, 2, 3))
        if rndm == 1:
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            qp.drawEllipse(r.randint(10, 400), r.randint(10, 400), a, a)
        elif rndm == 2:
            qp.setPen(QPen(Qt.red, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            qp.drawEllipse(r.randint(10, 400), r.randint(10, 400), a, a)
        else:
            qp.setPen(QPen(Qt.blue, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            qp.drawEllipse(r.randint(10, 400), r.randint(10, 400), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
