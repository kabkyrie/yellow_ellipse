import sys

from random import randint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class Visual(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 600, 600, 600)
        self.move(100, 100)
        self.setWindowTitle('Рисование')

        self.button = QPushButton('Рисовать', self)
        self.button.move(250, 550)
        self.button.resize(100, 30)
        self.do_paint = False
        self.button.clicked.connect(self.paint)


class Draw(Visual):
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def drawing(self, qp):
        a_0, b_0, a_1, b_1, a_2, b_2 = randint(10, 500), randint(10, 500), randint(10, 500), \
            randint(10, 500), randint(10, 500), randint(10, 500)

        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(a_0, b_0, a_0, b_0)

        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(a_1, b_1, a_1, b_1)

        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(a_2, b_2, a_2, b_2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())
